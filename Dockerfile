# Utilise l'image de base de Python 3.9
FROM python:3.9-slim-buster
# Copie des fichiers de l'application dans le conteneur
WORKDIR /app
# Installation des dépendances


COPY requirements.txt .
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exposition du port 8501 pour Streamlit
EXPOSE 8501

# Démarrage de l'application
CMD ["streamlit", "run", "streamlit_azure_chatbox.py", "--server.port", "8501"]