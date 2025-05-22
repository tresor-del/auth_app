# Application d'Authentification Django

Bienvenue dans l'application d'authentification Django ! Cette application fournit une solution simple et flexible pour gérer les utilisateurs, l'authentification, et les autorisations dans vos projets Django.

---

## Fonctionnalité

- **Inscription et connexion utilisateur**
- **Réinitialisation de mot de passe via e-mail**
- **Connexion via des fournisseurs OAuth (Google, Facebook, etc.)**
- **Gestion des rôles et permissions**
- **JSON Web Tokens (JWT) pour l'authentification API**
- **Panneau d'administration pour gérer les utilisateurs**

---

## Installation

1. Clonez le dépôt dans votre environnement de développement local :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repository.git
   cd votre-repository
   ```

2. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

3. Appliquez les migrations pour configurer la base de données :

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Lancez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

5. Accédez à l'application sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Configuration

1. **Configurer le fichier ****************************************************`settings.py`**************************************************** :**

   - Ajoutez l'application d'authentification dans `INSTALLED_APPS` :

     ```python
     INSTALLED_APPS = [
         ...
         'auth_app',  
     ]
     ```

   - Configurez les backends d'authentification, si nécessaire :

     ```python
     AUTHENTICATION_BACKENDS = [
         'django.contrib.auth.backends.ModelBackend',
         'allauth.account.auth_backends.AuthenticationBackend',  # Pour OAuth
     ]
     ```

2. **Fournisseurs OAuth :**

   Si vous utilisez des connexions via Google, Facebook ou d'autres fournisseurs, configurez leurs clés API dans vos variables d'environnement ou dans `settings.py` :

   ```python
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'votre-client-id'
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'votre-secret-client'
   ```

3. **JSON Web Tokens (JWT) :**

   Si vous utilisez JWT pour l'authentification API, configurez les paramètres correspondants :

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }
   ```

---

## Utilisation

1. **Inscription et connexion utilisateur :**

   - Les utilisateurs peuvent s'inscrire via le formulaire d'inscription ou utiliser leurs comptes de réseaux sociaux.

2. **Réinitialisation du mot de passe :**

   - Le système envoie un lien de réinitialisation à l'adresse e-mail fournie.

3. **API d'authentification :**

   - Endpoint pour obtenir un token JWT : `/api/token/`
   - Endpoint pour rafraîchir un token JWT : `/api/token/refresh/`

4. **Gestion des utilisateurs :**

   - Les administrateurs peuvent gérer les utilisateurs via le panneau d'administration accessible à `/admin/`.

---

## Tests

Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
python manage.py test
```

---

## Contribution

Les contributions sont les bienvenues ! Veuillez suivre les étapes ci-dessous :

1. Forkez le projet.

2. Créez une branche pour votre fonctionnalité ou correction de bug :

   ```bash
   git checkout -b ma-fonctionnalite
   ```

3. Faites vos modifications et effectuez un commit :

   ```bash
   git commit -m "Description de ma fonctionnalité"
   ```

4. Poussez les modifications :

   ```bash
   git push origin ma-fonctionnalite
   ```

5. Créez une Pull Request sur le dépôt principal.

---

## Licence

Ce projet est sous licence [MIT](LICENSE).

---

## Auteur

Développé par [tresor-del](https://github.com/tresor-del).


