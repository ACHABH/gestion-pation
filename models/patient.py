from odoo import models, fields, api


class Patient(models.Model):
    _name = "medical.patient"
    _description = "Patient Management"
    _rec_name = 'nom'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    genre = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string="Genre", required=True)
    email = fields.Char(string="Email")
    date_naissance = fields.Date(string="Date de naissance", required=True)
    photo = fields.Binary(string="Photo", attachment=True)

    prescription_ids = fields.One2many(
        'medical.prescription', 'patient_id', string="Prescriptions")
    rendez_vous_ids = fields.One2many(
        'medical.rendez.vous', 'patient_id', string="Rendez-vous")
