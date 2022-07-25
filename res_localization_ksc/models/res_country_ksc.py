from odoo import models, fields, api


class ResLocalizationKsc(models.Model):
    _inherit = 'res.country.ksc'

    state_ids = fields.One2many('res.state.ksc', 'country_Name_id', string="State Name")
