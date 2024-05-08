from odoo import models,fields


class Customer(models.Model):
    _name = 'garage.customer'
    _description = 'customer'
    _order = 'sequence'
#rec_name = '<recognition_field>

#sql_constraint = []   this is used add sql constraint in sql table

#inherits = {'<model_name>'}

    name =  fields.Char(string = 'name', required = True )
    name_title = fields.Selection(selection=[('Mr.','Mr.',),
                                  ('Ms','Ms')],string='Name Title',help='This field is used to identify the title for your name')
    age = fields.Integer('Age', default = 18, group_operator = 'avg')
    active = fields.Boolean('Active' , help = 'this field is used to activate or deactivate the record ',default = True,)
    notes = fields.Text('Notes')
    template = fields.Html('Template')
    birthdate = fields.Date('Birthdate')
    gender = fields.Selection(selection = [('male','Male'),
                                            ('female','Female')],string = 'Gender')
    customer_code = fields.Char('Customer Code' , size = 4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    url = fields.Char('URL')
    phone = fields.Char('Phone')


    sign_in = fields.Float('Sign in')
    priority = fields.Selection([(str(ele) , str(ele) )for ele in range(6)],'Priority')


    #vehicle_id = fields.Many2one('garage.vehicle','Vehicle',ondelete = 'restrict',domain = [('name','=','sp125')])
   # service_id = fields.Many2Many('garage.service','','','Services')

    # ref = fields.Reference([('garage.customer','customer'),
    #                         ('res.users','Users'),
    #                         ('res.partner','Contacts')],'Reference')


    document = fields.Binary('Document')
    file_name = fields.Char('File name')
    sequence =  fields.Integer('Sequence')
    photo = fields.Image('Photo')

    howufind = fields.Selection([('social_media', 'Socical Media'),
                              ('advertisement', 'advertisement'),
                              ('friends_refer', 'Friend Reference'),
                              ('other', 'Other'),])

    state = fields.Selection([('applied','Applied'),
                              ('interviewed','Interviewed'),
                              ('selected','Selected'),
                              ('rejected','Rejected'),
                              ('joined','Joined'),
                              ('left','Left')], 'State', default='applied')

    # company_name= fields.Many2one('')
    # model_name = fields.Many2one('')
    #vehicle_type = Many2one('')
    description_of_problem = fields.Text('Problem Description')
#     service_u_need = fields.Many2many('')

    # company_id =fields.Many2one('garage.brand','vehivle brand',domain="[('company_id','=',company_id)]")
    company_id = fields.Many2one('garage.brand', string='Company')
    vehicle_model_id = fields.Many2one('garage.vehicle','vehivle model',domain="[('brand_id','=',company_id)]")
