# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Dossier(models.Model):
    _name = "medical.dossier"
    _description = "Medical Dossier"
    _rec_name = 'numéro_dossier'

    # Champs supplémentaires
    numéro_dossier = fields.Char(string="Numéro de dossier", required=True)
    observation = fields.Text(string="Observation")
    
    # Champs de prescription
    date = fields.Date(string="Date", required=True, default=fields.Date.today)
    medicament_ids = fields.One2many(
        'medical.ligne.medicament', 'dossier_id', string="Médicaments")
    medecin_id = fields.Many2one(
        'medical.medicin', string="Médecin", required=True)
    patient_id = fields.Many2one(
        'medical.patient', string="Patient", required=True)
