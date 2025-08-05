# -*- coding: utf-8 -*-
{
    "name": "Navaratri Event",
    "version": "1.0",
    "author": "Parikshit Vaghasiya",
    "category": "Other",
    "summary": "navratri sell tickets online",
    'description': "Custom module for selling event tickets online and website",
    'maintainer': "Parikshit Vaghasiya",
    'website': 'parikshitvaghasiya@blogspot.in',
    "depends": ['base', 'event','website'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [

        ],
    },
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            # 'uk_joshi/static/src/js/main.js',
            # 'uk_joshi/static/src/js/**/*.js',
            'uk_joshi/static/src/css/style.css',
        ],
        'web.report_assets_common': [
            '/uk_joshi/static/src/scss/event_full_page_ticket_report.scss',
        ],
    },
}
