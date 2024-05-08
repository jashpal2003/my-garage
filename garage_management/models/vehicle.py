from odoo import models,fields,api





class VehicleBrand(models.Model):
    _name = "garage.brand"
    _description = "vehicle brand"

    name = fields.Char('Brand Name')


class Vehiclemodel(models.Model):
    _name = "garage.vehicle"
    _description = "Vehicle"

    brand_id = fields.Many2one('garage.brand','Brand Name')

    name = fields.Char('Model Name')

    