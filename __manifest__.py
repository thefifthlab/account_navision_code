{
    'name': 'Account Navision Code',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Add Navision Code column next to Code in Chart of Accounts',
    'description': """
Account Navision Code
===================
Adds a new field "Navision Code" beside the Code column
in the Chart of Accounts list view (account.account).
    """,
    'author': 'Custom',
    'depends': ['account'],
    'data': [
        'views/account_account_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
