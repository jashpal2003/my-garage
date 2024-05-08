from odoo import models,fields

class Department(models.Model):
    _name = 'garage.department'
    _description ='departments'

    name = fields.Char('Name of department')

