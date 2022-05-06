# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_department(models.Model):

    _inherit = 'hr.department'
    
    service_ids= fields.One2many(string='Service',
                                 comodel_name='service',
                                 inverse_name="departement_ids",
                                 ondelete="cascade")
    
    
    


class hr_service(models.Model):
    
    
    
    
    _name='service'
    name = fields.Char(string='Service',required='true')
    _sql_constraints = [('name', 'unique(name)', "Cette année existe déja")]
    image_small = fields.Binary("image_small")
    employes_ids= fields.One2many(string='Employes',
                                  comodel_name= 'hr.employee',
                                  inverse_name='employees_ids',
                                  ondelete="cascade")

    
    departement_ids = fields.Many2one(string='Département',
                                      comodel_name='hr.department',
                                      ondelete="cascade")
    
    responsable_sr_ids= fields.Many2one(string='Responsable',
                                        comodel_name='hr.employee',
                                        ondelete="cascade")
    
    
   
    
   
    objectif_qualite_service_id= fields.One2many(string='Qualité', 
                                                 comodel_name='objectif.qualite',
                                                 inverse_name="servicees_id")
   
    
    
       
    
    
    
    
    objectif_qualite_anuuel_ids = fields.Many2many(string='Qualité', 
                                           comodel_name='objectif.qualite.annuel',
                                           relation="service_object",
                                           column1="name",
                                           column2="date_id")
                                           
    
    
    
    

