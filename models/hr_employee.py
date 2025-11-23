# -*- coding: utf-8 -*-
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    date_debut = fields.Date(string='Date de début')
    nombre_annee = fields.Integer(string='Nombre d\'années')
    num_retraite = fields.Char(string='Numéro de retraite')
    date_retraite = fields.Date(string='Date de retraite')
