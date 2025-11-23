from odoo import models, fields, api


class RendezVous(models.Model):
    _name = "medical.rendez.vous"
    _description = "Appointments"
    _rec_name = 'patient_id'

    date = fields.Datetime(string="Date et heure", required=True)
    motif = fields.Text(string="Motif", required=True)
    etat = fields.Selection([
        ('planifie', 'Planifié'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('termine', 'Terminé')
    ], string="État", default='planifie', required=True)
    medecin_id = fields.Many2one(
        'medical.medicin', string="Médecin", required=True)
    patient_id = fields.Many2one(
        'medical.patient', string="Patient", required=True)
