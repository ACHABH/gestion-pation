from odoo import models, fields, api

class Medicament(models.Model):
    _name = "medical.medicament"
    _description = "Medications"
    _rec_name = 'nom_commercial'

    nom_commercial = fields.Char(string="Nom commercial", required=True)
    dci = fields.Char(string="DCI", required=True)
    forme = fields.Selection([
        ('gelule', 'Gélule'),
        ('sirop', 'Sirop'),
        ('comprime', 'Comprimé'),
        ('pommade', 'Pommade'),
        ('gel', 'Gel'),
        ('injection', 'Injection')
    ], string="Forme", required=True)
    
    ligne_medicament_ids = fields.One2many('medical.ligne.medicament', 'medicament_id', string="Lignes de médicament")