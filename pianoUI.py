import pygame, sys
from pygame.locals import *
import noteParser
import time

"""
Game logic - the general game running
"""
current_time = 0.
timeSlice = .25 #each slice of time that contains true false for each note
timeFrame = 2.0 #Notes will show up on screen 2 seconds before playtime.
comparisonSlice = 0 #The timeSlice to compare the current keypress with.
keySlice = 0 #The current keySlice, which is generated when a key is pressed.


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
        #w, h = noteParser.numNotes, total_rows
        #Matrix = [[0 for x in range(w)] for y in range(h)]

    def getCurrentFrame(self):
        self.song =  noteParser.getMIDISong()
        time_index = int(current_time/timeSlice)
        if time_index + self.total_rows <= len(self.song.data):
            comparisonSlice = self.song.data[time_index]
            compareSlice()
            self.song.data = self.song.data[time_index : time_index + self.total_rows]
            base_slice = noteParser.TimeSlice()
            #Enter a if key pressed here, change it to GOLD instead of base.
            base_slice.notesActive = [BASE] * noteParser.numNotes
            self.song.data = [base_slice] + self.song.data

    def compareSlice(self):
        #assuming that a keypress generates a timeslice.
        if keySlice == comparisonSlice: #If it matches up, transforms it to GREAT
            for i in comparisonSlice:
                if i is True:
                    i = GREAT
                    self.song.data[time_index] = comparisonSlice



"""
Game UI (pygame)
"""
tileSize = 80
tileWidth = 80 #pixels
tileHeight = 40
mapWidth = noteParser.numNotes
mapHeight = 9
BASE = 3
GREAT = 4

WHITE = (255, 255, 255)
PINK = (255, 20, 147)
BLACK = (0, 0, 0)
GOLD = (255, 215,0)
GREEN = (102, 255, 0)

keyDict = {'q':0, 'w':1, 'e':2, }

def getColor(val):
    if val is False:
        return WHITE
    if val is True:
        return PINK
    if val is BASE:
        return BLACK
    if val is GREAT:
        return GOLD


if __name__ == "__main__":
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileHeight))
    test = TimeSliceMatrix()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        test.getCurrentFrame() #Some kind of input to be determined later
        for row in range(mapHeight):
            for column in range(mapWidth):
                color = getColor(test.song.data[row].notesActive[column])
                pygame.draw.rect(DISPLAYSURF, color,(column*tileSize, row*tileHeight, tileSize, tileHeight))
        time.sleep(.25)
        current_time += .25

        pygame.display.update()
