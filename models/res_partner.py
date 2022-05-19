##############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
##############################################################################

from odoo import _, api, fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    ref = fields.Char(required=True,
                          readonly=True, store=True, default=lambda self: _('New')
    )


    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'res.partner') or _('New')
        res = super(Partner, self).create(vals)
        return res
