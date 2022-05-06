# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import datetime

#class test_graph(models.Model):
#    _name='test_graph'
    
#    y_axis_field = fields.Float('interest %', group_operator="avg")
#    total_amount = fields.Float('total amount')
#    paid= fields.Float()

#    _sql_constraints = [
#        ('y_axis_field', 'check(y_axis_field >= 0 and y_axis_field <= 100)', 'y_axis_field should be between 0% and 100%!')
#    ]

   
    #@api.depends('total_amount','paid')
    #def calculate_percentage(self):
    #    self.y_axis_field =((self.total_amount - self.paid) % (self.total_amount + 1))*100
    



class tout_audits(models.Model):
    _name='tout.audit'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    name = fields.Char()
    image_small = fields.Binary("image_small")
    theme_id = fields.Char()
    
    service_id =fields.Many2one(comodel_name='service',required='true',help="Selectionné le service qui vas étre audité")
    
    responsable_service_id=fields.Many2one(related='service_id.responsable_sr_ids',store="true",readonly=True)
    
    date_id = fields.Date(help="Date début d'audit",required='true')
    
    date_fin_id=fields.Date(help="Date fin d'audit",required='true')
    
    date_actuel_id = fields.Date(default=datetime.today(),readonly=True)
    
    type_audit_id = fields.Selection(selection=[('type1', 'Intèrne'),('type2','Extèrne')],help="type de l'audit par rapport a l'auditeur",required="true")
    
    description_id = fields.Text(help="Description génerale de l'audit")
    
    auditeur_externe_id = fields.Many2one(comodel_name='auditeurs',help="rensegné dabord le type(Intèrene ou Extèrne ) pour selectioné l'auditeur ")
    
    auditeur_interne_id = fields.Many2one(comodel_name='hr.employee',help="rensegné dabord le type(Intèrene ou Extèrne ) pour selectioné l'auditeur ")
    
    reclamation_ids = fields.One2many(comodel_name='crm.claim',inverse_name='audit_reclamation_id')
    
    
    state = fields.Selection([('planifier','Planifier'),
                            ('en_cours','En_cours'),
                            ('terminé','Terminé'),
                            ('annulé','Annulé'),],
                            string='Status', index=True, readonly=True, default='planifier')
    
    
    
  
    
    
    test = fields.Char(compute="def_test")   
    @api.depends('type_audit_id')
    def def_test(self):
        for re in self:
            if re.type_audit_id=='type1':
                re.test='Intèrne'
            else:
                re.test='Extèrne'  
      
      #test de date           
    @ api.one 
    @ api.constrains ( 'date_id' ,'date_actuel_id','date_fin_id') 
    def  _check_description ( self ):  
        if  (self.date_id  <  self.date_actuel_id)or(self.date_fin_id<self.date_id ) : 
            raise  ValidationError ( "DATE INVALIDE : Veuillez saisir une autre supériere ou égale a celle d'aujourd'hui" ) 
    
    @ api.one 
    @ api.constrains ( 'date_id','date_fin_id') 
    def  _check_date ( self ):  
        if self.date_fin_id<self.date_id  : 
            raise  ValidationError ( "DATE INVALIDE : Veuillez saisir une autre supériere ou égale a celle de début d'audit" )    
      
    
    
    # button suivant
    @api.multi
    def action_suivant(self):
        self.ensure_one()
        if self.state == 'planifier':
            if self.date_actuel_id>= self.date_id:
                self.write({'state':'en_cours'})
            else:
                raise ValidationError("Date début de l'audit n'est pas arrivé")
                
        elif self.state == 'en_cours':
            self.write({'state':'terminé'}) 
            self.write({'date_fin_id':self.date_actuel_id})
            
        else:
            raise ValidationError("votre etat is finish congratulation")
   
   
   #button Annuler
    @api.multi
    def action_annuler(self):
        self.ensure_one()
        if self.state == 'planifier':
            if self.date_id>=self.date_actuel_id:
                self.write({'state':'annulé'})
            else:
                raise ValidationError("vous pouvez pas annuler l'audit (date d'annulation est passé)")
                
         #erreur   
        elif self.state =='annulé':
            raise ValidationError("l'audit est déja annulé") 
         
        else:
            raise ValidationError("vous pouvez pas annuler l'audit vous etes dans un état supérieur ou l'audit été déja annuler")
                
    
 #_________________________________SEND MAIL___________________________________

    def action_send_mail(self, cr, uid, name, context=None):
        if not context:
            context= {}
        ir_model_data = self.pool.get('ir.model.data')
        template_id = ir_model_data.get_object_reference(cr, uid, 'iso_9001', 'email_template_audit')[1]
        ctx = dict(context)
        ctx.update({
            'default_model': 'tout.audit',
            'default_res_id': name[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
        })
        return {
            #'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }    
      
    
    
    
    
                 # Class auditeurs pour un type d'audit extèrne

class auditeurs(models.Model):
    _name="auditeurs"
    
    name = fields.Char(help="Nom et Prenom de l'auditeur")
    email = fields.Char()
    image_small = fields.Binary("image_small")
    audit_ids = fields.One2many(string='audits',comodel_name='tout.audit',inverse_name="auditeur_externe_id")
    
      