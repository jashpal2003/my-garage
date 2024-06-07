from odoo import fields,models,api

class Parts(models.Model):
    _name = "garage.parts"
    _description ="parts"

    name = fields.Char('Name of Parts')
    image = fields.Image("product image")

    price = fields.Float('Price Of Parts')
    qty = fields.Integer("qnty of parts")



    #
    # def  create_rec(self):
    #     r1 ={
    #         'name':'break',
    #         'price':'2000'
    #     }
    #     r2={
    #         'name':'Set of Engine Gasket,',
    #         'price':'100'
    #
    #     }
    #     record_list = [r1,r2]
    #     new_rec = self.create(record_list)
    #     print("auto record created is :====",record_list)
