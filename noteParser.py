#!/usr/bin/env python2
"""
This file attempts to parse and output a list of notes in a song. Initially,
that will be read from a .midi file, with eventual extensions to audio files hoped.
Maintainer: Eric
"""

from mido import MidiFile

import math

numNotes = 20

class TimeSlice():
	"""docstring for TimeSlice"""
	notesActive = []

	def __init__(self, singleNote = None):
		self.notesActive = [False] * numNotes

		if singleNote is not None:
			self.setNote(singleNote, True)

	def setNote(self, noteID, value):
		self.notesActive[noteID] = bool(value)

	def __str__(self):
		return '<{}>'.format(str(self.notesActive))

	__repr__ = __str__


class Song():
	"""docstring for Song"""
	dt = 0.25
	data = []

	def __init__(self, data):
		self.data = data

	def __str__(self):
		result = []

		chars = {False:'-', True:'x'}
		result.append('note:\t\t{}'.format('\t'.join(map(str,range(numNotes)))))
		for i, time in enumerate(self.data):
			result.append("t={}\t\t{}".format(i * self.dt,
				'\t'.join([chars[x] for x in time.notesActive])))

		return '\n'.join(result)

	__repr__ = __str__


def getMIDISong(filename='test data/birthday-single.mid'):
	""" Code adapted from
	https://github.com/olemb/mido/blob/master/examples/midifiles/print_midi_file.py"""

	midi = MidiFile(filename)

	global track
	track = getMainTrack(midi)

	notes = []

	elapsedtime = 0

	for i, msg in enumerate(track):
		elapsedtime += msg.time

		if msg.type == 'note_on':
			notes.append((elapsedtime, msg.note, findNoteDuration(track, msg.note, i+1)))

	return notesToSong(notes)


def notesToSong(notes, dt = 0.25, midispeed = 96*4, baseID = 60):
	def convertNoteID(noteID):
		result = noteID - baseID
		if (result < 0):
			result = 0
		if (result >= numNotes):
			result = numNotes - 1
		return result

	def convertTime(time):
		return int(math.ceil(float(time)/midispeed/dt))

	duration = convertTime(notes[len(notes)-1][0] + notes[len(notes)-1][2])

	# Initialize timeslices
	bufferzone = 20;
	timeslices = [TimeSlice() for _ in xrange(duration + bufferzone)]

	# Populate timeslices
	for note in notes:
		for i in xrange(convertTime(note[0]), convertTime(note[0]+note[2])):
			timeslices[i].setNote(convertNoteID(note[1]), True)

	song = Song(timeslices)
	song.dt = dt
	return song


def findNoteDuration(track, noteID, startpos):
	""" Finds the duration until note_off is called on noteID, starting search at startpos """
	elapsedtime = 0
	i = startpos
	while i < len(track):
		msg = track[i]
		elapsedtime += msg.time

		if msg.type == 'note_off' and msg.note == noteID:
			return elapsedtime

		i += 1

def printTrack(track):
	print '=== Track length {}\n'.format(len(track))
	for message in track:
		print '  {!r}\n'.format(message)

def getMainTrack(midi):
	return max(midi.tracks, key=len)

def getTestSong():
	song = Song([
		TimeSlice(),
		TimeSlice(1),
		TimeSlice(1),
		TimeSlice(2),
		TimeSlice(3),
		TimeSlice(),
		TimeSlice(4),
		TimeSlice(4),
		TimeSlice(5)
		])

	return song

if __name__ == '__main__':
	print getMIDISong()
