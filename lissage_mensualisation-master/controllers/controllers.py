# -*- coding: utf-8 -*-
# from odoo import http


# class Facturehugo(http.Controller):
#     @http.route('/facturehugo/facturehugo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facturehugo/facturehugo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('facturehugo.listing', {
#             'root': '/facturehugo/facturehugo',
#             'objects': http.request.env['facturehugo.facturehugo'].search([]),
#         })

#     @http.route('/facturehugo/facturehugo/objects/<model("facturehugo.facturehugo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facturehugo.object', {
#             'object': obj
#         })
