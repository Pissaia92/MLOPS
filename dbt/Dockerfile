FROM python:3.11-slim

# Instala git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Copia tudo
COPY . .

# Instala dbt-postgres (sem restrição de protobuf)
RUN pip install dbt-postgres==1.7.0

# Define entrada padrão
ENTRYPOINT ["dbt"]