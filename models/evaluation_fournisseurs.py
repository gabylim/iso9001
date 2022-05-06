# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime

class fournisseur(models.Model):
    _inherit = 'res.partner'
    
    evaluation_ids= fields.One2many(string='Evaluation',
                                    comodel_name='evaluation.fournisseur',
                                    inverse_name='fournisseur_ids'
                                    )
    
    

   
    
class evaluation_fournisseur(models.Model):
    _name='evaluation.fournisseur'    
    _order="datee desc"
    _rec_name="fournisseur_ids"
    image_small = fields.Binary("image_small")
    
    fournisseur_ids= fields.Many2one(comodel_name='res.partner',
                                     required="true",
                                     ondelete="cascade",domain=[('supplier', '=', True)])
   
    datee= fields.Date(default=datetime.today(),readonly=True)
    
    evaluateur_ids= fields.Many2one(comodel_name='hr.employee',
                                    required="true",
                                    ondelete="cascade")
    
    responsable_ids= fields.Many2one(comodel_name='hr.employee',
                                     required="true",
                                     ondelete="cascade")
    
    
    prix_id=fields.Selection(string='Sur Le Prix',selection=[('1','Rien a signaler'),
                                                              ('2','Problème Résolue'),
                                                              ('3','Demande en attente'),
                                                              ('4','Regeté')],default='1')
    
    delai_id=fields.Selection(string='Sur Le Prix',selection=[('1','Rien a signaler'),
                                                              ('2','Problème Résolue'),
                                                              ('3','Demande en Attente'),
                                                              ('4','Regeté')],default='1')
    
    qualiter_id=fields.Selection(string='Sur Le Prix',selection=[('1','Rien a signaler'),
                                                              ('2','Problème Résolue'),
                                                              ('3','Demande en attente'),
                                                              ('4','Regeté')],default='1')
   
    comentaire = fields.Text()
    
    note_id= fields.Integer(compute='calcule_moyenne')
    
    @api.depends('qualiter_id','delai_id','prix_id')
    def calcule_moyenne(self):
        for res in self:
            if res.qualiter_id=='4' or res.delai_id=='4' or res.prix_id=='4':
                res.note_id=0
            elif res.qualiter_id=='3' and res.delai_id=='3' and res.prix_id=='3':
                res.note_id=5
            
            elif ((res.qualiter_id== '3' and res.delai_id=='3' and res.prix_id=='1')or
                   (res.qualiter_id== '3' and res.delai_id=='1' and res.prix_id=='3')or
                   (res.qualiter_id== '1' and res.delai_id=='3' and res.prix_id=='3')or
                   (res.qualiter_id== '2' and res.delai_id=='3' and res.prix_id=='3')or
                   (res.qualiter_id== '3' and res.delai_id=='2' and res.prix_id=='3')or
                   (res.qualiter_id== '3' and res.delai_id=='3' and res.prix_id=='2')):
        
                res.note_id=10
            elif ((res.qualiter_id== '1' and res.delai_id=='1' and res.prix_id=='1')or
                 (res.qualiter_id== '1' and res.delai_id=='1' and res.prix_id=='2')or
                 (res.qualiter_id== '1' and res.delai_id=='2' and res.prix_id=='2')or
                 (res.qualiter_id== '2' and res.delai_id=='2' and res.prix_id=='2')or 
                 (res.qualiter_id== '2' and res.delai_id=='1' and res.prix_id=='1')or
                 (res.qualiter_id== '2' and res.delai_id=='2' and res.prix_id=='1')or
                 (res.qualiter_id== '1' and res.delai_id=='2' and res.prix_id=='1')or
                 (res.qualiter_id== '2' and res.delai_id=='1' and res.prix_id=='2')):
             
                res.note_id=20
            
            
            
            
            else:
                res.note_id=15

      
            
        
       