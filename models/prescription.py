from odoo import models, fields, api


class Prescription(models.Model):
    _name = "medical.prescription"
    _description = "Medical Prescriptions"
    _rec_name = 'medecin_id'

    date = fields.Date(string="Date", required=True, default=fields.Date.today)
    medicament_ids = fields.One2many(
        'medical.ligne.medicament', 'prescription_id', string="Médicaments")
    medecin_id = fields.Many2one(
        'medical.medicin', string="Médecin", required=True)
    patient_id = fields.Many2one(
        'medical.patient', string="Patient", required=True)
