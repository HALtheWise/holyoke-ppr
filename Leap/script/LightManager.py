#!/usr/bin/env python2

import urllib2
import time
import threading


class Color():
	"""docstring for Color"""
	r = 0
	g = 0
	b = 0
	def __init__(self, r=0, g=0, b=0):
		self.r = r
		self.g = g
		self.b = b
		
	def toHex(self):
		return '{:02x}{:02x}{:02x}'.format(int(self.r), int(self.g), int(self.b))

class Lights():
	"""docstring for Lights"""
	ip=''

	color=Color(0)

	lastUpdate = 0

	def __init__(self, ip='192.168.4.1'):
		self.ip = ip
		self.lastUpdate = time.time()
	
	def makeRequest(self, colorstring):
		url = 'http://{}/cc?pixels={}'.format(self.ip, colorstring)
		# print 'url={}'.format(url)
		try:
			urllib2.urlopen(url, timeout=1).read()
		except Exception as e:
			pass

	def sendColor(self):
		colorstring1 = self.color.toHex()
		off = '000000'
		row = off*4 + colorstring1

		colorstring = row * 7
		self.makeRequest(colorstring)

	def regressTo(self, c = Color(), decayRate = 4):
		dt = time.time() - self.lastUpdate
		dt = min(dt, .5)

		self.color = averageColors(self.color, c, decayRate * dt)
		self.lastUpdate = time.time()


def averageColors(a, b, w):
	""" weight 0 returns a, 1 returns b """
	r = (1-w)*a.r + w * b.r
	g = (1-w)*a.g + w * b.g
	b = (1-w)*a.b + w * b.b
	return Color(r, g, b)

d = Lights()

def pulse(color = Color(r=255, g=255,b=255)):
	d.color = color

def run():
	d.color=regressColor
	while True:
		d.regressTo(regressColor)
		d.sendColor()
		time.sleep(.01)

def start(color = Color(0,0,255)):
	global regressColor
	regressColor = color
	global thread
	thread = threading.Thread(target = run)
	thread.setDaemon(True)
	thread.start()

def stop():
	thread.stop()

start()