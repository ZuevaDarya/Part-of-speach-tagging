from urllib.request import urlopen
from bs4 import BeautifulSoup

import os
import nltk

html = urlopen('https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt')

bs = BeautifulSoup(html.read(), 'html.parser')

new_file = 'task.txt'
dir = './'

def txt_writer(data, new_file, dir):
    file_name = check_file(new_file, dir)
    path = dir + file_name

    with open(path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(data.get_text())

def check_file(new_file, dir):
    file_name = new_file.split('.')[0]
    file_expansion = new_file.split('.')[1]

    file_count = 0
    dir_files = []

    for dir_file in os.walk(dir):
        dir_files.append(dir_file)

    for files in dir_files:
        for dir_file in files[2]:
            dir_file_name = dir_file.split('.')[0]
            if file_name in dir_file_name and dir_file.split('.')[1] == file_expansion:
                file_count += 1

    return f"{file_name}_{file_count}.{file_expansion}"

def word_tokenize(file_name):
    with open(file_name, encoding='utf-8') as txt_file:
        tokens = nltk.word_tokenize(txt_file.read())
        tagged = nltk.pos_tag(tokens)
        nnCount = 0
        jjCount = 0
        rbCount = 0
        inCount = 0
        vbCount = 0
        prCount = 0

        for tag in tagged:
            # Существительное
            if 'NN' in tag[1]: nnCount += 1
            # Прилагательное
            elif 'JJ' in tag[1]: jjCount += 1
            # Наречия
            elif 'RB' in tag[1]: rbCount += 1
             # Междометия
            elif 'IN' in tag[1]: inCount += 1
            # Глаголы
            elif 'VB' in tag[1]: vbCount += 1
            # Предлоги
            elif 'PR' in tag[1]: prCount += 1

    new_file = 'task_output.txt'
    new_file_name = check_file(new_file, './')

    with open(new_file_name, 'w', encoding='utf-8') as txt_file:
        txt_file.write(
            f'NN: {nnCount}\nJJ: {jjCount}\nRB: {rbCount}\nIN: {inCount}\nVB: {vbCount}\nPR: {prCount}')


txt_writer(bs, new_file, dir)
word_tokenize('task_1.txt')
