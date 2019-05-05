# O meu desafio
Montar um parser em python para 2 arquivos, que rode em um container e que gere um arquivo csv para cada.

## To-do
- [x] Gerar o csv do arquivo de log através de seu o parsing
- [x] Gerar o csv do arquivo json através de seu o parsing
- [x] Criar um arquivo docker-compose.yml que executará o parser de cada arquivo em imagens diferentes

## Modo de uso
``` bash
# Baixando o repositório
git clone https://github.com/aleroxac/intelipost-jobtest.git
cd intelipost-jobtest

# Gerando e executando as imagens dos parsers com o docker-compose
sudo docker-compose up --build
sudo docker-compose run -v $PWD:/code parser-log python parser.py -l
sudo docker-compose run -v $PWD:/code parser-json python parser.py -j

# Gerando e executando o container do parser via Docker
sudo docker build -t parser .
sudo docker run parser -v $PWD:/code python parser.py -l
sudo docker run parser -v $PWD:/code python parser.py -j
```
## Requisitos
- python3
- docker
- docker-compose
