# Usa uma imagem oficial Python 3.8 slim
FROM python:3.8-slim

# Defina a pasta de trabalho dentro do container
WORKDIR /app

# Copie os arquivos de dependências
COPY requirements.txt /app/

# Instale as dependências do Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie o restante do código para dentro do container
COPY . /app/

# Expõe a porta que o Django vai rodar (default 8000)
EXPOSE 8000

# Define a variável de ambiente para evitar buffer de saída e acelerar logs
ENV PYTHONUNBUFFERED=1

# Comando padrão para rodar seu servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]