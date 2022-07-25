from odoo import api, models, fields

class AccountTaxKsc(models.Model):
    _name = 'account.tax.ksc'
    _description = 'Account Tax Ksc'

    name = fields.Char()
    tax_use = fields.Selection([('none', 'None'), ('sales', 'Sales'), ('purchase', 'Purchase')],help='about tax use')
    tax_value = fields.Float(string='Amount',help='about tax value')
    tax_amount_type = fields.Selection([('percentage', 'Percentage'), ('fixed', 'Fixed')], default='percentage',help='about tax amount type')