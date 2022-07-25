from odoo import api, models, fields


class ProductUomCategoryKsc(models.Model):
    _name = 'product.uom.category.ksc'
    _description = 'Product Umo Category Ksc'

    name = fields.Char(string='Uom Category Name', help='about uom category')
    uom_ids = fields.One2many('product.uom.ksc', 'uom_category_id', string='uom_category_id')