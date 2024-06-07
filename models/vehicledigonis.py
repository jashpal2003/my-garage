from odoo import fields,models,api

class VehicleDigonis(models.Model):
    _name = 'garage.vehicledigonis'
    _description = 'vehicledigonis'

    name = fields.Many2one('garage.customer','customer name')
    vehicle_problem = fields.Text(related="name.description_of_problem",string='Vehicle problem')
    # vehicle = fields.One2many(related="name.cars", string='vehicle')
    vehicle_brand = fields.Many2one(related="name.company_id", string="vehicle brand name")
    vehicle_model = fields.Many2one(related="name.vehicle_model_id", string='vehicle brand name')

#     Create another model and add a many2many field for this model in the existing
# model but give the table user defined name. Also give user defined name for the
# columns in this table



    # service_needed = fields.Many2many('garage.services','vehicle_service_rel','vehicle_id','service_id',"services",store=True)



    service_needed = fields.Many2many('garage.services',"services",store=True)
    # In the many2many field only the records which are ending with ‘ts’ substring
# should be allowed to select.

    # service_needed = fields.Many2many('garage.services',"services",domain="[('name','=like','%ts')]")
    parts_needed_id= fields.One2many('customer.parts',"vehicle_d_id")
    parts_price = fields.Float(compute="_comput_price_depend",string='price for parts')
    service_price = fields.Float(compute="_comput_price_depend",string='price for service')
    total_amount = fields.Float(compute = "_comput_price_depend",string = 'total amount to pay:=')


    additional_box = fields.Boolean('Additional summary')
    summary_text = fields.Text('Summary')










    @api.depends('parts_needed_id','service_needed')
    def _comput_price_depend(self):
        total_parts_price = 0.0
        total_service_price = 0.0


        for priced in self:
            for pr in priced.parts_needed_id:
                total_parts_price += pr.price
                print(total_parts_price)
            priced.parts_price = total_parts_price
            for sr in priced.service_needed:
                total_service_price += sr.service_price
                print(total_service_price)
            priced.service_price = total_service_price

            priced.total_amount = total_service_price + total_parts_price




                #

                #
                #
                # class AddSubscription(models.Model):
                #     _name = 'subscription.addsubscription'
                #     _description = 'Add Subscription'
                #
                #     type_id = fields.Many2one('subscription.type', 'Subscription', required=True)
                #     plan_id = fields.Many2one('subscription.plan', 'Plan', required=True)
                #     price_depend = fields.Float(compute='_compute_price_depend', string='Price')
                #     start_date = fields.Date(string='Start Date', default=fields.Date.today())
                #     expire_date = fields.Date(string='Expire Date')
                #     user_id = fields.Many2one('subscription.user', 'User', ondelete='cascade')
                #
                #     @api.depends('type_id', 'plan_id')
                #     def _compute_price_depend(self):
                #         for user in self:
                #             if user.type_id and user.plan_id:
                #                 plan_code = user.plan_id.code.lower()
                #                 if plan_code == 'monthly':
                #                     user.price_depend = user.type_id.monthly_price
                #                 elif plan_code == 'daily':
                #                     user.price_depend = user.type_id.daily_price
                #                 elif plan_code == 'weekly':
                #                     user.price_depend = user.type_id.weekly_price
                #                 elif plan_code == 'yearly':
                #                     user.price_depend = user.type_id.yearly_price
                #
                #                 else:
                #                     user.total_price = total
                #                     user.price_depend = 0.0
                #             else:
                #                 user.price_depend = 0.0

                #  user.expire_date = user.start_date + timedelta(days=30)
                # user.expire_date = user.start_date + timedelta(days=7)
                # user.expire_date = user.start_date + timedelta(days=365)


    # Add a button on the form view when you click on it, it will link few existing
    # records to the current model’s many2many field


    def link_record(self):

        # ids=[2]
        res1 = self.write({"service_needed": [(6,0,[1 ])]})
        print(" partial remove  ",res1)



class Customer_Parts(models.Model):
    _name = "customer.parts"
    _description = "pasrts for customer"



    vehicle_d_id = fields.Many2one('garage.vehicledigonis','parts_needed_id')
    parts_id = fields.Many2one('garage.parts')
    qty = fields.Integer("qty")

    price = fields.Float("Price")

    @api.depends('qty', 'parts_id')
    def verify_update(self):
        for stock in self:
            stock.parts_id.qty -= stock.qty
        print("________________", stock.parts_id.qty)
        # for x in parts_stock_qty:
        #     print("********************",x.)
        # # for gp in parts_stock_qty:
        # #     print("--------------------------",gp.qty)
        # # # for stock in self:
        # # #     update_qty = parts_stock_qty.qty - stock.qty






