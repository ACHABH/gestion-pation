# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AddMedicamentWizard(models.TransientModel):
    _name = 'add.medicament.wizard'
    _description = 'Wizard pour ajouter un médicament à une prescription'

    prescription_id = fields.Many2one(
        'medical.prescription', string='Prescription', required=True)
    medicament_id = fields.Many2one(
        'medical.medicament', string='Médicament', required=True)
    posologie = fields.Char(string='Posologie', required=True)
    date_prise = fields.Date(string='Date de prise',
                             required=True, default=fields.Date.today)

    @api.model
    def default_get(self, fields_list):
        """Récupère la prescription depuis le contexte"""
        res = super(AddMedicamentWizard, self).default_get(fields_list)
        if self.env.context.get('active_id'):
            res['prescription_id'] = self.env.context.get('active_id')
        return res

    @api.multi
    def action_add_medicament(self):
        """Ajoute le médicament à la prescription existante"""
        self.ensure_one()

        # Créer une nouvelle ligne de médicament
        new_ligne = self.env['medical.ligne.medicament'].create({
            'prescription_id': self.prescription_id.id,
            'medicament_id': self.medicament_id.id,
            'posologie': self.posologie,
            'date_prise': self.date_prise,
        })

        # Utiliser append() sur la relation One2many
        # En Odoo, cela se fait avec la commande (4, id) qui ajoute un enregistrement existant
        self.prescription_id.write({
            'medicament_ids': [(4, new_ligne.id)]
        })

        # Retourner vers la vue de la prescription
        return {
            'type': 'ir.actions.act_window',
            'name': 'Prescription',
            'res_model': 'medical.prescription',
            'res_id': self.prescription_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
