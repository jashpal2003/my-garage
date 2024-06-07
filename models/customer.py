from odoo import models, fields, api, Command,_
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _name = 'garage.customer'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'customer'
    _order = 'sequence'

    # 19.Add an SQL constraint to add a unique constraint on a single field.
    # 20. Add an SQL constraint to add a unique constraint on a combination of two fields.
    # 21. Add an SQL constraint to add a check constraint to check the value of a field.
    # #
    # _sql_constraints = [
    #     # ('check_age', 'check(age>=5)', 'bacha gadi ke sath paida hua tha kya '),
    #     ('unique_phone', 'unique (phone,email)','The phone number and email should be different')
    #     # ('unique_phone', 'unique (phone)','The phone number should be different')
    # ]
# this is used add sql constraint in sql table

#inherits = {'<model_name>'}

    name =  fields.Char(string = 'name' , required=True)
    name_title = fields.Selection(selection=[('Mr.','Mr.',),
                                  ('Ms','Ms')],string='Name Title',help='This field is used to identify the title for your name')
    reg_no = fields.Char(string ='Register no' , copy = False,radonly = True,default = lambda self:_('New'))
    age = fields.Integer('Age',group_operator = 'avg',required=True)
    active = fields.Boolean('Active' , help = 'this field is used to activate or deactivate the record ',default = True,)
    notes = fields.Text('Notes')
    template = fields.Html('Template')
    birthdate = fields.Date('Birthdate')
    gender = fields.Selection(selection = [('male','Male'),
                                            ('female','Female')],string = 'Gender',required=True)
    customer_code = fields.Char('Customer Code')
    password = fields.Char('Password')
    email = fields.Char('Email',required=True)
    url = fields.Char('URL')
    phone = fields.Char('Phone',required=True)
    preferred_contact = fields.Selection([('phone', 'Phone'), ('email', 'Email')], 'Preferred Contact Method')

    sign_in = fields.Float('Sign in')
    priority = fields.Selection([(str(ele) , str(ele) )for ele in range(6)],'Priority')

    #vehicle_id = fields.Many2one('garage.vehicle','Vehicle',ondelete = 'restrict',domain = [('name','like','%it%')])
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
                              ('digonised','Diagnose'),
                              ('repairing','Repairing'),
                              ('payment','Payment'),
                              ('deliver','Deliver'),
                              ('left','Left')], 'State', default='applied')

    # company_name= fields.Many2one('')
    # model_name = fields.Many2one('')
    #vehicle_type = Many2one('')
    description_of_problem = fields.Text('Problem Description')
#     service_u_need = fields.Many2many('')

    """In the many2one field only the records which are having ‘it’ as a substring in their
name should be allowed to select."""

    # company_id =fields.Many2one('garage.brand','vehivle brand',domain="[('company_id','like','it')]")
    # company_id = fields.Many2one('garage.brand', string='Company',domain="[('name','like','it')]")
    company_id = fields.Many2one('garage.brand', string='Company')
#     If a record is selected in a many2one field, it should not be possible to delete the
# record from the model of many2one


    # company_id = fields.Many2one('garage.brand', string='Company', ondelete='restrict')
    # # company_id = fields.Many2one('garage.brand', string='Company'domain="[('name','=like','%ts')]")
    vehicle_model_id = fields.Many2one('garage.vehicle','vehivle model',domain="[('brand_id','=',company_id)]")
    # cars = fields.One2many('garage.car','garage_id',string = "car")



    maintenance_ids = fields.One2many('garage.maintenance', 'car_id', string='Maintenance Records',limit = 2)






    color = fields.Char(string= "Color of vehicle")
    model_year = fields.Char(string = "Model Year")
    vehicle_type = fields.Selection(selection = [('2 wheeler','2 wheeler'),
                                            ('3 wheeler','3 wheeler'),('4 wheeler','4 wheeler'),],string = 'Vehicle Type')





    Fuel_type = fields.Selection(selection = [('electric','electric'),
                                            ('petrol','petrol'),('diesel','Diesel'),('CNG','CNG')],string = 'Fuel Type')


    horse_power = fields.Integer(string = "Horse Power")
    mileage = fields.Integer(string = "Mileage")





#     5. Create a functionality such that whenever I delete a main record all the records in
# its one2many should be deleted.


    # maintenance_ids = fields.One2many('garage.maintenance', 'car_id', string='Maintenance Records',ondelete='cascade',)
    def print_student(self):
        print("***************************************************************************************************************Lang",self.env.lang)

        print("COMPANY",self.env.company)
        print("USER", self.env.user)

        print("CONTEXT",self.env.context)

        form_view_stud = self.env.ref('garage_management.view_customer_form')
        print("FORM VIEW STUD",form_view_stud)

        # vehicle_obj = self.env['garage.vehicle']
        # print("STD OBJ",vehicle_obj)
        #
        # Get the value of all predefined fields for a recordset containing one or more
        # records without using the ORM methods.



