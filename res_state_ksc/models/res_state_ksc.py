from odoo import models, fields, api

class ResStateKsc(models.Model):
    _name = 'res.state.ksc'
    _description = 'Res State Ksc'
    _rec_name = 'name_of_the_state'

    name_of_the_state = fields.Char(string='Name of The State',help='Name Field',  translate=True)
    short_code_of_the_state = fields.Char(string='Short Code of The State', help='about the state code')
    country_Name = fields.Char(string="Country_Name",help='about the Country name', copy='False')
    active = fields.Boolean(string='Active',help='this fields for the active')



