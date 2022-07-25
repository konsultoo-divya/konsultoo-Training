from odoo import api, models, fields


class ResPartnerKsc(models.Model):
    _name = 'res.partner.ksc'
    _description = 'Res Partner Ksc'

    photo = fields.Image()
    name = fields.Char()
    street1 = fields.Char()
    street2 = fields.Char()
    birthdate = fields.Date('Birthdate', help='Enter Birthdate')
    country_id = fields.Many2one('res.partner.ksc')
    state_id = fields.Many2one('res.state.ksc')
    city_id = fields.Many2one('res.city.ksc')
    zip_code = fields.Char()
    email = fields.Char()
    mobile = fields.Char()
    phone = fields.Char()
    website = fields.Char()
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('res.partner.ksc')
    child_ids = fields.One2many('res.partner.ksc', 'parent_id')
    address_type = fields.Selection([('invoice', 'Invoice'), ('shipping', 'Shipping'), ('contact', 'Contact')])