#
        for customer in self:
            mt_dt = customer.get_metadata()
            print("MT DT", mt_dt)

#             # Filter the existing recordset with a condition. The condition should contain a field
# # and a value.
        cust_record = self.env['garage.customer'].search([])

#
        male_rec = cust_record.filtered(lambda r:r.gender=='male')

        print("filter male")
        print(male_rec)
        print('mapped ---',male_rec.mapped('name'))
#
        merge_name_age = cust_record.mapped(lambda x: f"{x.name}-{x.age}")
        print(merge_name_age)


#         From a recordset get a list of values in a specific field.
        record_list = cust_record.mapped('name')
        print(record_list)


#  Sort a recordset in a descending order with a field other than name. The action
# should be performed on a recordset only


        sort_by_age = cust_record.sorted(key='age',reverse = True)
        print("SORT BY AGE", sort_by_age)
        for x in sort_by_age:
            print(x.name,x.age)

            """Get three different recordset where first one will have all the records of a model,
        the second one will have few records of the model and third one will also have
        few records of that model. The condition of the later two recordset should not be
        same. Now check whether the later recordset are subset or superset of each other
        or not. Also check whether the first recordset is a superset or subset or not."""

        gender_record = cust_record.filtered('gender')
        female_rec = cust_record.filtered(lambda r:r.gender=='female')

        print('Male recod',male_rec)
        print('Female record',female_rec)

        print('subset check is female subset of male',female_rec < male_rec)
        print('subset check is female supersetset of male', female_rec > male_rec)
        print('subset check is gender is subset of male',gender_record < male_rec)
        print('subset check is gender supersetset of male', gender_record> male_rec)




#         Get the union, intersection and difference of two recordsets.
        print("Union check",male_rec | female_rec)
        print("Intersection Record",male_rec & gender_record)
        print("Diff Record",gender_record - male_rec)

    # Add a button on the form view on the page of a one2many field. When you click
    # this button it will add a record in the one2many field.
    def create_record(self):
        rec1={
            'name':'anjna1234567899999',
            'active':True,
            'age':23,
            'birthdate':'2003-04-23',
            'gender':'male',
            'description_of_problem':'repaire indicator',


        }
        rec2={
            'name':'anjna1234567899999',
            'active':True,
            'age':23,
            'birthdate':'2003-04-23',
            'gender':'male',
            'description_of_problem':'repaire engine',
            'maintenance_ids':[
                (0,0,{
                    'date':'2003-04-25',
                    'description':'change side light',
                    'cost':300.0,
                }),
                (0,0,{
                    'date':'2003-03-25',
                    'description':'change tyre',
                    'cost':300.0,
                })
            ],


        }
        rec_list =[rec1,rec2]
        new_record = self.create(rec_list)
        print("new record created is",new_record)



    #  Add a button on the form view. When you click this button it should update a
    # field’s value of the current record.
    def update_record(self):
        recup = {
            'name':'Updated name',
        }
        res = self.write(recup)
        print("res",res)





# 29. Add another button on the page of one2many field when you click on this button
# it will remove one record but it will not remove it from the database.
    def partial_remove(self):
        partial_remove_rec = {
            'maintenance_ids': [
                (3,11,False)]}
        res1 = self.write(partial_remove_rec)
        print(" partial remove  ",res1)

    def partial_remove2(self):
        partial_remove_rec = {
            'maintenance_ids': [
                (5,27,0)]}
        res1 = self.write(partial_remove_rec)
        print(" partial remove  ",res1)

    @api.model_create_multi
    def sequence_add(self,vals):
        if vals.get('reg_no',_('New')) == _('New'):
            vals['reg_no'] =self.env['ir.sequence'].next_by_code('garage.customer.sequence') or _('New')
        if vals.get('name'):
            vals['customer_code'] = vals['name'][:3].upper()

        result = super().create(vals)
        return result
    def search_record(self):
        all_records = self.search([])

        print('ALL student',all_records)
        no_of_record = self.search([],count = True)
        # Add a smart button which displays the count of records from another model
