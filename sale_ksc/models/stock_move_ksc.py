from odoo import api, models, fields


class StockMoveKsc(models.Model):
    _name = 'stock.move.ksc'
    _description = 'Stock Move Ksc'

    name = fields.Char(string='Description')
    product_id = fields.Many2one('product.ksc', required=True)
    uom_id = fields.Many2one('product.uom.ksc', required=True)
    source_location_id = fields.Many2one('stock.location.ksc')
    destination_location_id = fields.Many2one('stock.location.ksc')
    qty_to_deliver = fields.Float(string='qty_to_deliver')
    qty_delivered = fields.Float(string='qty_delivered')
    state = fields.Selection([('draft', 'Draft'), ('cancel', 'Cancelled'), ('validate','Validate')], default='draft')
    sale_line_id = fields.Many2one('sale.order.line.ksc', string='sale_line_id')
    purchase_line_id = fields.Many2one('purchase.order.line.ksc')
    stock_inventory_id = fields.Many2one('stock.inventory.ksc')
    picking_id = fields.Many2one('stock.picking.ksc', string='picking_id')