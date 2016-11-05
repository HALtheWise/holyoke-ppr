import pygame, sys
from pygame.locals import *
import noteParser
import time

"""
Game logic - the general game running
"""
current_time = 0.
timeSlice = .25 #each slice of time that contains true false for each note
timeFrame = 1.0 #Notes will show up on screen 2 seconds before playtime.


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
        self.song = noteParser.getTestSong()
        self.timeSlice_index = len(self.song.data)
        #w, h = noteParser.numNotes, total_rows
        #Matrix = [[0 for x in range(w)] for y in range(h)]

    def getCurrentFrame(self):
        self.song = noteParser.getTestSong()
        time_index = int(current_time/timeSlice)
        if time_index + 4 <= len(self.song.data):
            self.song.data = self.song.data[time_index : time_index + self.total_rows]
            base_slice = noteParser.TimeSlice()
            base_slice.notesActive = [BASE] * noteParser.numNotes
            self.song.data = [base_slice] + self.song.data



"""
Game UI (pygame)
"""
tileSize = 80 #40 pixels
mapWidth = noteParser.numNotes
mapHeight = 5
BASE = 0

WHITE = (255, 255, 255)
PINK = (255, 20, 147)
BLACK = (0, 0, 0)

def getColor(val):
    if val is False:
        return WHITE
    if val is True:
        return PINK
    if val is BASE:
        return BLACK


if __name__ == "__main__":
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileSize))
    test = TimeSliceMatrix()
    for row in range(mapHeight):
        for column in range(mapWidth):
            color = getColor(test.song.data[row].notesActive[column])
            pygame.draw.rect(DISPLAYSURF, color,(column*tileSize, row*tileSize, tileSize, tileSize))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        test.getCurrentFrame()
        for row in range(mapHeight):
            for column in range(mapWidth):
                color = getColor(test.song.data[row].notesActive[column])
                pygame.draw.rect(DISPLAYSURF, color,(column*tileSize, row*tileSize, tileSize, tileSize))
        time.sleep(1)
        current_time += .25

        pygame.display.update()
