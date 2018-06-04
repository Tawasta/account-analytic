# -*- coding: utf-8 -*-
from odoo import api, models


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    @api.onchange('product_id')
    def onchange_product_id_update_analytic_tags_from_template_tags(self):
        for record in self:
            if record.product_id and record.product_id.tag_ids:
                record.analytic_tag_ids += \
                    record.product_id.tag_ids.analytic_tag_ids
