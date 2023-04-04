Chatbot avec LUIS et Blenderbot

Il s'agit d'une application Streamlit qui démontre une implémentation de chatbot en utilisant LUIS et Blenderbot. Le chatbot prend l'entrée utilisateur, l'envoie à LUIS pour prédire l'intention et les entités, et génère une réponse en utilisant Blenderbot. L'historique de conversation est affiché sur la page.
Pour commencer

Pour exécuter cette application, vous devrez installer les packages suivants :



streamlit
transformers
azure-cognitiveservices-language-luis
msrest

Vous devrez également fournir votre ID d'application LUIS et votre clé d'abonnement dans le code.



Comment utiliser


Exécutez l'application en tapant "streamlit run app.py" dans la ligne de commande.
Entrez votre message dans la zone de saisie de texte et appuyez sur Entrée pour envoyer.
Le chatbot générera une réponse en fonction de votre entrée et l'affichera sur la page.
L'historique de conversation est également affiché sur la page.

Composants

streamlit : Streamlit est une bibliothèque Python qui vous permet de créer des applications web pour les projets d'apprentissage automatique et de science des données.
transformers : Transformers est une bibliothèque Python pour les tâches de traitement du langage naturel (NLP), telles que la classification de texte, la réponse aux questions et les agents conversationnels.
azure-cognitiveservices-language-luis : Il s'agit d'un kit de développement logiciel Python pour le service Azure Language Understanding (LUIS). LUIS est un service de traitement du langage naturel basé sur le cloud qui vous permet de construire des agents conversationnels capables de comprendre une entrée en langage naturel.
msrest : Il s'agit d'une bibliothèque Python pour travailler avec des API RESTful, comme l'API LUIS.

L'application utilise un modèle Blenderbot pré-entraîné pour générer des réponses. Les objets tokenizer et model sont obtenus à partir de la fonction get_models(). La fonction get_intent() envoie l'entrée utilisateur à LUIS pour prédire l'intention et les entités, et la fonction generate_answer() génère une réponse en utilisant Blenderbot en fonction de l'entrée utilisateur et de l'intention et des entités prédites.
Crédits

Tout le crédit reviebnt à l'équipe Cédric Duroisin , Kamel Benfattou , Kévin Matchelink,Omar Sahboun , et nos clients/formateurs Charles et Jéremy.