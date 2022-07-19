{

    'name': "Product_ksc",
    'summary': "The data of product",
    'description': """
	""",
    'author': "Your name",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base', 'mail', 'web'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_ksc.xml',
        # 'wizard/book_rent_wizard_view.xml',
        # 	# 'security/groups.xml',
        'security/ir.model.access.csv',
        # 	# 'views/res_partner_views.xml',

    ],
    'demo': [
        # 'data/library_book_demo.xml',
    ],

    'application': True,
    'installable': True,

}

