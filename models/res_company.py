# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'

    bypass_update_of_mrp_raw_material = fields.Boolean('Prevent auto updating of raw material qty done')

