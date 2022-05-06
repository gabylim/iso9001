# -*- coding: utf-8 -*-
from openerp import http

# class Iso9001(http.Controller):
#     @http.route('/iso_9001/iso_9001/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iso_9001/iso_9001/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iso_9001.listing', {
#             'root': '/iso_9001/iso_9001',
#             'objects': http.request.env['iso_9001.iso_9001'].search([]),
#         })

#     @http.route('/iso_9001/iso_9001/objects/<model("iso_9001.iso_9001"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iso_9001.object', {
#             'object': obj
#         })