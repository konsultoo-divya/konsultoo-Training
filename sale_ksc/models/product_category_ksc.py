from odoo import api, fields, models

class ProductCategoryKsc(models.Model):
    _name = 'product.category.ksc'
    _description = 'Product Category Ksc'

    name = fields.Char(required=True, help='about name')
    parent_id = fields.Many2one('product.category.ksc', string='parent_id', help='parent id')
