# -*- coding: utf-8 -*-
{
    'name': "employee_mgmt_ksc",
    'summary': "The data of employee management",
    'description': """This models is all about understand the active attributes""",
    'author': "konsultoo",
    'website': "http://www.konsultoo.com",
    'category': 'Uncategorized',
    'version': '2.2',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_department_ksc.xml',
        'views/employee_department_shift_ksc.xml',
        'views/employee_ksc.xml',
        'views/employee_leave_ksc.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto-install': False,
    'license': 'LGPL-3',
}
