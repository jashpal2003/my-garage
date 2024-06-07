from odoo import fields,models,api

class Billing(models.Model):
    _name='garage.billing'
    _description ='billing'
    # _rec_name = 'name'

    name = fields.Many2one('garage.vehicledigonis','customer name')
    # vehicle = fields.One2many(related="name.vehicle", string='vehicle Info')

    vehicle_brand = fields.Many2one(related="name.vehicle_brand", string="vehicle brand name")
    vehicle_model = fields.Many2one(related="name.vehicle_model", string='vehicle model name')

    service = fields.Many2many(related="name.service_needed",string="services")
    parts = fields.One2many(related='name.parts_needed_id',string ="parts_needed")


    # currency_id = fields.Many2one('res.currency','Currency')
    amount_pay = fields.Float(compute = "comput_bill_depend",string='total amount to pay:=')
    # final_fees_amount = fields.(currency_field='currency_id',string='Fees Amount')


    @api.depends('parts', 'service')
    def comput_bill_depend(self):
        total_parts_price = 0.0
        total_service_price = 0.0

        for priced in self:
            for pr in priced.parts:
                total_parts_price += pr.price


                print(total_parts_price)

            for sr in priced.service:
                total_service_price += sr.service_price
                print(total_service_price)
            priced.amount_pay = total_service_price + total_parts_price















    #
    # cname = fields.Many2one('garage.customer','customer name')
    # services = fields.Many2many('garage.services','services')
    # parts = fields.Many2many('garage.parts',"parts_needed")
    # amount_pay = fields.Float(compute = "comput_amount_depend",string = 'total amount to pay:=')
    #
    # @api.depends('parts','services')
    # def _comput_price_depend(self):
    #     total_parts_price = 0.0
    #     total_service_price = 0.0
    #
    #
    #     for priced in self:
    #         for pr in priced.parts:
    #             total_parts_price += pr.price
    #             print(total_parts_price)
    #         priced.parts_price = total_parts_price
    #         for sr in priced.service:
    #             total_service_price += sr.service_price
    #             print(total_service_price)
    #         priced.service_price = total_service_price
    #
    #         priced.total_amount = total_service_price + total_parts_price


