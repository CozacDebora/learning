from odoo import fields, models


class LearnTicket(models.Model):
    _name = "learn.ticket"
    _description = "Sesizare"

    name = fields.Char(string="Titlu", required=True)
    is_resolved = fields.Boolean(string="Rezolvat")
    problem = fields.Text(string="Problema")
