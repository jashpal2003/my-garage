from odoo import fields,models,api

class Billing(models.Model):
    _name="garage.billing"
    _description = "billing"

    cname = fields.Char('Name of Customer')
    vehicle = fields.Char('name of vehicle')
    service = fields.Char('Name of Service')
    parts = fields.Char('Name of parts')
    amount_pay = fields.Integer('Amount to be payed')