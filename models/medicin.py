from odoo import models, fields, api

class Medicin(models.Model):
    _name = "medical.medicin"
    _description = "Medical Doctors Management"
    _rec_name = 'nom'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    specialite = fields.Selection([
        ('cardiologue', 'Cardiologue'),
        ('ophtalmologue', 'Ophtalmologue'),
        ('neurologue', 'Neurologue'),
        ('generaliste', 'Généraliste')
    ], string="Spécialité", required=True)
    telephone = fields.Char(string="Téléphone")
    nationalite = fields.Char(string="Nationalité")
    
    prescription_ids = fields.One2many('medical.prescription', 'medecin_id', string="Prescriptions")
    rendez_vous_ids = fields.One2many('medical.rendez.vous', 'medecin_id', string="Rendez-vous")
