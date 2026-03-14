# Utiliser Python 3.12
FROM python:3.12-slim

# Répertoire de travail
WORKDIR /app

# Copier le projet et le requirements.txt
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Entrypoint
ENTRYPOINT ["python", "scanner.py"]
