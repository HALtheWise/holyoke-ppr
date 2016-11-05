#Fun facts from Kimber: How to make a noise!!!! 11/5/16


from mingus.midi import fluidsynth
fluidsynth.init('/usr/share/sounds/sf2/FluidR3_GM.sf2',"alsa")

fluidsynth.play_Note(64,0,100)