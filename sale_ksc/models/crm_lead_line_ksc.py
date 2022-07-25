from odoo import api, models, fields
from datetime import date


class CrmLeadLineKsc(models.Model):
    _name = 'crm.lead.line.ksc'
    _description = 'Crm Lead line Ksc'

    product_id = fields.Many2one('product.ksc',help='about product id', string='product_id')
    name = fields.Char(string='name',help='about name')
    expected_sell_qty = fields.Float(string='expected_sell_qty',help='about expected sell qautity')
    uom_id = fields.Many2one('product.uom.ksc',help='about uom id', string='uom_id')
    # order_ids - O2M - keep it readonly, record will not be generated from here,# it is just for the display purpose
    crm_lead_id = fields.Many2one('crm.lead.ksc', help='about crm lead id', string='crm_lead_id')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        '''
         update product name when product selection is changed
        '''
        self.name = self.product_id.name
