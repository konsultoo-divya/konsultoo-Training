from odoo import api, models, fields

class StockWarehouseKsc(models.Model):
    _name = 'stock.warehouse.ksc'
    _description = 'Stock Warehouse Ksc'

    name = fields.Char()
    short_code = fields.Char(required=True)
    address_id = fields.Many2one('res.partner.ksc')
    stock_location_id = fields.Many2one('stock.location.ksc', string='stock_location_id')
    view_location_id = fields.Many2one('stock.location.ksc', string='view_location_id')