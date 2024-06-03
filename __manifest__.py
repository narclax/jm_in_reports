# -*- coding: utf-8 -*-
{
    'name': "Implementación Reportes IN V16",

    'summary': """
        Implementación Reportes IN V16""",

    'description': """
        FImplementación Reportes IN V16
    """,

    'author': "Jose Marty",
    'website': "https://www.gsuiterd.com",
    'email' : "jose.m.marty@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Formatos - Qweb - XML',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

    # always loaded
    'data': [
        'reports/template_view.xml',
        'reports/scale_cal.xml',
        #'reports/quotation_report.xml',
        'reports/view_report.xml'
    ],
    'application': True,
    'installable':True,
}
