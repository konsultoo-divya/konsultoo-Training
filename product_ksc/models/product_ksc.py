from odoo import models, fields, api


class ProductKsc(models.Model):
    _name = 'product.ksc'
    _description = 'product Ksc'

    name_of_the_product = fields.Char(string='Name of The Product')
    stock_keeping_unit = fields.Char(string='SKU')
    barcode = fields.Boolean(string='Barcode of The Product')
    sold_product = fields.Char(string="Can This Product Be Sold")
    product_type = fields.Selection([('storable', 'Storable'),
                                     ('consumable', 'Consumable'),
                                     ('service', 'Service'),
                                     ], string='Product Type')
    sale_price = fields.Float(string="Sale Price", digits=(12,6))
    cost_price = fields.Float(string="Cost Price", digits=(12,6))
    active = fields.Boolean(string='Active')
    warehouse = fields.Char(string="Warehouse")
    # product_image = fields.image(string="Product Image")
    website_description = fields.Html(string="Website Description")
    Internal_Note = fields.Text(string="Internal Note")








