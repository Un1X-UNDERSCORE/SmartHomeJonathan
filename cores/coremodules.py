# Imports
from cores.speak import say
import os
from threading import Thread

# Make core class
class core:
    # Add a note func
    def addnote():
        say('what do you want to add to your notes? ')
        note = input().lower()
        note = note.strip('\n')
        # Open the text file
        with open('notes.txt', 'a') as f:
            f.write(f'\n{note}')
        say(f'Added {note} to your notes!')
    # List notes func
    def listnotes():
        # Open the text file
        with open('notes.txt', 'r+') as f:
            lines = f.readlines()
            bruh = []
            for line in lines:
                bruh.append(line.strip('\n').strip('\x00'))
            say('Your notes is as following:')
            for aaa in bruh:
                say(aaa)
    # Remove a note func
    def removenote():
        # Get the notes that has to get removed
        say('what do you want to remove from notes? ')
        note = input().lower()
        # Open the text file
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
