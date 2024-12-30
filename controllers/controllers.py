# -*- coding: utf-8 -*-
# from odoo import http


# class Autoescuela(http.Controller):
#     @http.route('/autoescuela/autoescuela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autoescuela/autoescuela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen.listing', {
#             'root': '/autoescuela/autoescuela',
#             'objects': http.request.env['examen.autoescuela'].search([]),
#         })

#     @http.route('/autoescuela/autoescuela/objects/<model("examen.autoescuela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen.object', {
#             'object': obj
#         })

