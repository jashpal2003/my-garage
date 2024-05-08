from odoo import fields,models,api

class Parts(models.Model):
    _name = "garage.parts"
    _description ="parts"

    name = fields.Char('Name of Parts')
    price = fields.Float('Price Of Parts')
