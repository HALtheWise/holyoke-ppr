#Fun facts from Kimber: How to make a noise!!!! 11/5/16

#
# from mingus.midi import fluidsynth
# from mingus.containers import Note
# import mingus.core.notes as notes
# import time
#
# fluidsynth.init('GeneralUser.sf2')
#
# # fluidsynth.play_Note(64,1,100)
# # fluidsynth.play_Note(10,0,100)
# # fluidsynth.set_instrument(1,14)
# # n = Note("C")
# # n.channel = 5
# # n.velocity = 50
# print notes.is_valid_note("C")
# print fluidsynth.play_Note(Note("D"))



from mingus.core import progressions, intervals
from mingus.core import chords as ch
from mingus.containers import NoteContainer, Note
from mingus.midi import fluidsynth
import mingus.core.notes as notes
from random import random

import time

SF2 = 'GeneralUser.sf2'
if not fluidsynth.init(SF2):
    print "Couldn't load soundfont", SF2
    sys.exit(1)
# progression = [
#     'I',
#     'vi',
#     'ii',
#     'iii7',
#     'I7',
#     'viidom7',
#     'iii7',
#     'V7',
#     ]
# key = 'C'
# chords = progressions.to_chords(progression, key)

# while 1:
    # i = 0
    # for chord in chords:
        # c = NoteContainer(chords[i])
        # l = Note(c[0].name)
        # p = c[1]
        # l.octave_down()
        # print ch.determine(chords[i])[0]
fluidsynth.play_Note(Note(("C#-3")))
time.sleep(1)        # Play chord and lowered first note

        # fluidsynth.play_NoteContainer(c)


        # Play highest note in chord

        # fluidsynth.play_Note(c[-1])

        # 50% chance on a bass note

        # if random() > 0.50:
        #     p = Note(c[1].name)
        #     p.octave_down()
        #     fluidsynth.play_Note(p)
        # time.sleep(0.50)
        #
        # # 50% chance on a ninth
        #
        # if random() > 0.50:
        #     l = Note(intervals.second(c[0].name, key))
        #     l.octave_up()
        #     fluidsynth.play_Note(l)
        # time.sleep(0.25)
        #
        # # 50% chance on the second highest note
        #
        # if random() > 0.50:
        #     fluidsynth.play_Note(c[-2])
        # time.sleep(0.25)
        # # fluidsynth.stop_NoteContainer(c)
        # fluidsynth.stop_Note(p)
        # i += 1
    # print '-' * 20
