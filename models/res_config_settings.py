# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    bypass_update_of_mrp_raw_material = fields.Boolean('Prevent auto updating of raw material qty done',
                                                     related='company_id.bypass_update_of_mrp_raw_material',
                                                     readonly=False)