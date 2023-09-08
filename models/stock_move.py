# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, OrderedSet

import logging

_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = "stock.move"

    def _should_bypass_set_qty_producing(self):
        if self.company_id.bypass_update_of_mrp_raw_material and self.state in (
        'confirmed', 'partially_available', 'assigned', 'done', 'cancel') and self._related_operation_is_terminated():
            return True
        return super(StockMove, self)._should_bypass_set_qty_producing()

    def _related_operation_is_terminated(self):
        self.ensure_one()
        related_bom = self.raw_material_production_id and self.raw_material_production_id.bom_id
        if not related_bom:
            return False
        related_bom_lines = related_bom.bom_line_ids.filtered(lambda bl:bl.product_id.id == self.product_id.id)
        if not related_bom_lines:
            return False
        related_workorder = self.raw_material_production_id.workorder_ids.filtered(lambda wo:wo.operation_id.id == related_bom_lines[0].operation_id.id)
        if not related_workorder:
            return False
        if related_workorder[0].state in ('cancel','done'):
            return True
        else:
            return False


