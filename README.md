# Python_2_ano_IFC_2026
Usado para escola
# Instruções da AV5
- Abra o git bash
- Clone este repositório usando o “git clone https://github.com/UniverseCoder12/Python_2_ano_IFC_2026.git”
- Abra a pasta “AV5”
- Abra a pasta “projeto”
- Dentro desta pasta, para se conectar em um servidor mysql, crie um arquivo .env que contenha o seguinte conteúdo(exemplo, pode escolher o banco que desejar):
“
MYSQL_USER = root
MYSQL_PASSWORD = root
MYSQL_HOST = localhost
MYSQL_PORT = 3306
MYSQL_DATABASE = estoque
”
- Abra a pasta “projeto” dentro da pasta “projeto”
- Abra um terminal a partir desta pasta
- Verifique se uv está instalado digitando uv no terminal
- Se estiver instalado rode os seguintes comandos no terminal:
    1. uv add sqlalchemy
    2. uv add pymysql
- Depois execute o comando “uv run ../Organizador_de_estoque_6000.py” para rodar o programa
- Agora é só usar o programa
