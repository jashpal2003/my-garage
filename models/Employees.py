from odoo import fields,models,api


class Employees(models.Model):
    _name = 'garage.employee'
    _description = 'employees'

    # _rec_name = 'name'


    name = fields.Char('Name')

    department_name = fields.Many2one('garage.department','select department')
    parent_id = fields.Many2one('garage.employee','head of department')
    child_id = fields.One2many('garage.employee','parent_id','employee')