# related to your current record. When you click on this button it will show you the
# same no of records in a list view.

        print("no of record display",no_of_record)
        sort_skip_rec = self.search([('gender','=','male')],offset = 5,limit = 15,order = 'name')
        print('sort - skip - offset record',sort_skip_rec)
        no_of_female_students = self.search_count([('gender', '=', 'female')])
        print("FEMALE STUDENTS", no_of_female_students)

    def browse_record(self):
        customer_record =self.browse(1)
        cust_dict_record = customer_record.read(['name','age','description_of_problem'],load ='')
        print(cust_dict_record)


    #
    #
    # @api.model
    # def create(self,vals):
    #
    #     if vals.get('reg_no',_('New')) == _('New'):
    #         vals['reg_no'] =self.env['ir.sequence'].next_by_code('garage.customer.sequence') or _('New')
    #     if vals.get('name'):
    #         vals['customer_code'] = vals['name'][:3].upper()


        #
        # result = super().create(vals)
        # return result
    # 4. Override write() method to update the records.

    def add_seq(self):
        seq =self.env['ir.sequence']
        self.reg_no=seq.next_by_code('garage.customer.sequence')


    def write(self,vals):
        if vals.get('name'):
            vals['customer_code'] = vals['name'][:7].upper()

        return super().write(vals)

    @api.model
    def search(self,args,offset = 0,limit = None,order =None,count=False):
        args =['|',('active','=',False),('active','=','True')] +args

        return super().search(args,offset = 0,limit = limit,order = order,count=count)

    def unlink(self):
        if self.state != 'applied':
            raise ValidationError(("Paise de aur gadi le ja"))

        return super(Customer,self).unlink()
    # Override copy() method to remove one of the existing fields and add another
    # value.
    # Override copy() method and have the state field not copied and bring back to the
    # fiirst state in the selection.
    def copy(self,default = None):
        default ={
            'name':self.name+'- Copy',
            'customer_code':'copy',
            'state':'applied',
            'email':'etyytr',
            'phone':'987678865445',

        }

        return super().copy(default=default)

    @api.model
    def default_get(self,field_list):
        print("field list ",field_list)
        res = super().default_get(fields_list=field_list)
        print(res)
        res.update({'email':'i am jashpal'})
        print("update res ",res)
        return res

    @api.onchange('gender','description_of_problem')
    def onchange_gender(self):
        for customer in self:
            code = ''
            if customer.description_of_problem == '':
                raise ValidationError('d,kanejgnsjbhj do ')
            elif customer.gender == 'female':
                code = 'FF'
            elif customer.gender == 'male':
                code = 'MM'
            customer.customer_code = code


    @api.constrains('age','gender')
    def check_customer_age(self):
        for customer in self:
            if customer.gender =='male' and customer.age<12:
                raise ValidationError('i know male better rider than girl but bhai bachhe ko bada to hone do ')
            if customer.gender =='female' and customer.age <30:
                raise ValidationError('i know the right age for woman is 20 but as per survey they became papa ki pari thats why we make age for female is 30 + ')




    #22. Add an object constraint to make sure that the length of a character field is
# exactly 4 characters.
    @api.constrains('customer_code')
    def check_customer_code(self):
        for customer in self:
            r = customer.customer_code
            if len(r) != 4:
                raise ValidationError(' kya re gunda banega tu hamara  code 4 digit ka  hai')
            print(r)

    # 1. Override create method to create a record in another model.
    # @api.model
    # def create(self, vals):
    #     record = super(Customer, self).create(vals)
    #     if record.description_of_problem:
    #         self.env['garage.maintenance'].create({
    #             'description':record.description_of_problem,
    #               'date':fields.Date.today(),
    #             'cost':98765432123456789,
    #             'car_id':record.id,
    #
    #         })
    #         print(record)
    #     return record
    # @api.model
    # def create(self,vals):
    #     record = super(Customer, self).create(vals)
    #     if vals.get('name_title') =='Mr':
    #         record['gender'] = 'male'
    #     if vals.get('name_title') =='Ms':
    #         record['gender'] = 'female'
    #
    #     self.env['garage.customer'].create({record['gender']})
    #
    #     return record




    # 9. Override name_get method and display two fields rather than just name in the
    # many2one field.
    def name_get(self):
        cust_list = []
        for cust in self:
            cust_name = ''
            if cust.customer_code:
                cust_name+='['+ cust.customer_code +']'
            cust_name+=cust.name
            cust_list.append((cust.id,cust_name))

        return cust_list

    # 10.Override name_search method to search with both the fields which are displayed
    # in many2one field
    # in many2one field
    @api.model
    def name_search(self,name = '', args = None,operator ='ilike',limit = 100):

        print("NAME", name)
        print("ARGS", args)
        print("OP", operator)
        print("LIMIT", limit)
        if not args:
            args = []

            args += ['|', ('name',operator, name),('customer_code', operator, name)]
            customer_name =self.search(args)

            return customer_name.name_get()


    @api.model
    def name_craete(self,name):
        vals ={
            'name':name,
            'customer_code':'abcd'
        }
        cust_name_code =self.craete(vals)
        print("------------------------",cust_name_code)

        return  cust_name_code.name_get()[0]



class MaintenanceRecord(models.Model):
    _name = 'garage.maintenance'
    _description = 'Maintenance Record'

    date = fields.Date(string='Date')
    description = fields.Text(string='Description')
    cost = fields.Float(string='Cost')
    car_id = fields.Many2one('garage.customer', string='Car')













