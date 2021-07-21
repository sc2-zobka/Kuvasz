# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TimeSheetInherited(models.Model):
    _inherit = "account.analytic.line"

    @api.onchange("date")
    def _check_days(self):
        """DatePicker validation
        Raises:
            ValidationError:
                When selecting a date past today or
                "n" days before current date.
        Type:
            fields.Date(): <class 'datetime.date'>
        """

        # fetch model "ir.config_parameter" data
        data = self.env["ir.config_parameter"].sudo()

        # retrieve the value for "days_before_today" key
        days = int(data.get_param("days_before_today"))

        today = fields.Date.today()
        delta = today - self.date

        if self.date:
            if self.date > today:
                raise ValidationError(_("Fecha no puede ser mayor a %s") % today)

            elif delta.days > days:
                raise ValidationError(_("Fecha no permitida"))
