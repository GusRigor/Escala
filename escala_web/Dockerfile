FROM python:3.11-slim

# Defina a pasta de trabalho
WORKDIR /app

# Instale LaTeX e dependências do sistema
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        texlive-latex-base \
        texlive-latex-recommended \
        texlive-fonts-recommended \
        texlive-latex-extra \
        ghostscript \
        make \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

# Copie os arquivos de dependências
COPY requirements.txt /app/

# Instale dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie o código
COPY . /app/

# Exponha a porta
EXPOSE 8000

# Saída não-bufferizada para logs
ENV PYTHONUNBUFFERED=1

# Comando para iniciar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
