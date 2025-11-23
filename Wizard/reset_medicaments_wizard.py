# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResetMedicamentsWizard(models.TransientModel):
    _name = 'reset.medicaments.wizard'
    _description = 'Wizard pour réinitialiser les médicaments d\'une prescription'

    prescription_id = fields.Many2one(
        'medical.prescription', string='Prescription', required=True)
    medicament_count = fields.Integer(
        string='Nombre de médicaments', compute='_compute_medicament_count')
    confirmation = fields.Boolean(
        string='Je confirme la suppression de tous les médicaments', default=False)

    @api.depends('prescription_id')
    def _compute_medicament_count(self):
        """Calcule le nombre de médicaments dans la prescription"""
        for wizard in self:
            wizard.medicament_count = len(
                wizard.prescription_id.medicament_ids)

    @api.model
    def default_get(self, fields_list):
        """Récupère la prescription depuis le contexte"""
        res = super(ResetMedicamentsWizard, self).default_get(fields_list)
        if self.env.context.get('active_id'):
            res['prescription_id'] = self.env.context.get('active_id')
        return res

    @api.multi
    def action_reset_medicaments(self):
        """Supprime tous les médicaments de la prescription"""
        self.ensure_one()

        # Vérifier la confirmation
        if not self.confirmation:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Attention',
                    'message': 'Veuillez cocher la case de confirmation pour continuer.',
                    'type': 'warning',
                    'sticky': False,
                }
            }

        # Récupérer toutes les lignes de médicaments
        medicaments_to_delete = self.prescription_id.medicament_ids
        count = len(medicaments_to_delete)

        # Utiliser unlink() pour supprimer toutes les lignes
        if medicaments_to_delete:
            medicaments_to_delete.unlink()

        # Afficher un message de succès
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Succès',
                'message': f'{count} médicament(s) supprimé(s) avec succès.',
                'type': 'success',
                'sticky': False,
                'next': {
                    'type': 'ir.actions.act_window',
                    'res_model': 'medical.prescription',
                    'res_id': self.prescription_id.id,
                    'view_mode': 'form',
                    'target': 'current',
                }
            }
        }
