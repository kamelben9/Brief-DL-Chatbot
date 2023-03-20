### *Ceci est une version temporaire du README.md : il faudra la retravailler et la compléter*

# Chatbot Conversationnel NLP - Preuve de Concept

Ceci est un projet de preuve de concept pour un chatbot conversationnel qui utilise le traitement du langage naturel (NLP) pour interagir avec les utilisateurs. Le chatbot doit pouvoir répondre aux entrées utilisateur de manière conversationnelle.

## Versions

Le framework Streamlit a été choisi pour ce projet.
Plusieurs versions du chatbot sont disponibles, chacune avec une complexité croissante. Les versions sont énumérées ci-dessous par ordre de complexité :

1. [Version 1 - API OpenAI](https://github.com/kamelben9/Brief-DL-Chatbot/tree/CBA-81-En-tant-qu-utilisateur-final-je-veux-acces-un-chatbot-basique-sans-memoire-des-messages-passes-utilisant-l-API-d-OpenAI-et-son-modele-GPT-3-text-davinci-003) : application Streamlit basique avec une interface simple, utilisant l'API OpenAI. Comprend un champ de texte pour que les utilisateurs écrivent quelque chose et un champ de chat pour enregistrer les entrées utilisateur et les réponses du bot. L'objet de cette version est d'implémenter un squelette applicatif de base pour la suite.

Notez que pour pouvoir utiliser cette version, il vous faudra créer un fichier 'openai_api_key.env' dans le dossier 'premiers_tests' et y inscrire votre API Key pour OpenAI. Le fichier contiendra ceci (c'est un exemple, la clé n'est pas valable):

```sh
API_KEY=sk-LEse4vpb7vXaXhHyrTc3lbhJeqxldpfp8bq8mvr13d
```

2. [Version 2](#)

3. [Version 3](#)

## Comment exécuter

Pour exécuter n'importe quelle version du chatbot, suivez ces étapes :

1. Clonez le dépôt sur votre machine locale et placez-vous dans le dossier de la version souhaitée:

```sh
git clone https://github.com/username/chatbot.git
```

2. Installez les dépendances requises :

```sh
pip install -r requirements.txt
```

3. Accédez à la version que vous souhaitez exécuter :

```sh
cd chatbot/premiers_tests
```

4. Exécutez l'application Streamlit :

```sh
streamlit run basic_GPT3_chatbot.py
```

## Contributeurs

Les contributeurs au projet sont :

- Omar
- Kevin
- Kamel
- Cédric

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](https://opensource.org/license/mit/) pour plus d'informations.
