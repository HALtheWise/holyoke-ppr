# ###############################################################################
# HackHolyoke - PianoPianoRevolution                                            #
#                                                                               #
# Master Script of our project                                                  #
#                                                                               #
# Contains the script to play the piano using the Leap Motion, and also         #
# implements a pygame DDR game that allows users to play and practice with this	#
# invention.                                                                    #
#                                                                               #
# Created by Kevin Zhang, Kimberly Winter, Eric Miller, and Max Wei             #
# ###############################################################################
import pygame, sys
from pygame.locals import *
import noteParser

from mingus.core import progressions, intervals
from mingus.core import chords as ch
from mingus.containers import NoteContainer, Note
from mingus.midi import fluidsynth
import mingus.core.notes as notes

import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
lib_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, lib_dir)

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


import piano_key
import piano_fingers

"""
Game logic - the general game running
"""
current_time = 0.
timeSlice = .25 #each slice of time that contains true false for each note
timeFrame = 4.0 #Notes will show up on screen 2 seconds before playtime.


class keyNote:
     #Create the notes and number them 0 to 7.
     #scalable to account for multiple keys beyond an octave?
     def __init__(note_id):
        ID = note_id


        xPos = 0 #The x position of the note on the screen.
        yPos = 0 #The y position of the note on the screen.

class TimeSliceMatrix():

    def __init__(self):
        self.total_rows = int(timeFrame/timeSlice) #for now, 4 rows.
        self.song = noteParser.getMIDISong()
        self.timeSlice_index = len(self.song.data)
        self.keyslice = noteParser.TimeSlice()


    def getCurrentFrame(self):
        self.song =  noteParser.getMIDISong()
        time_index = int(current_time/timeSlice)
        if time_index + self.total_rows <= len(self.song.data):
            first_slice = self.song.data[time_index]
            processed_slice = process_events(self.keyslice)
            evaluated_slice = self.compareSlice(first_slice, processed_slice)
            self.song.data[time_index] = evaluated_slice
            self.song.data = self.song.data[time_index : time_index + self.total_rows]
            base_slice = noteParser.TimeSlice()

            base_slice.notesActive = KEYS * noteParser.numNotes
            self.song.data = [base_slice] + self.song.data

        else:
            sys.exit()

    def compareSlice(self, first_slice, processed_slice):
        for i in range(len(first_slice.notesActive)):
            if first_slice.notesActive[i] is True:
                if processed_slice.notesActive[i] is True:
                    first_slice.notesActive[i] = 'green'
                else:
                    first_slice.notesActive[i] = 'red'

        return first_slice




"""
Game UI (pygame)
"""
tileSize = 80
tileWidth = 60 #pixels
tileHeight = 40
mapWidth = noteParser.numNotes
mapHeight = 15
KEYS = [0] * 24
PRESSED = 1

WHITE = (255, 255, 255)
GRAY = (220,220,220)
BLACK = (0, 0, 0)
GOLD = (255, 215,0)
GREEN = (127,255,0)
RED = (255, 0, 0)

keyDict = {'q':0, 'w':1, 'e':2, }

controller = Leap.Controller()
pkeys = piano_key.create_piano_keys()
piano = piano_fingers.PianoFingers(controller, pkeys)

history = [False] * 24

SF2 = 'GeneralUser.sf2'
if not fluidsynth.init(SF2):
    print "Couldn't load soundfont", SF2
    sys.exit(1)

def getColor(val):
    if val is False:
        return WHITE
    if val is True:
        return GRAY
    if val is 0:
        return BLACK
    if val is PRESSED:
        return GOLD
    if val == "green":
        return GREEN
    if val == "red":
        return RED

