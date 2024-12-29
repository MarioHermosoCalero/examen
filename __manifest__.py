# -*- coding: utf-8 -*-
{
    'name': 'XXXXXXXXXXYYYY',

    'summary': 'XXXXXXXXXXYYYY',

    'description': """
        XXXXXXXXXXYYYY.
    """,

    'author': 'XXXXXXX',
    'website': 'XXXXXXXXXX',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'XXXXXXXXXX',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/autoescuela_security.xml',
		'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    # indicamos que es una aplicación
}

