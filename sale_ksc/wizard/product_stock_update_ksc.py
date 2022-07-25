from odoo import models, fields, api


class ProductStockUpdateKsc(models.TransientModel):
	_name = 'product.stock.update.ksc'
	_description = 'product stock update ksc'

	location_id = fields.Many2one(comodel_name='stock.location.ksc', string='Location',
								  domain="[('location_type','=','Internal')]")
	current_stock = fields.Float(string='Current Stock')
	counted_stock = fields.Float(string='Counted Stock')
	difference_qty = fields.Float(string='Difference Qty', compute='_compute_counted_stock_difference')

	def _compute_counted_stock_difference(self):
		for product in self:
			product.difference_qty = product.counted_stock - product.current_stock
	#
	# @api.onchange('location_id')
	# def onchange_location(self):
	# 	product = self.env['product.ksc'].browse(self.env.context['active_ids'])
	# 	self.current_stock = product.with_context(get_location=self.location_id.id).product_qty

	def update_stock(self):
		if self.location_id:
			product = self.env['product.ksc'].browse(self.env.context['active_ids'])
			inventory = self.env['stock.inventory.ksc'].create(
				{
					'name': '3 month review for ' + product.name + ' management',
					'location_id': self.location_id.id,
					'stock_inventory_line_ids': [(0, 0, {
						'product_id': product.id,
						'available_qty': self.current_stock,
						'counted_product_qty': self.counted_stock
					})]
				}
			)
			inventory.validate_inventory()