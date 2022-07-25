# -*- coding: utf-8 -*-
{
    'name': "Res_localization_ksc",
    'summary': "The data of Res localization Ksc",
    'description': """This models is all about understand the active attributes """,
    'author': "konsultoo",
    'website': "http://www.konsultoo.com",
    'category': 'Uncategorized',
    'version': '2.1',
    'depends': ['base', 'res_country_ksc', 'res_state_ksc', 'res_city_ksc'],
    'data': [
        'views/res_country_ksc_views.xml',
        'views/res_state_ksc_views.xml',
        'views/res_city_ksc_views.xml',
        'report/country_report.xml',
        'report/country_report_templates.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto-install': False,
    'license': 'LGPL-3',
}