def process_events(keyslice):
    """
    this function handles keypresses and executes various other functions like
    sound, pygame stuff, and history when a key is pressed

    Note: this function is terribly written, we understand. It's a hackathon, and it does work.
    """

    keypressed, keyunpressed = piano.on_frame()
    k = keypressed
    if (k[0] == True or k[1] == True) and history[0] == False:
        KEYS[0] = 1
        keyslice.notesActive[0] = True
        fluidsynth.play_Note(Note("F-3"))
        history[0] = True
    if k[2] == True and history[1] == False:
        KEYS[1] = 1
        keyslice.notesActive[1] = True
        fluidsynth.play_Note(Note("F#-3"))
        history[1] = True
    if (k[3] == True or k[4] == True) and history[2] == False:
        KEYS[2] = 1
        keyslice.notesActive[2] = True
        fluidsynth.play_Note(Note("G-3"))
        history[2] = True

    if k[5] == True and history[3] == False:
        KEYS[3] = 1
        keyslice.notesActive[3] = True
        fluidsynth.play_Note(Note("G#-3"))
        history[3] = True
    if (k[6] == True or k[7] == True) and history[4] == False:
        KEYS[4] = 1
        keyslice.notesActive[4] = True
        fluidsynth.play_Note(Note("A-3"))
        history[4] = True

    if k[8] == True and history[5] == False:
        KEYS[5] = 1
        keyslice.notesActive[5] = True
        fluidsynth.play_Note(Note("A#-3"))
        history[5] = True

    if (k[9] == True or k[10] == True) and history[6] == False:
        KEYS[6] = 1
        keyslice.notesActive[6] = True
        fluidsynth.play_Note(Note("B-3"))
        history[6] = True

    if (k[11] == True or k[12] == True) and history[7] == False:
        KEYS[7] = 1
        keyslice.notesActive[7] = True
        fluidsynth.play_Note(Note("C-4"))
        history[7] = True

    if k[13] == True and history[8] == False:
        KEYS[8] = 1
        keyslice.notesActive[8] = True
        fluidsynth.play_Note(Note("C#-4"))
        history[8] = True

    if (k[14] == True or k[15] == True) and history[9] == False:
        KEYS[9] = 1
        keyslice.notesActive[9] = True
        fluidsynth.play_Note(Note("D-4"))
        history[9] = True

    if k[16] == True and history[10] == False:
        KEYS[10] = 1
        keyslice.notesActive[10] = True
        fluidsynth.play_Note(Note("D#-4"))
        history[10] = True

    if (k[17] == True or k[18] == True) and history[11] == False:
        KEYS[11] = 1
        keyslice.notesActive[11] = True
        fluidsynth.play_Note(Note("E-4"))
        history[11] = True

    if (k[19] == True or k[20] == True) and history[12] == False:
        KEYS[12] = 1
        keyslice.notesActive[12] = True
        fluidsynth.play_Note(Note("F-4"))
        history[12] = True
    if k[21] == True and history[13] == False:
        KEYS[13] = 1
        keyslice.notesActive[13] = True
        fluidsynth.play_Note(Note("F#-4"))
        history[13] = True

    if (k[22] == True or k[23] == True )and history[14] == False:
        KEYS[14] = 1
        keyslice.notesActive[14] = True
        fluidsynth.play_Note(Note("G-4"))
        history[14] = True

    if k[24] == True and history[15] == False:
        KEYS[15] = 1
        keyslice.notesActive[15] = True
        fluidsynth.play_Note(Note("G#-4"))
        history[15] = True

    if( k[25] == True or k[26] == True) and history[16] == False:
        KEYS[16] = 1
        keyslice.notesActive[16] = True
        fluidsynth.play_Note(Note("A-4"))
        history[16] = True
    if k[27] == True and history[17] == False:
        KEYS[17] = 1
        keyslice.notesActive[17] = True
        fluidsynth.play_Note(Note("A#-4"))
        history[17] = True
    if (k[28] == True or k[29] == True )and history[18] == False:
        KEYS[18] = 1
        keyslice.notesActive[18] = True
        fluidsynth.play_Note(Note("B-4"))
        history[18] = True
    if (k[30] == True or k[31] == True) and history[19] == False:
        KEYS[19] = 1
        keyslice.notesActive[19] = True
        fluidsynth.play_Note(Note("C-5"))
        history[19] = True
    if k[32] == True and history[20] == False:
        KEYS[20] = 1
        keyslice.notesActive[20] = True
        fluidsynth.play_Note(Note("C#-5"))
        history[20] = True
    if (k[33] == True or k[34] == True) and history[21] == False:
        KEYS[21] = 1
        keyslice.notesActive[21] = True
        fluidsynth.play_Note(Note("D-5"))
        history[21] = True
    if k[35] == True and history[22] == False:
        KEYS[22] = 1
        keyslice.notesActive[22] = True
        fluidsynth.play_Note(Note("D#-5"))
        history[22] = True
    if (k[36] == True or k[37] == True) and history[23] == False:
        KEYS[23] = 1
        keyslice.notesActive[23] = True
        fluidsynth.play_Note(Note("E-5"))
        history[23] = True






    k = keyunpressed
    if k[0] == True and k[1] == True:
        KEYS[0] = 0
        keyslice.notesActive[0] = False
        fluidsynth.stop_Note(Note("F-3"))
        history[0] = False
    if k[2] == True:
        KEYS[1] = 0
        keyslice.notesActive[1] = False
        fluidsynth.stop_Note(Note("F#-3"))
        history[1] = False
    if k[3] == True and k[4] == True:
        KEYS[2] = 0
        keyslice.notesActive[2] = False
        fluidsynth.stop_Note(Note("G-3"))
        history[2] = False
    if k[5] == True:
        KEYS[3] = 0
        keyslice.notesActive[3] = False
        fluidsynth.stop_Note(Note("G#-3"))
        history[3] = False
    if k[6] == True and k[7] == True:
        KEYS[4] = 0
        keyslice.notesActive[4] = False
        fluidsynth.stop_Note(Note("A-3"))
        history[4] = False
    if k[8] == True:
        KEYS[5] = 0
        keyslice.notesActive[5] = False
        fluidsynth.stop_Note(Note("A#-3"))
        history[5] = False
    if k[9] == True and k[10] == True:
        KEYS[6] = 0
        keyslice.notesActive[6] = False
        fluidsynth.stop_Note(Note("B-3"))
        history[6] = False
    if k[11] == True and k[12] == True:
        KEYS[7] = 0
        keyslice.notesActive[7] = False
        fluidsynth.stop_Note(Note("C-4"))
        history[7] = False
    if k[13] == True:
        KEYS[8] = 0
        keyslice.notesActive[8] = False
        fluidsynth.stop_Note(Note("C#-4"))
        history[8] = False
    if k[14] == True and k[15] == True:
        KEYS[9] = 0
        keyslice.notesActive[9] = False
        fluidsynth.stop_Note(Note("D-4"))
        history[9] = False
    if k[16] == True:
        KEYS[10] = 0
        keyslice.notesActive[10] = False
        fluidsynth.stop_Note(Note("D#-4"))
        history[10] = False
    if k[17] == True and k[18] == True:
        KEYS[11] = 0
        keyslice.notesActive[11] = False
        fluidsynth.stop_Note(Note("E-4"))
        history[11] = False
    if k[19] == True and k[20] == True:
        KEYS[12] = 0
        keyslice.notesActive[12] = False
        fluidsynth.stop_Note(Note("F-4"))
        history[12] = False
    if k[21] == True:
        KEYS[13] = 0
        keyslice.notesActive[13] = False
        fluidsynth.stop_Note(Note("F#-4"))
        history[13] = False
    if k[22] == True and k[23] == True:
        KEYS[14] = 0
        keyslice.notesActive[14] = False
        fluidsynth.stop_Note(Note("G-4"))
        history[14] = False
    if k[24] == True:
        KEYS[15] = 0
        keyslice.notesActive[15] = False
        fluidsynth.stop_Note(Note("G#-4"))
        history[15] = False
    if k[25] == True and k[26] == True:
        KEYS[16] = 0
        keyslice.notesActive[16] = False
        fluidsynth.stop_Note(Note("A-4"))
        history[16] = False
    if k[27] == True:
        KEYS[17] = 0
        keyslice.notesActive[17] = False
        fluidsynth.stop_Note(Note("A#-4"))
        history[17] = False
    if k[28] == True and k[29] == True:
        KEYS[18] = 0
        keyslice.notesActive[18] = False
        fluidsynth.stop_Note(Note("B-4"))
        history[18] = False
    if k[30] == True and k[31] == True:
        KEYS[19] = 0
        keyslice.notesActive[19] = False
        fluidsynth.stop_Note(Note("C-5"))
        history[19] = False
    if k[32] == True:
        KEYS[20] = 0
        keyslice.notesActive[20] = False
        fluidsynth.stop_Note(Note("C#-5"))
        history[20] = False
    if k[33] == True and k[34] == True:
        KEYS[21] = 0
        keyslice.notesActive[21] = False
        fluidsynth.stop_Note(Note("D-5"))
        history[21] = False
    if k[35] == True:
        KEYS[22] = 0
        keyslice.notesActive[22] = False
        fluidsynth.stop_Note(Note("D#-5"))
        history[22] = False
    if k[36] == True and k[37] == True:
        KEYS[23] = 0
        keyslice.notesActive[23] = False
        fluidsynth.stop_Note(Note("E-5"))
        history[23] = False


    return keyslice


if __name__ == "__main__":

    """
    the pygame stuff was unfortunately never fully integrated with the Leap Motion to create a cohesive game,
    thus for the pygame portion has been commented out to allow full functionality for the Leap Motion Piano.
    """

    # pygame.init()
    # pygame.font.init()
    # font = pygame.font.Font('Korean_Calligraphy.ttf', 40)
    # screen = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileHeight))
    test = TimeSliceMatrix()
    letters = ["F", "Gb", "G", "Ab", "A", "Bb", "B", 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab',
     'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E']

    ready = raw_input("Are you ready?\n")

    if ready == 'y':
        while True:
            test.getCurrentFrame()
            # for row in range(mapHeight):
            #     for column in range(mapWidth):
            #         color = getColor(test.song.data[row].notesActive[column])
            #         pygame.draw.rect(screen, color,(column*tileSize, row*tileHeight, tileSize, tileHeight))
            #         for i in range(24):
            #             screen.blit(font.render(letters[i],False, (255,255,255)), (10 + i * 60, -5))
            time.sleep(.1)
            # current_time += .25

            # pygame.display.update()
