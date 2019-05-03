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
# IMPROVEMENTS:
# - Refatoração do arquivo json para que poder ser carregado via biblioteca json do python
# - Só considerei a primeira linha do arquivo json para gerar o header do arquivo csv
#
# TO-DO:
# -generate_csv_for_jsonfile:
#   [] Arrumar a formatação do arquivo csv do json: As linhas de registros devem começar com ";" / Separar o header dos registros
#   [] Gerar 1 linha para cada registro csv do json, ignorando a redundância(as outras 2 linhas do json são cópias da primeira)


import re
import json
import sys


def generate_csv_for_logfile(log_file, csv_file):
    csv_line = ''
    csv_content = []
    csv_fields = {'timestamp': '\d{4}-\d{2}-\d{2} (\d{2}:){2}[0-9]{2},[0-9]{3}',
                    'logtype': '\w{1,} \]',
                    'event': '\[[\w.]{1,}\]',
                    'message': '--.*'}

    with open(log_file) as log: 
        for line in log: 
            csv_line = ';' + str(re.match('\d{4}-\d{2}-\d{2} (\d{2}:){2}[0-9]{2},[0-9]{3}', line)[0])
            csv_line += ';' + str(re.findall('\w{3,} \]', line)[0]).strip(' ]')
            csv_line += ';' + re.findall('\[[\w.]{1,}\]',line)[0].strip('[]')
            csv_line += ';' + re.findall('--.*',line)[0][3:]
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

    with open(json_file) as jsonfile:
        jsonfile_content = json.load(jsonfile)

    for key in jsonfile_content['logs'][0].keys():
        csv_fields.append(key)

    # for line in jsonfile_content['logs']:
    #     for key in line.keys():
    #         print(key)

    for value in jsonfile_content['logs'][0].values():
        csv_values_with_dicts.append(value)

    # for line in jsonfile_content['logs']:
    #     for value in line.values():
    #         print(value)

    for value in csv_values_with_dicts:
        if type(value) == dict:
            csv_values.append(str(list(value.keys())).strip("[]").replace(' ','').replace("'",''))
        else:
            csv_values.append(str(value))

    csv_formatted_fields = ';'.join(csv_fields)
    csv_formatted_values = ";".join(csv_values)

    # with open(csv_file, 'w') as file:
    #     file.write(csv_formatted_fields)
    # with open(csv_file, 'a') as file:
    #     for line in csv_content:
    #         file.write("%s\n" % line)


if __name__ == "__main__":
    # generate_csv_for_logfile('file.log','logFile.csv')
    generate_csv_for_jsonfile('file.log','logFile.csv')


