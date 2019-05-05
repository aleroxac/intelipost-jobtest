#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: Augusto Cardoso dos Santos
# DATE: 2019-05-02
# DESCRIPTION: Implementação de parser proposto no desafio para vaga de Analista DevOps na Intelipost.
# VERSION: 1.0
#
# CHANGELOG:
#   2019-05-02 | 1.0 - generate_csv_for_logfile
#   2019-05-02 | 1.0 - generate_csv_for_jsonfile
#
# INFO:
# - Refatorei o arquivo json para poder carregá-lo nativamente via python
# - Só considerei a primeira linha do arquivo json para gerar o header do arquivo csv
# - Se estivéssemos em um ambiente de produção teríamos que usar ponteiros para
#   fazer a leitura dos arquivos. Esse aspecto não foi considerado nessa
#   implementação, visando a simplicidade.


from re import findall
from json import load
from sys import argv
from os import path


def generate_csv_for_logfile(log_file, csv_file):
    csv_line = ''
    csv_content = []
    csv_fields = {'timestamp': '\d{4}-\d{2}-\d{2} (\d{2}:){2}[0-9]{2},[0-9]{3}',
                    'logtype': '\w{1,} \]',
                    'event': '\[[\w.]{1,}\]',
                    'message': '--.*'}

    with open(log_file) as log:
        for line in log:
            csv_line = ';' + str(findall('\d{4}-\d{2}-\d{2} (\d{2}:){2}[0-9]{2},[0-9]{3}', line)[0])
            csv_line += ';' + str(findall('\w{3,} \]', line)[0]).strip(' ]')
            csv_line += ';' + findall('\[[\w.]{1,}\]',line)[0].strip('[]')
            csv_line += ';' + findall('--.*',line)[0][3:]
            csv_content.append(csv_line)

    csv_file_header = 'timestamp;logtype;event;message\n'

    with open(csv_file, 'w') as file:
        file.write(csv_file_header)
    with open(csv_file, 'a') as file:
        for line in csv_content:
            file.write("%s\n" % line)


def generate_csv_for_jsonfile(json_file, csv_file):
    csv_fields = []
    csv_values_with_dicts = []
    csv_values = []
    csv_lines = []

    with open(json_file) as jsonfile:
        jsonfile_content = load(jsonfile)

    for key in jsonfile_content['logs'][0].keys():
        csv_fields.append(key)

    for line in jsonfile_content['logs']:
        for value in line.values():
            csv_values_with_dicts.append(value)
        csv_values_with_dicts.append('\n')

    for value in csv_values_with_dicts:
        if type(value) == dict:
            csv_values.append(str(list(value.keys())).strip("[]").replace(' ','').replace("'",''))
        else:
            csv_values.append(str(value))

    csv_formatted_fields = ';'.join(csv_fields)
    csv_formatted_values = ";" + ";".join(csv_values)

    with open(csv_file, 'w') as file:
        file.write(csv_formatted_fields+'\n')
        file.write(csv_formatted_values)


def usage_message():
    print('Uso: ' + path.basename(argv[0]) + ' [OPCAO]\n\
    Implementação de parser proposto no desafio para vaga de Analista DevOps na Intelipost\n\
        -l Faz o parse do arquivo file.log e gera o logFile.csv\n\
        -j Faz o parse do arquivo json.log e gera o jsonFile.csv\n\
        -h Mostra esta ajuda')

if __name__ == "__main__":
    try:
        if argv[1] == '-l':
            generate_csv_for_logfile('file.log','logFile.csv')
        elif argv[1] == '-j':
            generate_csv_for_jsonfile('json.log','jsonFile.csv')
        else:
            usage_message()
    except IndexError:
        usage_message()
