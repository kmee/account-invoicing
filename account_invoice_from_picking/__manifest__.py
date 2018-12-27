# -*- coding: utf-8 -*-
# Copyright 2017 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice From Picking',
    'summary': """
        Allows to create invoice lines from picking orders""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'www.akretion.com',
    'depends': [
        'stock_account',
        'onchange_helper',
    ],
    'data': [
        'views/account_invoice.xml',
        'wizard/stock_invoice_onshipping_view.xml',
        'wizard/stock_return_picking_view.xml',
        'views/stock_view.xml',
    ],
    'demo': [
        'demo/account_invoice_from_picking_demo.xml',
    ],
    'installable': True,
}