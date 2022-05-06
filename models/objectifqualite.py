# -*- coding: utf-8 -*-

from openerp import models, fields, api

from datetime import datetime

class objectif_qualite_annuel(models.Model):
    _name="objectif.qualite.annuel"
    _rec_name="date_id"
    
    _order="date_id desc"
    name = fields.Char()
    image_small = fields.Binary("image_small")
    date_id= fields.Selection(string="date",selection=[('1','2020'),('2','2021'),
                                      ('3','2022'),('4','2023'),
                                      ('5','2024'),('6','2025'),
                                      ('7','2026'),('8','2027'),
                                      ('9','2028'),('10','2029'),
                                      ('11','2030'),('12','2031'),
                                      ('13','2032'),('14','2033'),
                                      ('15','2034'),('16','2035'),
                                      ('17','2036'),('18','2037'),
                                      ('19','2038'),('20','2039'),
                                      ('21','2040'),('22','2041'),
                                      ('23','2042'),('24','2043'),
                                      ('25','2044'),('26','2045')],required="true",help="Objectif qualité de l'année :")
    
    _sql_constraints = [('date_id', 'unique(date_id)', "Cette année existe déja")]
    
    
    
    
    
    
    
    
    
    object_qualite_ids = fields.One2many(string='Objectif annuel',
                                          comodel_name='objectif.qualite',
                                          inverse_name="objectif_annul_id")
    
    
    
    
    
    
    
    
    

    serviceees_id=fields.Many2many(string='Service',comodel_name='service',
                                   relation='objetanul_service',
                                   column1="date_id",
                                   column2= "name")


   

                
    
    
        

        
        
class objectif_qualite(models.Model):
    _name="objectif.qualite"
    
    
    date = fields.Date(default=datetime.today(),readonly=True,help="date de définition de l'objectif qualité")        
    
    
    description = fields.Char(required='true',help="déscription de l'objectif qualité riel mensuel accomplie ")

    servicees_id = fields.Many2one(string='Service',
                                   comodel_name='service',required="true",
                                   ondelete="cascade")
    
    
    
    
    
    
    
    
    
    
    daate_id = fields.Selection(related="objectif_annul_id.date_id",store="true")
    
    
    objectif_annul_id = fields.Many2one(string="Objectif annuel",
                                        comodel_name="objectif.qualite.annuel",
                                        ondelete="cascade")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    objectif_qualiter_mensuel_ids = fields.One2many(string='mensuel',
                                                    comodel_name='objectif.qualite.mensuel',
                                                    inverse_name="objectif_qualiter_mens_id")
     
    note_id = fields.Integer()
    
  
   
  

  
  
class objectif_qualite_mensuel(models.Model):
    _name ="objectif.qualite.mensuel"
    
    mois_annee_id = fields.Date(default=datetime.today(),readonly=True)  
    
    descriptions = fields.Char(string="Description",help="Une déscription de l'objectif réel obtenu")
    valeur= fields.Integer(string="Note --/20",help="evaluation de votre travaille par rapport a l'objectif globale")
    
    objectif_qualiter_mens_id = fields.Many2one(string="Objectif Atteint ",
                                                comodel_name="objectif.qualite",
                                                ondelete="cascade")
      
        
         
       