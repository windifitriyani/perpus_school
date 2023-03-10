# -*- coding: utf-8 -*-
# from odoo import http


# class PerpusSchool(http.Controller):
#     @http.route('/perpus_school/perpus_school/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/perpus_school/perpus_school/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('perpus_school.listing', {
#             'root': '/perpus_school/perpus_school',
#             'objects': http.request.env['perpus_school.perpus_school'].search([]),
#         })

#     @http.route('/perpus_school/perpus_school/objects/<model("perpus_school.perpus_school"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('perpus_school.object', {
#             'object': obj
#         })
