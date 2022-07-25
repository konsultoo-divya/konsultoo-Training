from odoo import api, models, fields
from datetime import datetime


class StockInventoryLineKsc(models.Model):
    _name = 'stock.inventory.line.ksc'
    _description = 'Stock Inventory Line Ksc'

    product_id = fields.Many2one('product.ksc')
    available_qty = fields.Float(string='available_qty')
    counted_product_qty = fields.Float(string='counted_product_qty')
    difference = fields.Float(compute='_compute_difference', string='difference')

    @api.depends('counted_product_qty', 'available_qty')
    def _compute_difference(self):
        for rec in self:
            rec.difference = rec.counted_product_qty * rec.available_qty

    stock_inventory_id = fields.Many2one('stock.inventory.ksc')