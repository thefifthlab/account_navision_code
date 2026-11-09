from odoo import models, fields


class AccountAccount(models.Model):
    _inherit = 'account.account'

    navision_code = fields.Char(
        string='Navision Code',
        help='Navision ERP code for this account.',
        copy=False,
        index=True,
    )
