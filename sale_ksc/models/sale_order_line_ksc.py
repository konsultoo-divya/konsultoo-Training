from odoo import api, models, fields


class SaleOrderLineKsc(models.Model):
    _name = 'sale.order.line.ksc'
    _description = 'Sale order Line Ksc'

    order_no_id = fields.Many2one('sale.order.ksc')
    product_id = fields.Many2one('product.ksc')
    name = fields.Text(string='Description')
    quantity = fields.Float(digits=(6, 2))
    unit_price = fields.Float(digits=(6, 2))
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')])
    uom_id = fields.Many2one('product.uom.ksc')
    subtotal = fields.Float(compute='_compute_subtotal', store=True)
    warehouse_id = fields.Many2one('stock.warehouse.ksc')
    tax_ids = fields.Many2many('account.tax.ksc', domain="[('tax_use', '=', 'sales')]")
    subtotal_tax = fields.Float('Subtotal Tax', compute='_compute_total_tax', store=True)

    @api.onchange('product_id')
    def _onchange_product(self):
        '''
            # Requirement - 4 When product is selected on sale.order.line.ksc,
            fetch the unit price from product model, also set the quantity as 1 - use onchange method
        '''
        if self.product_id:
            self.unit_price = self.product_id.sale_price
            self.quantity = 1

    @api.depends('quantity', 'unit_price')
    def _compute_subtotal(self):
        '''
         subtotal_without_tax - Float - computed field which is stored in database,
         which depends on order  line qty and order line unit price
         Requirement - 4
        '''
        for rec in self:
            rec.subtotal = rec.quantity * rec.unit_price


    @api.depends('quantity', 'unit_price', 'tax_ids')
    def _compute_total_tax(self):
        '''
            When product is selected, bring the taxes from product and
            set it in the sales order line - use onchange of product_id
             Requirement - 13
        '''
        for line in self:
            line.tax_ids = line.product_id.tax_ids.filtered(lambda tax: tax.tax_use == 'sales')

            line.subtotal_tax = sum(list(
                map(lambda x: (x.tax_value * line.unit_price * line.quantity / 100),
                    filter(lambda x: x.tax_amount_type == 'percentage', line.tax_ids)
                    )))

            line.subtotal_tax += sum(list(
                map(lambda x: x.tax_value,
                    filter(lambda x: x.tax_amount_type == 'fixed', line.tax_ids)
                    )))
