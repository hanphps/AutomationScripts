import os, shutil
from pathlib import Path

"""
    TODO:
        - Make directories for nulls.
        - Task scheduler
        - DONE?
"""

HOME = str(Path.home())
DOWNLOADS = Path(HOME+'/Downloads')
MAIN = Path(HOME+'/Documents/Library')

"""
    Rules for moving files
        FRONT takes front part of name and matches it to specific directory with keywords
        END takes end extensions and matches to specific directory
"""
RULES = {
    'front': {
        'BOOK' : 'Books',
        'SCHOOL' : 'School',
        'WORK' : 'Work',
        'PROJECT': 'Projects'
    },

    'end':{
        '.pdf.ocx' : 'Documents',
        '.png.jpg.mp4': 'Memes',
        '.exe' : 'Installers'
    }
}

def detectRule(file):
    for location, dic in RULES.items():
        for i,v in dic.items():
            if location == 'front':
                if i in file:
                    return v
            
            elif location == 'end':
                end = file[-3:]
                types = i.split('.')
                for e in types:
                    if end == e:
                        return v

            else:
                print('error') #change to return NULL later 
                return None       

def checkDestinationExist(name):
    if not(MAIN is None):
        if name in (os.listdir(MAIN)):
            return True  
    else:
        return False



def mover(file):
    file = str(file)
    directory = detectRule(file)
    if checkDestinationExist(directory) == True:
        directory = Path(str(MAIN)+'/'+directory)
        shutil.move(file,directory)
    else:
        #Need to throw/catch some stuff
        pass

def TestCase1():
    for f in DOWNLOADS.iterdir():
        f = str(f)
        print(f)
        detectRule(f)

def TestCase2():
    TestFolder = Path(str(DOWNLOADS)+'/TestFiles')
    for f in TestFolder.iterdir():
        mover(f)


#TestCase1() PASS
#TestCase2() PASS
