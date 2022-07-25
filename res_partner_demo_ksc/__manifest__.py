# -*- coding: utf-8 -*-
{
    'name': "res_partner_demo_ksc",
    'summary': "The data of Customers",
    'description': """This models is all about understand the active attributes """,
    'author': "konsultoo",
    'website': "http://www.konsultoo.com",
    'category': 'Uncategorized',
    'version': '1.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_demo.xml',
        'data/res_partner_demo_ksc.xml',
    ],
    'demo': [
        'data/res_partner_demo_ksc.xml',
    ],
    'application': True,
    'installable': True,
    'auto-install': False,
    'license': 'LGPL-3',
}
