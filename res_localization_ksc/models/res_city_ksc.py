from odoo import models, fields, api

class ResLocalizationKsc(models.Model):
    _inherit = 'res.city.ksc'

    state_id = fields.Many2one('res.state.ksc', string="State Name id", help='many cities belong to one state')




