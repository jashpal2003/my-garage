from odoo import fields,models,api


class Employees(models.Model):
    _name = 'garage.employee'
    _description = 'employees'

    # _rec_name = 'name'


    name = fields.Char('Name')

    department_name = fields.Many2one('garage.department','select department')


