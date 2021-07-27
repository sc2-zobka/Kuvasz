# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import float_is_zero
from odoo.exceptions import ValidationError


class TimeSheetInherited(models.Model):
    _inherit = "account.analytic.line"
    
    unit_amount = fields.Float(default=1) 

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

        # today's date with user context 
        today_ctx = fields.Date.context_today(self)
    
        delta = today_ctx - self.date
        
        if self.date:
            if self.date > today_ctx:
                raise ValidationError(_("Fecha no puede ser mayor a %s") % today_ctx)

            if delta.days > days:
                raise ValidationError(_("Fecha no permitida"))

    @api.onchange("unit_amount")
    def _check_unit_amount(self):
        """ check for unit_amount field with zero or negative hours"""

        if float_is_zero(self.unit_amount, precision_digits=3) is True:
            raise ValidationError (_("Horas ingresadas no pueden ser cero"))
        elif self.unit_amount < 0:
            raise ValidationError(_("Horas ingresadas no pueden ser negativas"))
