from odoo import models, fields, api


class ResCityKsc(models.Model):
    _name = 'res.city.ksc'
    _description = 'Res City Ksc'
    _rec_name = 'city_name'

    city_name = fields.Char(string='City Name',help='City Name')
    state_name = fields.Char(string='State Name', help='State Name', copy='False')
    active = fields.Boolean(string='Active', default=True,help='Active City')



