from odoo import models, fields, api


class LigneMedicament(models.Model):
    _name = "medical.ligne.medicament"
    _description = "Medication Line"

    medicament_id = fields.Many2one(
        'medical.medicament', string="Médicament", required=True)
    prescription_id = fields.Many2one(
        'medical.prescription', string="Prescription", required=True)
    date_prise = fields.Date(string="Date de prise", required=True)
    posologie = fields.Char(string="Posologie", required=True)
