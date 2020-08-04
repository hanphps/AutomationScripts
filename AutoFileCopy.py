import os, shutil
from pathlib import Path

HOME = str(Path.home())
ORIGIN = Path(HOME+'/Documents/Rust-Plugins/Dev/Rust-Forge/Rust-Forge')
MAIN = Path('E:/steamcmd/rust/oxide/plugins')

USE_RULES = False
RULES = '.Rust-Forge.Bonfire'


def check(file):
    file = str(file)
    end = file[-3:]
    if end == '.cs':
        if USE_RULES:
            front = file[:-3]
            names = RULES.split('.')
            for n in names:
                if front == n:
                    return file
        else:
            return file
    else:
        print('error')
        return None

def mover(file):
    file = str(file)
    if not(check(file) is None) == True:
        shutil.copy(file,MAIN)
    else:
        #Need to throw/catch some stuff
        pass

def TestCase1():
    for f in ORIGIN.iterdir():
        f = str(f)
        print(f)
        mover(f)

def main():
    for f in ORIGIN.iterdir():
        mover(f)

#TestCase1()

main()