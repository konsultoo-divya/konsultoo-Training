from odoo import models, fields, api


class ProductKsc(models.Model):
    _name = 'product.ksc'
    _description = 'product Ksc'

    name_of_the_product = fields.Char(string='Name of The Product', help='about product name')
    stock_keeping_unit = fields.Char(string='SKU', help='about stock keeping unit')
    barcode = fields.Boolean(string='Barcode of The Product',help='about barcode')
    sold_product = fields.Char(string="Can This Product Be Sold",help='about sold product')
    product_type = fields.Selection([('storable', 'Storable'),
                                     ('consumable', 'Consumable'),
                                     ('service', 'Service'),
                                     ], string='Product Type',help='about product type')
    sale_price = fields.Float(string="Sale Price", digits=(12, 6),help='sale price')
    cost_price = fields.Float(string="Cost Price", digits=(12, 6),help='about cost price')
    active = fields.Boolean(string='Active', help='about active')
    warehouse = fields.Char(string="Warehouse",help='about Wherehouse')
    product_image = fields.Image(string="Product Image",copy=False, attachment=True, max_width=1024, max_height=1024 )
    website_description = fields.Html(string="Website Description",help='about Web Description')
    Internal_Note = fields.Text(string="Internal Note", help='about Internal Notes')








