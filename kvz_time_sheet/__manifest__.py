# -*- coding: utf-8 -*-
{
    "name": "Kuvasz Timesheet Extension",
    "summary": """Odoo 14 TimeSheet module extension to restrict adding timesheet lines
                to any project's task.""",
    "author": "Kuvasz Solutions",
    "website": "https://www.kvz.cl",
    "category": "Timesheets",
    "version": "1.0",
    "depends": [
        "base",
        "timesheet_grid",
    ],
    "data": [
        "views/timesheet_line_view.xml",
        "views/res_config_settings_view.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
}
