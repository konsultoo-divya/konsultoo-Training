from odoo import fields, api, models

class ProductUomKsc(models.Model):
    _name = 'product.uom.ksc'
    _description = 'Product Uom Ksc'

    name = fields.Char(string="Name")
    uom_category_id = fields.Many2one('product.uom.category.ksc', string="UOM Category")