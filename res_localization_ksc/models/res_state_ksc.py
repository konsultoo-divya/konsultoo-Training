from odoo import models, fields, api


class ResStateKsc(models.Model):
    _inherit = 'res.state.ksc'

    country_Name_id = fields.Many2one('res.country.ksc', string='Country Name id', help='many state has one country')
    city_ids = fields.One2many('res.city.ksc', 'state_id', string="City Name", help='one state has many cities')


