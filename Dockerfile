# Utilise une image Python légère
FROM python:3.11-slim

# Empêche Python de créer des fichiers .pyc et force le flush stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Crée le dossier de travail
WORKDIR /app

# Installe les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code du bot
COPY code_1.py ./

# Commande par défaut pour lancer le bot
CMD ["python", "-u", "code_1.py"]
