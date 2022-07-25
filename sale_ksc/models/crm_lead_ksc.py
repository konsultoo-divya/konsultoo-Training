from odoo import models, fields, api
from datetime import date


class CrmLeadKsc(models.Model):
    _name = 'crm.lead.ksc'
    _description = 'Crm Lead Ksc'

    customer_name = fields.Char(string='Customer Name', required=True, help='about name')
    customer_email = fields.Char(string='customer Email', required=True, help='about email')
    customer_phone = fields.Char(string="Customer phone", required=True, help='about phone number')
    expected_revenue = fields.Float(string="Expected revenue", digit=(14, 3), help='about expected revenue')
    sales_person = fields.Char(string="Salesperson", required=True, help='about sale person')
    sales_team = fields.Char(string="Sales Team", help='about sales team')
    campaign = fields.Char(string="Campaign", help='about campaign')
    channel = fields.Selection(
        [('facebook', 'Facebook'), ('whatsapp', 'Whatsapp'), ('email', 'Email'), ('newspaper', 'Newspaper'),
         ('television', 'Television'), ('phone call', 'Phone Call'), ('sms', 'SMS'), ('google', 'Google')],
        required=True, help='about channel')
    state = fields.Selection(
        [('new', 'New'), ('qualified', 'Qualified'), ('proposition', 'Proposition'), ('won', 'Won'), ('lost', 'Lost')],
        help='about state')
    followup = fields.Date(string="Next Follow Up Date", help='about followup')
    won_date = fields.Date(string="Won Date", required=True, help='about won date')
    lost_date = fields.Date(string="Lost reason", required=True, help='about lost won')
    # Requirement - 5 Bring crm.lead.ksc model and its view to this module
    partner_id = fields.Many2one('res.partner.ksc', help='about partner id')
    order_ids = fields.One2many('sale.order.ksc', 'lead_id', readonly=True, help='order ids')
    lead_line_ids = fields.One2many('crm.lead.line.ksc', 'crm_lead_id', string='lead_line_ids', help='lead line ids')

    # mark won status to lead(when lead is won)
    def action_lead_won(self):
        self.update({
            'state': 'won'
        })

    # mark lost status to lead(when lead is lost)
    def action_lead_lost(self):
        self.update({
            'state': 'lost'
        })
