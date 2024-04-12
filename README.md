# Todo List API

### **API de liste de tâches utilisant Firebase**

**Objectif :** Développer une API CRUD (Créer, Lire, Mettre à jour, Supprimer) pour une application de gestion de liste de tâches en utilisant Firebase comme base de données.

### Points de terminaison:

- **`/todos`** : Lister toutes les tâches et ajouter une nouvelle tâche.
- **`/todos/{id}`** : Récupérer, mettre à jour ou supprimer une tâche spécifique.

### Tâches :

- **Utiliser Firebase Database :** Stocker les tâches dans Firebase pour permettre une persistance des données.
- **Tester les endpoints**
- **Implementer pipeline de test**

### Tests :

- **Tester les endpoints pour le comportement attendu :** S'assurer que chaque action CRUD fonctionne correctement avec Firebase.
- **Inclure des tests pour les modes de défaillance potentiels :** Par exemple, tester la suppression d'une tâche non existante.
- **Authentification et autorisation (si implémentée) :** Tester les scénarios avec et sans authentification valide.

### Pipeline CI :

- **Exécuter les tests :** Assurer que tous les tests passent avant tout déploiement ou merge dans la branche principale.
- **Feeback de coverage** :  Creer un feedback de coverage pour verifier le coverage complet des tests de votre application