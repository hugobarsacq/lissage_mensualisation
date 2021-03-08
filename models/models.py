# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools
from datetime import date, timedelta, datetime

import calendar
import logging
_logger = logging.getLogger(__name__)

class lissage(models.Model):
    _name = 'lissage'
    _description = 'lissage'

    @api.model
    def factureE(self, invoice_id):

        date = self.env['account.move'].search([('id', '=', invoice_id)]).invoice_date
        montant = self.env['account.move'].search([('id', '=', invoice_id)]).amount_total
        strDate = str(date)
        cutDate = (datetime.strptime(strDate, '%Y-%m-%d')).strftime('%d/%m/%Y')
        cutDate2 = (datetime.strptime(strDate, '%Y-%m-%d')).strftime('%m')
        cutDate3 = (datetime.strptime(strDate, '%Y-%m-%d')).strftime('%Y')
        intCutDate2 = int(cutDate2)
        intCutDate3 = int(cutDate3)
        autresmois = int(montant / ((12 - int(cutDate2)) + 1))
        strautresmois = str('{:.2f} '.format(autresmois))
        le1ermois = montant - (autresmois * 10)
        strle1ermois = str('{:.2f} '.format(le1ermois))
        le2ememois = int(cutDate2) + 1
        strle2ememois = str(le2ememois)
        date_calendar = calendar.monthrange(intCutDate3, intCutDate2)
        last_day = str(date_calendar[1])

        la1erephrase = "Prélèvement le " + cutDate + " de " + strle1ermois + "€"

        list = []
        for i in range(le2ememois, 13):
            date_calendar2 = calendar.monthrange(intCutDate3, i)
            last_day2 = str(date_calendar2[1])
            if i < 10:
                i = "0" + str(i)
                list.append("Prélèvement le 01/" + str(i) + "/" + cutDate3 + " de " + strautresmois + "€")
            else:
                list.append("Prélèvement le 01/" + str(i) + "/" + cutDate3 + " de " + strautresmois + "€")
            listToStr = "\n".join([str(elem) for elem in list])

        concatenate = "La facture couvre la période suivante : " + cutDate + " - " + "31/12/" + cutDate[
                                                                                                -4:] + "\n" + "\n" + la1erephrase + "\n" + listToStr

        accounts = self.env['account.move'].search([('id', '=', invoice_id)]).update({'narration': concatenate})



class ResConfigSettings(models.TransientModel):
    _name = 'settingslissage'
    _description = 'settingslissage'
    _inherit = 'res.config.settings'
    _logger.debug('eymeric')
    # journal_hugo = fields.Many2one('account.journal', string="Journal", store=True)
    journal_hugo = fields.Char('account.journal', store=True)


















#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
