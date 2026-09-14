from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    titlu = fields.Char(
        string="Titlu",
        required=True
    )

    autor = fields.Char(
        string="Autor"
    )

    gen = fields.Selection(
        [
            ("fiction", "Ficțiune"),
            ("fantasy", "Fantasy"),
            ("mystery", "Mister"),
            ("romance", "Romance"),
            ("science", "Știință"),
            ("history", "Istorie"),
            ("other", "Altele"),
        ],
        string="Gen"
    )

    dataPublicarii = fields.Date(
        string="Data publicării"
    )

    numarulPaginii = fields.Integer(
        string="Număr de pagini"
    )

    disponibilitate = fields.Boolean(
        string="Disponibil",
        default=True
    )
