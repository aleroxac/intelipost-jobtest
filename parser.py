#!/usr/bin/env python3


import re
import sys


def generate_csv_for_logfile(log_file, csv_file):
    csv_line = ''
    csv_content = []
    csv_fields = {'timestamp': '\d{4}-\d{2}-\d{2} (\d{2}:){2}[0-9]{2},[0-9]{3}',
                    'logtype': '\w{1,} \]',
                    'event': '\[[\w.]{1,}\]',
                    'message': '--.*'}

    with open(log_file) as file: 
        for line in log: 
            csv_line = re.match('\d{4}-\d{2}-\d{2} (\d{2}:){2}[0-9]{2},[0-9]{3}', line)[0]
            csv_line += ';' + str(re.findall('\w{3,} \]', line)[0]).strip(' ]')
            csv_line += ';' + re.findall('\[[\w.]{1,}\]',line)[0].strip('[]')
            csv_line += ';' + re.findall('--.*',line)[0][3:]
            csv_content.append(csv_line)

    with open(csv_file, 'w') as file:
        for line in csv_content:
            file.write("%s\n" % line)


def generate_csv_for_jsonfile(json_file, csv_file):
    pass


if __name__ == "__main__":
    generate_csv_for_logfile('file.log','logFile.csv')


