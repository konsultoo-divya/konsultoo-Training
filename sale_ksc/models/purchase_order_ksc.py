from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class PurchaseOrderKsc(models.Model):
    _name = 'purchase.order.ksc'
    _description = 'Purchase Order Ksc'

    order_number = fields.Char(string='order_number')
    warehouse_id = fields.Many2one('stock.warehouse.ksc')
    partner_id = fields.Many2one('res.partner.ksc', string='Vendor')
    vendor_reference = fields.Char()
    order_deadline = fields.Date()
    receipt_date = fields.Date()
    purchase_line_ids = fields.One2many('purchase.order.line.ksc', 'order_no_id')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')])
    total_weight = fields.Float(compute='_compute_total_weight', store=True)
    order_total = fields.Float(compute='_compute_order_total', store=True)
    def action_confirm_order(self):
        '''
            Add a button in purchase order to confirm the order.
            When the purchase order is confirmed,
            Requirement - 6
        '''
        self.state = 'confirmed'
        if not self.partner_id:
            raise ValidationError(_('Create Customer First'))
        else:
            picking = self.env['stock.picking.ksc'].create({
                'partner_id': self.partner_id.id,
                'purchase_order_id': self.id,
                'transaction_type': 'in',
            })

            for rec in self.purchase_line_ids:
                self.env['stock.move.ksc'].create({
                    'product_id': rec.product_id.id,
                    'uom_id': rec.uom_id.id,
                    'qty_to_deliver': rec.quantity,
                    'purchase_line_id': rec.id,
                    'source_location_id': self.env['stock.location.ksc'].search([('location_type', '=', 'vendor')],
                                                                                limit=1).id,
                    'picking_id': picking.id,
                    'destination_location_id': rec.order_no_id.warehouse_id.stock_location_id.id,
                })
    @api.depends('purchase_line_ids.product_id')
    def _compute_total_weight(self):
        '''
            calculate total weight based on individual product in purchase lines
        '''
        for rec in self:
            if rec.purchase_line_ids:
                sum_weight = 0
                for records in rec.purchase_line_ids:
                    sum_weight += records.product_id.weight
                rec.total_weight = sum_weight

    @api.depends('purchase_line_ids.subtotal')
    def _compute_order_total(self):
        '''
            calculate order total  based on individual product in purchase lines
        '''
        for rec in self:
            if rec.purchase_line_ids:
                sum_weight = 0
                for records in rec.purchase_line_ids:
                    sum_weight += records.product_id.subtotal
                rec.total_weight = sum_weight

