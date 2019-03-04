# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Module WebSite',
    'summary': 'Child Module - Parent website',
    'version': '1.2',
    'depends': ['website'],
    'author' : 'SIKI SAS, Developer Ing Henry Vivas',
	'website' : 'www.sikisoftware.com',
    "support": "controlwebmanager@gmail.com",
    'category': 'Website',
    'description': """
This module modifies the main WebSite module in the platform.
========================================================================

List of modifications:
-------------------
    * V.-1.0 Field Social Add boton shared Instagram ( Req. 1059 )
    * V.-1.1 Delete Field Social Google Plus and GitHub
    * V.-1.2 Add Field Social Pinterest and Contact Whatsapp
    * ...:
        * ...
        * ...
 """,
    'data': [
        'views/res_config.xml',
        'views/website_views.xml',
        'views/website_templates.xml',
        'data/data.xml',
    ],
    'installable': True,
    'application': False,
}