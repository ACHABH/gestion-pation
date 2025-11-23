# -*- coding: utf-8 -*-
from odoo import models, fields


class Patient(models.Model):
    _name = 'patient'

    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénom")
    date_naissance = fields.Date(string="Date de naissance")
    nationalite = fields.Char(string="Nationalité")
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ])
