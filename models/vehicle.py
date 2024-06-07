from odoo import models,fields,api


#
# class car(models.Model):
#     _name = "garage.car"
#     _description = "car"
#
#     name = fields.Char("name")
#     brand = fields.Char("brand name")
#     milage = fields.Float("milage ")
#     garage_id=fields.Many2one('garage.customer','customer')
#








class VehicleBrand(models.Model):
    _name = "garage.brand"
    _description = "vehicle brand"

    name = fields.Char('Brand Name')
    logo = fields.Image('Logo')


class Vehiclemodel(models.Model):
    _name = "garage.vehicle"
    _description = "Vehicle"

    brand_id = fields.Many2one('garage.brand','Brand Name')

    name = fields.Char('Model Name')


# class Maintenance(models.Model):
#     _name = 'garage.maintenance'
#     _description = 'Vehicle Maintenance Record'
#
#     vehicle_id = fields.Many2one('garage.customer', string='Vehicle', required=True)
#     date = fields.Date(string='Date', required=True)
#     description = fields.Text(string='Description', required=True)
#     cost = fields.Float(string='Cost', required=True)
#
#