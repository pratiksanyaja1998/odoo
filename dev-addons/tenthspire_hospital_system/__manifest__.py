# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TenthSpire Hospital System',
    'description': 'TenthSpire hospital system',
    'website': 'https://www.tenthspire.com',
    'author': 'TethSpire Technology',
    'depends': [
        'base_setup',
        'mail',
        'web',
    ],
    'data': [
        'views/auth_signup_login_templates.xml',
    ],
}
