# -*- coding: utf-8 -*-
{
    'name': "KVZ timesheet date",

    'summary': """Odoo 14 TimeSheet module extension to restrict adding timesheet lines
                to any project's task.""",

    'author': "KVZ",
    
    'category': 'Timesheets',
    'version': '0.2',

    'depends': [
        'base',
        'timesheet_grid'
    ],

    'data': [
        # 'security/groups.xml',
        # 'security/ir.model.access.csv',
        'views/timesheet_line.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
