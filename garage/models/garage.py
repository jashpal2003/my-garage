from odoo import models, fields
from datetime import datetime

class Garage(models.Model):
    _name = 'garage.customer'
    _description = 'customer'


    name = fields.Char(string='Customer name',help='in this feild enter your name '   )

    vehicle_number = fields.Integer('Vehicle number',help='This field for vehicle number ')

    vehicle_age = fields.Float('Vehivle age', required = True,help='This field is used for identify vehicle age',digits=(16,3))

    vehicle_service_done = fields.Boolean('Service Done',help='This field is used to check is service done or not  ')
    vehicle_model = fields.Text('Vehicle Model',required = True)
    vehicle_service_entry_date = fields.Date("Vehicle Entry",index=True,default=datetime.today(),help='This field is used to find when the vehicle enter in the garage  ')
    vehicle_service_exit_time = fields.Datetime("Vehicle Exit",help='This field is used to find when vehicle exit from garage')
    name_title = fields.Selection(selection=[('Mr.','Mr.',),
                                  ('Ms','Ms')],string='Name Title',help='This field is used to identify the title for your name')
    service_code = fields.Char('Service Code', size=4)
    notes = fields.Text('Notes')
    template = fields.Html('Template')
    active = fields.Boolean('active',default = True)
    password = fields.Char('Password')
    email = fields.Char('Email')
    website = fields.Char('Website')
    priority = fields.Selection([(str(ele), str(ele)) for ele in range(5)], 'Review')
    sign_in_idk = fields.Float('Time vehicle stay')
    vehicle_type = fields.Selection(selection=[('activa','Activa'),
                                               ('bike','Bike'),
                                               ('car','Car'),
                                               ('auto','Auto'),
                                               ('ev','E.V.')],string = "Type Of Vehicle",default = "bike")