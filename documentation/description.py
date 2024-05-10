# API Description
api_description = """
API de liste de tâches

Objectif : Développer une API CRUD (Créer, Lire, Mettre à jour, Supprimer) pour une application de gestion de liste de tâches en utilisant Firebase comme base de données.

Points de terminaison:

- `/todos` : Lister toutes les tâches et ajouter une nouvelle tâche.
- `/todos/{id}` : Récupère, mets à jour ou supprime une tâche spécifique.

Modèle de données:
- `id` : Identifiant unique de la tâche.    
- `name` : Nom de la tâche. 
- `description` : Description de la tâche.
- `date` : Date de la tâche.
- `priority` : Priorité de la tâche.
- `status` : Statut de la tâche (En cours, Terminé, En attente).

"""