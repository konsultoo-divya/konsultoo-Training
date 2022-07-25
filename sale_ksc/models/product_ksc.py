from odoo import api, models, fields


class KscProduct(models.Model):
    _name = 'product.ksc'
    _description = 'Product Ksc'

    name = fields.Char(string='product name')
    sku = fields.Char(string="SKU", help='about the SKU')
    weight = fields.Float(string='Weight', help='about weight',digits=(10, 2))
    length = fields.Float(string='Length', help='about Length',digits=(10, 2))
    volume = fields.Float(string='width', help='about volume', digits=(10, 2))
    width = fields.Float(digits=(10, 2), help='about weight')
    barcode = fields.Char(string='Barcode', help='about barcode')
    product_type = fields.Selection([('storable', 'Storable'), ('consumable', 'Consumable'), ('service', 'Service')])
    sale_price = fields.Float(digits=(6, 2), default=1.00, help='about the sale price')
    cost_price = fields.Float(digits=(6, 2), default=1.00, help='about the cost price')
    product_category_id = fields.Many2one('product.category.ksc',help='about Product Category Many product has one category')
    uom_id = fields.Many2one('product.uom.ksc',help='about many to one of product uom')
    product_stock = fields.Float(string='Product Stock', store=False, help='about the product stock quantity')
    tax_ids = fields.Many2many('account.tax.ksc', domain="[('tax_use', '=', 'sales')]", help='about the m2m of account tax master')

    def new_function_object_type(self):
        '''
        This function returns an action that displays the opportunities from partner.
        Add a button of type ‘object’ on the form view of the product.
        # requirement : 9
        '''
        action = self.env["ir.actions.actions"]._for_xml_id("sale_ksc.action_product_stock_update_ksc")
        action['domain'] = [('id', 'in', self.uom_id.ids)]
        action['context'] = {
            'active_id': self._context.get('active_id'),
            'active_model': 'product.stock.update.ksc',
        }
        return action
