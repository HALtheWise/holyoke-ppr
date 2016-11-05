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
        time_index = int(current_time/timeSlice)
        if time_index + 7 <= len(song):
            self.song = self.song[time_index : time_index + total_rows]
            base = ([BASE, BASE, BASE, BASE, BASE, BASE ,BASE ,BASE])
            self.song = base + self.song







"""
Game UI (pygame)
"""
tileSize = 80 #40 pixels
mapWidth = 8
mapHeight = 5
BASE = 0

WHITE = (255, 255, 255)
PINK = (255, 20, 147)
BLACK = (0, 0, 0)

color = {
            True : PINK,
            False : WHITE,
            BASE : BLACK
          }


if __name__ == "__main__":
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileSize))
    test = TimeSliceMatrix()
    test.getCurrentFrame

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for row in range(mapHeight):
            for column in range(mapWidth):
                pygame.draw.rect(DISPLAYSURF, color[test.song.data[row].notesActive[column]], \
                (column*tileSize, row*tileSize, tileSize, tileSize))

        pygame.display.update()
