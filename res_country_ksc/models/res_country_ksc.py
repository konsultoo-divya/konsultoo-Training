from odoo import models, fields, api

class ResCountryKsc(models.Model):
    _name = 'res.country.ksc'
    _description = 'Res country Ksc'
    _rec_name = 'name_of_the_country'

    name_of_the_country = fields.Char(string='Name of The Country', help='describe the country name',  translate=True)
    short_code_of_the_country = fields.Char(string='Short Code of The Country', help='describe the country code')
    active = fields.Boolean(string='Active', help='the active fields is true', default=True)
    '''
	    # requirement 3. Add unique _sql_constraint on country_code field for res.country.ksc
	    #    ''' This code is for identify unique country code.If any person write duplicate country code
	    #         which is already in the database it gives an error like "Country code is already exist"..
     '''
    _sql_constraints = [
        ('short_code_of_the_country_unique', 'unique(short_code_of_the_country)', 'Country code is already exist ..!'),
    ]

