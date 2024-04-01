{
    'name': 'Garage Management',
    'description': 'This module is used to manage garage Information',
    'author': 'Jashpal',
    'website': 'https://www.jashpal.com',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/garage_security.xml',
        'security/ir.model.access.csv',
        'views/garage_view.xml',
    ],
    'auto_install': True,
    'installable':True,
    'application': True,
}