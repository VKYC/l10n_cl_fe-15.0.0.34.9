from odoo import fields, models


class paymentTerm(models.Model):
    _inherit = "account.payment.term"

    dte_sii_code = fields.Selection([("1", "1: Contado"), ("2", "2: Credito"), ("3", "3: Otro")], "Forma de pago SII",)
