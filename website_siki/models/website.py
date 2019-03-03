# -*- coding: utf-8 -*-

import openerp

from openerp import models, api, fields

class website_extend(models.Model):

    _inherit = "website" # Avoid website.website convention for conciseness (for new api). Got a special authorization from xmo and rco
    _description = "Website Extend SIKI"

    social_instagram = fields.Char('Cuenta Instagram')
    social_pinterest = fields.Char('Cuenta Pinterest')
    social_whatsapp = fields.Char('Cuenta Whatsapp')

    @api.model
    def _new_data_social_siki(self):

        for record in self.search([]):
            record.write({
                'social_twitter': 'https://twitter.com/',
                'social_facebook': 'https://www.facebook.com/Sikisoftware/',
                'social_linkedin': 'https://es.linkedin.com/company/siki-s-a-s',
                'social_youtube': 'https://www.youtube.com/channel/UCG19tL1bb-ipKtTU4WNIZtA',
                'social_googleplus': 'https://plus.google.com/u/1/b/113919160666820523652/113919160666820523652',
                'social_instagram': 'https://www.instagram.com/sikisoftwareadministrativo/',
                'social_pinterest': 'https://www.pinterest.es/sikisoftware/'})

        return True