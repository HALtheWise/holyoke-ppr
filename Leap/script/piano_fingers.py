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

class PianoFingers:
    def __init__(self, controller):
        self.pressed = 50
        self.controller = controller
        self.finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
        self.bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']


    def on_frame(self):
        # Get the most recent frame and report some basic information
        frame = self.controller.frame()

        # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
            #   frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            # print "  %s, position: %s" % (
                # handType, hand.palm_position)

            # Get the hand's normal vector and direction
            # normal = hand.palm_normal
            # direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            # print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #     direction.pitch * Leap.RAD_TO_DEG,
            #     normal.roll * Leap.RAD_TO_DEG,
            #     direction.yaw * Leap.RAD_TO_DEG)

            # Get arm bone
            arm = hand.arm
            # print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
            #     arm.direction,
            #     arm.wrist_position,
            #     arm.elbow_position)

            # Get fingers
            for finger in hand.fingers:

                # print "    %s finger" % (self.finger_names[finger.type])

                # Get bone
                bone = finger.bone(3)
                # print "      Bone: %s, end: %s" % (
                    # self.bone_names[bone.type],
                    # bone.next_joint)

                self.if_pressed(bone)



        if not (frame.hands.is_empty):
            print ""




    def if_pressed(self, bone):

        if bone.next_joint.y < self.pressed:
            



def main():

    # Create a controller
    controller = Leap.Controller()

    piano = PianoFingers(controller)


    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        while 1:
            # sys.stdin.readline()
            piano.on_frame()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
