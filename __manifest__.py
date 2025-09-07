{
    'name': "furniture_orders",
    'version': '1.0',
    'depends': ['base', 'web'],
    'author': "Herzok",
    'category': 'Operations',
    'description': "test desc",
    'installable': True,
    'application': True,
    'data': [
        'security/groups.xml',
        'security/models.xml',
        'security/ir.model.access.csv',
        'views/furniture_orders_views.xml',
        'views/furniture_devices_views.xml',
    ],
    'assets': {
        'web._assets_backend': [
            'furniture_orders/static/src/css/kanban.css',
        ],
    },
}