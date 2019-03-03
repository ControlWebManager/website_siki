# -*- coding: utf-8 -*-

import openerp
from openerp import api, tools, SUPERUSER_ID

from openerp import models, api, fields

class website_config_settings_extend(models.Model):
    _inherit = ['website.config.settings']
    _description = "Website Config Extend SIKI"

    social_instagram = fields.Char(related='website_id.social_instagram', string='Cuenta Instagram')
    social_pinterest = fields.Char(related='website_id.social_pinterest', string='Cuenta Pinterest')
    social_whatsapp = fields.Char(related='website_id.social_whatsapp', string='Cuenta Whatsapp')