from odoo import api, models, fields
from odoo.exceptions import ValidationError


class StockPickingKsc(models.Model):
    _name = 'stock.picking.ksc'
    _description = 'Stock Picking Ksc'

    name = fields.Char(string='name')
    partner_id = fields.Many2one('res.partner.ksc')
    back_order_id = fields.Many2one('stock.picking.ksc')
    state = fields.Selection([('draft', 'Draft'), ('cancel', 'Cancelled'), ('validate', 'Validate')], default='draft')
    purchase_order_id = fields.Many2one('purchase.order.ksc')
    transaction_type = fields.Selection([('in', 'IN'), ('out', 'OUT')])
    move_ids = fields.One2many('stock.move.ksc', 'picking_id')
    transaction_date = fields.Date(default=fields.Date.context_today)
    order_id = fields.Many2one('sale.order.ksc')
    parent_picking_id = fields.Many2one('stock.picking.ksc')
    # requirement 11 :compute method for button-box
    move_ids = fields.One2many('stock.move.ksc', 'picking_id', string='Move Ids')
    stock_move_count = fields.Integer(compute='_compute_stock_move_count', string='Stock Move Count', store=True)

    @api.depends('move_ids', 'stock_move_count')
    def _compute_stock_move_count(self):
        for rec in self:
            rec.stock_move_count = len(rec.move_ids.ids)

    def action_view_moving(self):
        '''
            This function returns an action that displays the opportunities from partner.
             requirement 11: If there are more than one stock move, open list view of the stock move with
             listing only stock moves which are associated with that sales order
        '''

        action = self.env["ir.actions.actions"]._for_xml_id("sale_ksc.action_stock_move_ksc")
        action['domain'] = [('id', 'in', self.move_ids.ids)]
        move = self.move_ids
        if len(move) == 1:
            action['views'] = [(self.env.ref('sale_ksc.form_view_stock_move_ksc').id, 'form')]
            action['res_id'] = move.id
        return action
