# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Account Payment-Receipt',
    'version': '1.0',
    'category': 'Account-Pay',
    'summary': 'Account-Pay Report',
    'description': "",
    'website': 'https://www.odooimplementers.com',
    'depends': ['payment'],
    'data': [
        'reports/payment_template.xml',
        'reports/payment.xml',
        'views/account_inheri.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
