from odoo import api, models, fields
from datetime import datetime


class StockInventoryKsc(models.Model):
    _name = 'stock.inventory.ksc'
    _description = 'Stock Inventory Ksc'

    name = fields.Char()
    state = fields.Selection(
        [('draft', 'Draft'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')])
    location_id = fields.Many2one('ksc.stock.location')
    inventory_date = fields.Date(default=datetime.today())
    inventory_line_ids = fields.One2many('stock.inventory.line.ksc', 'stock_inventory_id')


    def action_start_inventory(self):
        self.state = 'in_progress'
        if self.inventory_line_ids:
            for each_product in self.inventory_line_ids:
                each_product.available_qty = each_product.product_id.with_context(
                    {'get_location': self.location_id.id}).product_qty
