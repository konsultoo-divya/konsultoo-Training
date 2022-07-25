from odoo import api, models, fields


class StockLocationKsc(models.Model):
    _name = 'stock.location.ksc'
    _description = 'Stock Location Ksc'

    name = fields.Char(string='name')
    parent_id = fields.Many2one('stock.location.ksc', string='parent_id')
    location_type = fields.Selection([('vendor', 'Vendor'), ('customer', 'Customer'), ('internal', 'Internal'), ('inventory_loss', 'Inventory Loss'), ('production', 'Production'), ('transit', 'Transit'), ('view', 'View')])
    is_scrap_location = fields.Boolean(string='is_scrap_location')