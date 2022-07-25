from odoo import api, fields, models, _

class SaleOrderKsc(models.Model):
    _name = 'sale.order.ksc'
    _description = 'Sale Order Ksc'

    order_number = fields.Char(string='Order Number', required=True, copy=False,
                               index=True, default=lambda self: _('New'), readonly=True)
    customer_id = fields.Many2one('res.partner.ksc', required=True)
    invoice_customer_id = fields.Many2one('res.partner.ksc', required=True)
    shipping_customer_id = fields.Many2one('res.partner.ksc', required=True)
    sale_order_date = fields.Date()
    order_line_ids = fields.One2many('sale.order.line.ksc', 'order_no_id')
    salesperson_id = fields.Many2one('res.users')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft')
    order_total = fields.Float(string="Order Total")
    total_weight = fields.Float(compute='_compute_total_weight', store=True)
    lead_id = fields.Many2one('crm.lead.ksc', string='lead_id')
    warehouse_id = fields.Many2one('stock.warehouse.ksc')
    picking_ids = fields.One2many('stock.picking.ksc', 'order_id')
    delivery_count = fields.Integer(compute='_compute_delivery_count', string='Delivery Count', store=True)
    amount_untaxed = fields.Float(compute='_compute_untaxed_amount')
    total_tax = fields.Float(compute='_compute_total_tax', store=True)
    total_amount = fields.Float(compute='_compute_total_amount', store=True)

    @api.depends('order_line_ids.product_id')
    def _compute_total_weight(self):
        '''
             Add field total_weight in sale.order.ksc model, which should be computed field
             with 2 decimals and  should not be stored in database -
             it will calculate the weight from sale.order.line.ksc -&gt; product_id field
        '''
        for rec in self:
            if rec.order_line_ids:
                sum_weight = 0
                for records in rec.order_line_ids:
                    sum_weight += records.product_id.weight
                rec.total_weight = sum_weight


    def action_confirm_order(self):
        '''
        conform order and move stocks from one location to another location
        for  Requirement - 5
        '''
        self.state = 'confirmed'
        picking = self.env['stock.picking.ksc'].create({
            'name': self.order_number,
            'partner_id': self.customer_id.id,
        })
        self.env['stock.move.ksc'].create({
            'source_location_id': self.warehouse_id.stock_location_id.id
        })
        for recs in self.order_line_ids:
            recs.state = 'confirmed'
            self.env['stock.move.ksc'].create({
                'product_id': recs.product_id.id,
                'name': recs.name,
                'qty_to_deliver': recs.quantity,
                'sale_line_id': recs.id,
                'uom_id': recs.uom_id,
                'destination_location_id': self.env['stock.location.ksc'].search([('location_type', '=', 'customer')],
                                                                                 limit=1).id,
                'picking_id': picking.id
            })


    @api.depends('picking_ids')
    def _compute_delivery_count(self):
        '''  Add button-box at the top right corner of the screen for Delivery order(Requirement - 11 )
             calculates delivery counts
        '''
        for rec in self:
            rec.delivery_count = len(rec.picking_ids.ids)

    def action_view_delivery(self):
        # shows delivery pop up and sets values in view
        action = self.env["ir.actions.actions"]._for_xml_id("sale_ksc.action_stock_picking_ksc")
        pickings = self.mapped('picking_ids')
        if len(pickings) == 1:
            picking = pickings[0]
            action['res_id'] = picking.id
            action['view_mode'] = 'form'
            form_view = [(self.env.ref("sale_ksc.form_view_sale_order_ksc").id, 'form')]
            action['views'] = form_view
        else:
            action['view_mode'] = 'tree,form'
            action['domain'] = [('id', 'in', pickings.ids)]
        return action

    @api.depends('order_line_ids')
    def _compute_untaxed_amount(self):
        '''
            calculate untaxed amount (Requirement - 13)
        '''
        for order in self:
            order.amount_untaxed = 0
            for line in order.order_line_ids:
                order.amount_untaxed += line.subtotal

    @api.depends('order_line_ids')
    def _compute_total_tax(self):
        ''' calculate total tax in order line ids '''
        for order in self:
            order.total_tax = 0
            for line in order.order_line_ids:
                order.total_tax += line.subtotal_tax
    @api.depends('order_line_ids')
    def _compute_total_amount(self):
        '''  calculate total amount of amount untaxed and total tax '''
        for order in self:
            order.total_amount = order.amount_untaxed + order.total_tax
