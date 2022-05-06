# -*- coding: utf-8 -*-

from openerp import models, fields, api

class reclamation(models.Model):
    _inherit ='crm.claim'
    
    audit_reclamation_id = fields.Many2one(comodel_name='tout.audit')
    

    