#!/usr/bin/env python2
"""
This file attempts to parse and output a list of notes in a song. Initially,
that will be read from a .midi file, with eventual extensions to audio files hoped.
Maintainer: Eric
"""

numNotes = 8

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
	print getTestSong()