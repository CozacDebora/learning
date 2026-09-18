from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    puncteLoialitate = fields.Integer(
        string = "Puncte loialitate",
        default = 0
    )

    nivelDeLoialitate = fields.Selection(
        [
            ("bronz", "Bronz"),
            ("argint", "Argint"),
            ("aur", "Aur"),
        ],
        string = "Nivel de loialitate",
        compute = "computeNivelLoialitate",
        store = True,
    )

    @api.depends("puncteLoialitate")
    def computeNivelLoialitate(self):
     for partner in self:
         if partner.puncteLoialitate < 100:
                    partner.nivelDeLoialitate = "bronz"
         elif partner.puncteLoialitate >= 100 and partner.puncteLoialitate < 200:
                    partner.nivelDeLoialitate = "argint"
         else:
                    partner.nivelDeLoialitate = "aur"