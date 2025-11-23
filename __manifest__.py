
{
    "name": "Gestion Pation",
    "version": "2.0",
    "category": "Gestion",
    "author": "Abdelhalim",
    "depends": ["base"],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'Wizard/prescription_wizard.xml',
        'Wizard/add_medicament_wizard.xml',
        'Wizard/reset_medicaments_wizard.xml',
        'views/medicin.xml',
        'views/patient.xml',
        'views/prescription.xml',
        'views/medicament.xml',
        'views/rendez_vous.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
