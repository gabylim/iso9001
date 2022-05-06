# -*- coding: utf-8 -*-

from openerp import models, fields, api

   
class hr_employee(models.Model):
   
    
    _inherit = 'hr.employee'
   
    
   
    
    fonction_ids= fields.Many2one(string='fonction',
                                  comodel_name='fonctions',
                                  ondelete="cascade")
    
    employees_ids= fields.Many2one(string='Service',
                                   comodel_name='service',
                                   ondelete="cascade")
    

    competance_employee_ids=fields.Many2many(string='Employes',comodel_name='competance',
                                       relation='employee_rl_competance',
                                       column1='emp_id',
                                       column2='name_cmp'
                                       )
    
    responsable_service_ids = fields.One2many(string='responsable',
                                              comodel_name='service',
                                              inverse_name='responsable_sr_ids'
                                              )
    
   
    
    evaluations_ids= fields.One2many(string='Evaluations',
                                     comodel_name='evaluation.fournisseur',
                                     inverse_name='evaluateur_ids',
                                     ondelete="cascade") 
    
    


      

    
    
                                          