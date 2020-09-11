import string
import os, shutil
from pathlib import Path
import xlsxwriter
import slate3k as slate

"""

    I do a lot of text analysis but (really) some words are more important than others 
    if I can find more important words and their repetition would make my life easier
        -> if specific key phrase is never said, then why am I reading this doc?
    TODO:
        -sort descending count on words in xlsxfile
        -Check if file is a pdf
        -handle non pdf cases

        -focus on keywords and get x # forward and back sentences IMPORTANT



"""

HOME = str(Path.home())
MAIN = Path(HOME+'/Documents/DocLibrary')
REMOVE = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

def strip(st):
    if type(st) == string :
        for char in st:
            if char in REMOVE:  
                st = st.replace(char,'')
    return st

def readFile(file):
    with open(file,'rb') as f:
        read = slate.PDF(f)
    for st in range(len(read)):
        read[st]= read[st].lower()
    f.close()
    return read

def createExcel(name,tab):
    workbook = xlsxwriter.Workbook(str(MAIN)+'/'+name+'_analysis.xlsx')
    ws = workbook.add_worksheet()
    row = 0
    for key,val in tab.items():
        ws.write(row,0,key)
        ws.write(row,1,val)
        row += 1
    workbook.close()

def parseText(tab):
    counter = {}
    for st in tab:
        line = st.split(' ')
        line = strip(line)
        for word in line:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter

def doit(file):
    tab = readFile(file)
    count = parseText(tab)
    name = str(file)
    name = name.split('\\')[-1]
    name = name[:-4]
    createExcel(name,count)
    print('Pass')
    
def Main():
    for f in DOWNLOADS.iterdir():
        doit(f)
Main()

