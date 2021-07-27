# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettingInherited(models.TransientModel):
    _inherit = "res.config.settings"

    days_before_today = fields.Integer(
        string="Restricted days",
        help="Set number of days before today to restrict adding timesheet lines on a task",
        config_parameter="days_before_today",
    )

    def set_values(self):
        super(ResConfigSettingInherited, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "kvz_time_sheet.days_before_today", self.days_before_today
        )

    def get_values(self):
        res = super(ResConfigSettingInherited, self).get_values()
        days_before_today = self.env["ir.config_parameter"].get_param(
            "kvz_time_sheet.days_before_today"
        )
        res.update(
            {
                "days_before_today": days_before_today,
            }
        )
        return res

    @api.constrains("days_before_today")
    def _check_days_before_today(self):

        if self.days_before_today < 0:
            raise ValidationError(
                _("Amount of days must be greater than 0, not %s")
                % self.days_before_today
            )
