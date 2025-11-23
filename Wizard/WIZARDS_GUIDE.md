# Guide complet des Wizards - Gestion Patient

## Vue d'ensemble

Ce module contient deux wizards pour faciliter la gestion des prescriptions et des médicaments :

1. **Prescription Wizard** : Créer une nouvelle prescription depuis un patient
2. **Add Medicament Wizard** : Ajouter un médicament à une prescription existante

---

## 1. Wizard de création de prescription

### Accès

- **Depuis** : Formulaire Patient
- **Bouton** : "Créer une prescription" (en-tête)

### Fonctionnalités

- Patient pré-rempli automatiquement
- Sélection du médecin
- Ajout de plusieurs médicaments en une fois
- Création automatique de la prescription avec toutes les lignes

### Technique utilisée

```python
# Création de la prescription
prescription = self.env['medical.prescription'].create({...})

# Création des lignes
for ligne in self.ligne_medicament_ids:
    ligne_medicament = self.env['medical.ligne.medicament'].create({...})
    ligne_ids.append(ligne_medicament.id)

# Utilisation de (6, 0, liste_ids) pour remplacer tous les enregistrements
prescription.write({
    'medicament_ids': [(6, 0, ligne_ids)]
})
```

### Commande Odoo : `(6, 0, [ids])`

- **Action** : Remplace tous les enregistrements liés par la nouvelle liste
- **Équivalent Python** : `liste = [nouvel1, nouvel2, nouvel3]`
- **Usage** : Initialisation complète d'une relation One2many

---

## 2. Wizard d'ajout de médicament

### Accès

- **Depuis** : Formulaire Prescription
- **Bouton** : "Ajouter un médicament" (en-tête)

### Fonctionnalités

- Prescription pré-remplie automatiquement
- Sélection d'un médicament
- Saisie de la posologie
- Sélection de la date de prise
- Ajout à la prescription existante sans affecter les autres médicaments

### Technique utilisée

```python
# Création de la nouvelle ligne
new_ligne = self.env['medical.ligne.medicament'].create({
    'prescription_id': self.prescription_id.id,
    'medicament_id': self.medicament_id.id,
    'posologie': self.posologie,
    'date_prise': self.date_prise,
})

# Utilisation de (4, id) pour ajouter un enregistrement (append)
self.prescription_id.write({
    'medicament_ids': [(4, new_ligne.id)]
})
```

### Commande Odoo : `(4, id)`

- **Action** : Ajoute un enregistrement existant à la relation
- **Équivalent Python** : `liste.append(nouvel_element)`
- **Usage** : Ajout incrémental à une relation One2many

---

## Comparaison des commandes Odoo pour One2many/Many2many

| Commande            | Action                   | Équivalent Python               | Usage                                |
| ------------------- | ------------------------ | ------------------------------- | ------------------------------------ |
| `(0, 0, values)`    | Créer et ajouter         | `liste.append(new)`             | Créer un nouvel enregistrement       |
| `(1, id, values)`   | Mettre à jour            | `liste[i] = updated`            | Modifier un enregistrement           |
| `(2, id)`           | Supprimer définitivement | `del liste[i]` + suppression DB | Supprimer de la relation et de la DB |
| `(3, id)`           | Retirer de la relation   | `liste.remove(item)`            | Retirer sans supprimer de la DB      |
| **`(4, id)`**       | **Ajouter existant**     | **`liste.append(item)`**        | **Ajouter à la relation**            |
| `(5,)`              | Vider la relation        | `liste.clear()`                 | Supprimer tous les liens             |
| **`(6, 0, [ids])`** | **Remplacer tous**       | **`liste = [...]`**             | **Réinitialiser la relation**        |

---

## Structure des fichiers

```
Wizard/
├── __init__.py                        # Import des wizards
├── prescription_wizard.py             # Wizard de création de prescription
├── prescription_wizard.xml            # Vues du wizard de prescription
├── add_medicament_wizard.py          # Wizard d'ajout de médicament
├── add_medicament_wizard.xml         # Vues du wizard d'ajout
├── README.md                         # Doc wizard de prescription
├── ADD_MEDICAMENT_README.md          # Doc wizard d'ajout
└── WIZARDS_GUIDE.md                  # Ce fichier (guide complet)
```

---

## Installation et mise à jour

1. **Redémarrer le serveur Odoo**
2. **Mettre à jour le module** `gestion_patient`
3. Les boutons apparaîtront automatiquement dans les formulaires

---

## Bonnes pratiques

### Quand utiliser `(6, 0, [ids])` ?

- Initialisation d'une nouvelle relation
- Remplacement complet de tous les enregistrements
- Import de données
- Synchronisation de données

### Quand utiliser `(4, id)` ?

- Ajout d'un élément à une liste existante
- Ajout incrémental sans toucher aux autres
- Actions utilisateur (ajout manuel)
- Modifications partielles

### Sécurité

- Les deux wizards utilisent `TransientModel` (données temporaires)
- Validation des données requises (`required=True`)
- Droits d'accès définis dans `ir.model.access.csv`

---

## Exemples d'utilisation

### Créer une prescription complète

```python
# Via le wizard depuis un patient
1. Ouvrir le patient
2. Cliquer "Créer une prescription"
3. Choisir le médecin
4. Ajouter plusieurs médicaments en même temps
5. Valider -> Prescription créée avec tous les médicaments
```

### Ajouter un médicament à une prescription existante

```python
# Via le wizard depuis une prescription
1. Ouvrir la prescription
2. Cliquer "Ajouter un médicament"
3. Choisir le médicament
4. Saisir posologie et date
5. Valider -> Médicament ajouté à la prescription
```

---

## Dépannage

### Le bouton n'apparaît pas

- Vérifier que le fichier XML est dans `__manifest__.py`
- Vérifier l'ordre de chargement (wizard avant la vue qui l'utilise)
- Redémarrer Odoo et mettre à jour le module

### Erreur "External ID not found"

- Le fichier wizard XML doit être chargé **avant** la vue qui le référence
- Vérifier l'ordre dans `__manifest__.py`

### Erreur de droits d'accès

- Vérifier que le modèle est dans `ir.model.access.csv`
- Format : `access_id,access.name,model_id,,1,1,1,1`

---

## Support

Pour toute question ou problème :

1. Consulter les fichiers README individuels
2. Vérifier les logs Odoo
3. Vérifier la structure des données dans la base
