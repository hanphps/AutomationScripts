import os, shutil
from pathlib import Path

HOME = str(Path.home())
DOWNLOADS = Path(HOME+'/Downloads')
#MAIN = Path('hannah/Documents/Library')

RULES = {
    'front': {
        'BOOK' : {'Books'},
        'SCHOOL' : {'School'},
        'WORK' : {'Work'},
        'PROJECT': {'Projects'}
    },

    'end':{
        '.pdf.ocx' : {'Documents'},
        '.png.jpg.mp4':{'Memes'},
        '.exe' : {'Installers'}
    }
}

def detectRule(file):
    for location, dic in RULES.items():
        for i,v in dic.items():
            if location == 'front':
                if i in file:
                    print(v) #change to return later
            
            elif location == 'end':
                end = file[-3:]
                types = i.split('.')
                for e in types:
                    if end == e:
                        print(v) #change to return later

            else:
                print('error') #change to return NULL later         


#def mover(file):
    #TODO make it!


def TestCase():
    for f in DOWNLOADS.iterdir():
        f = str(f)
        print(f)
        detectRule(f)

TestCase()