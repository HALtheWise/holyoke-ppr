# ###############################################################################
# HackHolyoke - PianoPianoRevolution                                            #
# Leap Motion Codebase that deals with handling finger presses to               #
# emulate piano key presses                                                     #
#                                                                               #
# Created by Kevin Zhang and Kimberly Winter                                    #
# ###############################################################################
import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
lib_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, lib_dir)

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

import piano_key

class PianoFingers:
    def __init__(self, controller, pkeys):
        self.pressed = 205
        self.controller = controller
        self.pkeys = pkeys
        self.finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
        self.bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
        self.pressed_keys = [False] * 38
        self.unpressed_keys = [False] * 38


    def on_frame(self):

        # Get the most recent frame and report some basic information
        frame = self.controller.frame()


        # Get key presses
        self.pressed_keys = [False] * 38
        self.unpressed_keys = [False] * 38

        #Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            print "  %s, position: %s" % (
                handType, hand.palm_position)


            arm = hand.arm

            # Get fingers
            for finger in hand.fingers:


                # Get distal bone (the end of each finger)
                bone = finger.bone(3)
                # print "      Bone: %s, end: %s" % (self.bone_names[bone.type], bone.next_joint)

                self.if_pressed(bone)


        if not (frame.hands.is_empty):
            print ""


        return self.pressed_keys, self.unpressed_keys


    def if_pressed(self, bone):

        if bone.next_joint.y < self.pressed:
            for i in range(len(self.pkeys)):
                if self.pkeys[i].is_pressed(bone):
                    self.pressed_keys[i] = True
        self.unpressed_keys = [not item for item in self.pressed_keys]









def main():

    # Create a controller
    controller = Leap.Controller()

    pkeys = piano_key.create_piano_keys()


    piano = PianoFingers(controller, pkeys)



    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        while 1:
            piano.on_frame()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
