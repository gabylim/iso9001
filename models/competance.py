# -*- coding: utf-8 -*-

from openerp import models, fields, api


class fonctions(models.Model):
    _name = 'fonctions'
    
    
  
  

    name = fields.Char(string='fonction',required="true")
    
    services_fonc_id= fields.Many2one(comodel_name='service')
    departement_id = fields.Many2one(related='services_fonc_id.departement_ids',store=True)
        
        
    
    competance_id = fields.One2many(comodel_name='competance',
                                    inverse_name='fonction_ids'
                                   )
    
    emplyee_ids= fields.One2many(string='Employee:',
                                 comodel_name='hr.employee',
                                 inverse_name="fonction_ids")
    
    
                                         
    

    
   # competance_ids = fields.Many2many(string='competance',comodel_name='competance',
    #                                  relation='fonction_relation_competance',
     #                                 column1='name',
      #                                column2='name_cmp')
    
    
class competance(models.Model):
    _name = 'competance'
    name_cmp = fields.Char(string='Competance',required="true")
    
    type_cmp = fields.Selection(string='type',
                                selection=[('type1','capacité'),
                                           ('type2','connaissance'),
                                           ('type3','attitude')],
                                required="true")
    
    fonction_ids = fields.Many2one(string='fonction',comodel_name='fonctions',required="true")
    
    employee_comp_ids=fields.Many2many(string='Competance',comodel_name='hr.employee',
                                       relation='competance_rl_employee',
                                       column1='name_cmp',
                                       column2='emp_id',)
    
    
    
   # employer_ids = fields.Many2one(string='employer:',comodel_name='student')
   # fonction_ids = fields.Many2many(string='fonction:',comodel_name='fonctions',
    #                                      relation='competance_relation_fonction',
     #                                     column1='name_cmp',
      #                                    column2='name')
    

    

    