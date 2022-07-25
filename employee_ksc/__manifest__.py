# -*- coding: utf-8 -*-
{
    'name': "Employee Ksc",
    'summary': "The data of employee",
    'description': """This models is all about understand the active attributes """,
    'author': "konsultoo",
    'website': "http://www.konsultoo.com",
    'category': 'Employees',
    'version': '1.6',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_ksc.xml',
    ],
    'application': True,
    'installable': True,
    'auto-install': False,
    'license': 'LGPL-3',
}
