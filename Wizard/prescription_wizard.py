# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PrescriptionWizardLine(models.TransientModel):
    _name = 'prescription.wizard.line'
    _description = 'Ligne de médicament pour le wizard'

    wizard_id = fields.Many2one(
        'prescription.wizard', string='Wizard', required=True, ondelete='cascade')
    medicament_id = fields.Many2one(
        'medical.medicament', string='Médicament', required=True)
    posologie = fields.Char(string='Posologie', required=True)
    date_prise = fields.Date(string='Date de prise',
                             required=True, default=fields.Date.today)


class PrescriptionWizard(models.TransientModel):
    _name = 'prescription.wizard'
    _description = 'Wizard de création de prescription'

    patient_id = fields.Many2one(
        'medical.patient', string='Patient', required=True)
    medecin_id = fields.Many2one(
        'medical.medicin', string='Médecin', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    ligne_medicament_ids = fields.One2many(
        'prescription.wizard.line',
        'wizard_id',
        string='Médicaments'
    )

    @api.model
    def default_get(self, fields_list):
        """Récupère le patient depuis le contexte"""
        res = super(PrescriptionWizard, self).default_get(fields_list)
        if self.env.context.get('active_id'):
            res['patient_id'] = self.env.context.get('active_id')
        return res

    @api.multi
    def action_create_prescription(self):
        """Crée la prescription avec les médicaments"""
        self.ensure_one()

        # Créer d'abord la prescription
        prescription = self.env['medical.prescription'].create({
            'patient_id': self.patient_id.id,
            'medecin_id': self.medecin_id.id,
            'date': self.date,
        })

        # Créer les lignes de médicaments
        ligne_ids = []
        for ligne in self.ligne_medicament_ids:
            ligne_medicament = self.env['medical.ligne.medicament'].create({
                'prescription_id': prescription.id,
                'medicament_id': ligne.medicament_id.id,
                'posologie': ligne.posologie,
                'date_prise': ligne.date_prise,
            })
            ligne_ids.append(ligne_medicament.id)

        # Mettre à jour la prescription avec les lignes de médicaments
        # Utilisation de (6, 0, liste_ids) pour remplacer tous les enregistrements
        prescription.write({
            'medicament_ids': [(6, 0, ligne_ids)]
        })

        # Retourner vers la vue de la prescription créée
        return {
            'type': 'ir.actions.act_window',
            'name': 'Prescription créée',
            'res_model': 'medical.prescription',
            'res_id': prescription.id,
            'view_mode': 'form',
            'target': 'current',
        }
