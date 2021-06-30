# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payment Smart Icon - Hide',
    'version': '14.0.1.0',
    'author': 'Oodu Implementers Private Limited',
    'website': 'https://www.odooimplementers.com',
    'category': 'POS',
    'summary': 'Smart Icon in POS Session is hidden',
    'description': """Smart Icon in POS Session is hidden""",
    'depends': ['base', 'stock', 'point_of_sale'],
    'data': [
    'views/pos_session_view.xml'
    ],
    'installable': True,
    'auto_install': False
}
