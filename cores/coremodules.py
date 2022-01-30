from cores.speak import say
import os
from threading import Thread

def start(open):
    os.system('minecraft.lnk')

class core:
    def minecraft():
        say('Ok, opening minecraft :D')
        thread = Thread(target = start, args = ('minecraft.lnk', ))
        thread.start()
    def addnote():
        say('what do you want to add to your notes? ')
        note = input().lower()
        note = note.strip('\n')
        with open('notes.txt', 'a') as f:
            f.write(f'\n{note}')
        say(f'Added {note} to your notes!')
    def listnotes():
        with open('notes.txt', 'r+') as f:
            lines = f.readlines()
            bruh = []
            for line in lines:
                bruh.append(line.strip('\n').strip('\x00'))
            say('Your notes is as following:')
            for aaa in bruh:
                say(aaa)
    def removenote():
        say('what do you want to remove from notes? ')
        note = input().lower()
        with open('notes.txt', 'r+') as f:
            lines = f.readlines()
            file = open('notes.txt', 'w')
            file.close()
            print(lines)
            for line in lines:
                print(line)
                if line.strip('\n') != note:
                    print('added')
                    f.write(line)
        say(f'{note} was removed from your notes')