# backend

## Dependências para Desenvolvimento

* Docker
* Docker-compose

---

## Setup

Configure as permissões para utilizar comandos "docker" sem utilizar "sudo" com os comandos abaixo:

~~~~ bash
sudo groupadd docker
sudo usermod -aG docker $USER
~~~~

### Criar arquivo de variáveis de ambiente .env

~~~~ bash
cp sample.env .env
~~~~

Para autenticar o backoffice no backend,
configure as variaveis OAUTH2_* em ambos projetos com o mesmo valor

### Buildar e startar a aplicação

~~~~ bash
docker-compose up -d --build
~~~~

### Migrar o banco de dados

~~~~ bash
docker-compose run --rm application alembic upgrade head
~~~~

___

## Documentação

<http://localhost:8000/docs>

---

## Comandos úteis

### Migrations

~~~bash
# Executa todas as migrations
alembic upgrade head
~~~
