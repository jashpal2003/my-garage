from odoo import fields,models,api

class Services(models.Model):
    _name='garage.services'
    _description='Services'
    _rec_name='name'


    name = fields.Char('Name of Service')

    service_price = fields.Float("Price Of Service")
    time_consume = fields.Float('Time Consume by Service')

