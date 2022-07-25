from odoo import models, fields, api
from datetime import date
from datetime import datetime

class Customers(models.Model):
    _name = 'res.partner.demo.ksc'
    _description = 'res partner Data'

    name = fields.Char(string='Name', translate=True,help='name')
    email = fields.Char(string="Email Id",help='email')
    street1 = fields.Char(string="Street1",help='Enter street1')
    street2 = fields.Char(string="street2",help='Enter street2')
    city = fields.Char(string="City",help='Enter city')
    state = fields.Char(string="State",help='Enter state')
    zip_code = fields.Char(string="Zip Code",help='enter zip code')
    country = fields.Char(string="Country",help='enter country')
    birthdate = fields.Date(string='BirthDate',help='enter birthdate', default=datetime.today())
    age = fields.Integer(string="Age",help='enter age', compute='_compute_age')
    weight = fields.Float(string="Weight",help='enter weight')
    description = fields.Text(string="Description",help='description for the res partner ')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('transgender)', 'Transgender)')],
                              default='female',help='enter gender', string="Gender")
    detail = fields.Html('Detail', sanitize=True, help='detail html tag',trip_style=False)
    is_spectacles = fields.Boolean(string="Is_spectacles",help='enter true/False')
    extra_detail = fields.Html(string="extra_detail",help='enter extra detail')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status',help='enter state', readonly=True, copy=False)

    
    @api.depends("birthdate")
    '''
    	 calculating age base on Birthdate using @api depends()	
    '''
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birthdate:
                rec.age = today.year - rec.birthdate.year
            else:
                rec.age = 1
