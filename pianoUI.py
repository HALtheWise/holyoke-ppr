import pygame, sys
from pygame.locals import *
import noteParser
import time

"""
Game logic - the general game running
"""
current_time = 0.
previous_time = 0.
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

    def getNormalFrame(self):
        self.song =  noteParser.getMIDISong()
        time_index = int(current_time/timeSlice)
        if time_index + self.total_rows <= len(self.song.data):
            self.song.data = self.song.data[time_index : time_index + self.total_rows]
            base_slice = noteParser.TimeSlice()

            base_slice.notesActive = [0] * noteParser.numNotes
            self.song.data = [base_slice] + self.song.data

        else:
            sys.exit()




"""
Game UI (pygame)
"""
tileSize = 80
tileWidth = 80 #pixels
tileHeight = 40
mapWidth = noteParser.numNotes
mapHeight = 15
KEYS = [0] * 20
PRESSED = 1

WHITE = (255, 255, 255)
GRAY = (220,220,220)
BLACK = (0, 0, 0)
GOLD = (255, 215,0)
GREEN = (127,255,0)
RED = (255, 0, 0)

keyDict = {'q':0, 'w':1, 'e':2, }

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

    pygame.event.pump
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            k = event.key
            if k == pygame.K_1:
                print "1"
                KEYS[0] = 1
                keyslice.notesActive[0] = True
            if k == pygame.K_2:
                print "2"
                KEYS[1] = 1
                keyslice.notesActive[1] = True
            if k == pygame.K_3:
                print "3"
                KEYS[2] = 1
                keyslice.notesActive[2] = True
            if k == pygame.K_4:
                print "4"
                KEYS[3] = 1
                keyslice.notesActive[3] = True
            if k == pygame.K_5:
                print "5"
                KEYS[4] = 1
                keyslice.notesActive[4] = True
            if k == pygame.K_6:
                print "6"
                KEYS[5] = 1
                keyslice.notesActive[5] = True
            if k == pygame.K_7:
                print "7"
                KEYS[6] = 1
                keyslice.notesActive[6] = True
            if k == pygame.K_8:
                print "8"
                KEYS[7] = 1
                keyslice.notesActive[7] = True
            if k == pygame.K_9:
                print "9"
                KEYS[8] = 1
                keyslice.notesActive[8] = True
            if k == pygame.K_0:
                print "0"
                KEYS[9] = 1
                keyslice.notesActive[9] = True

        elif event.type == pygame.KEYUP:
            k = event.key
            if k == pygame.K_1:
                KEYS[0] = 0
                keyslice.notesActive[0] = False
            if k == pygame.K_2:
                KEYS[1] = 0
                keyslice.notesActive[1] = False
            if k == pygame.K_3:
                KEYS[2] = 0
                keyslice.notesActive[2] = False
            if k == pygame.K_4:
                KEYS[3] = 0
                keyslice.notesActive[3] = False
            if k == pygame.K_5:
                KEYS[4] = 0
                keyslice.notesActive[4] = False
            if k == pygame.K_6:
                KEYS[5] = 0
                keyslice.notesActive[5] = False
            if k == pygame.K_7:
                KEYS[6] = 0
                keyslice.notesActive[6] = False
            if k == pygame.K_8:
                KEYS[7] = 0
                keyslice.notesActive[7] = False
            if k == pygame.K_9:
                KEYS[8] = 0
                keyslice.notesActive[8] = False
            if k == pygame.K_0:
                KEYS[9] = 0
                keyslice.notesActive[9] = False

    return keyslice


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('Korean_Calligraphy.ttf', 50)
    screen = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileHeight))
    test = TimeSliceMatrix()


    while True:
        if (time.clock() - previous_time) >= timeSlice/3:
            test.getNormalFrame()
            current_time += .25
            previous_time = time.clock()
        test.getCurrentFrame()
        for row in range(mapHeight): #Draw will update constantly, frame will not.
            for column in range(mapWidth):
                color = getColor(test.song.data[row].notesActive[column])
                pygame.draw.rect(screen, color,(column*tileSize, row*tileHeight, tileSize, tileHeight))
                for i in range(10):
                    screen.blit(font.render(str(i+1),False, (255,255,255)), (10 + i * 80, -5))

            pygame.display.update()
