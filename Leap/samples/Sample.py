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

# class SampleListener(Leap.Listener):
finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

def on_connect(controller):
    print "Connected"

    # Enable gestures
    controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
    controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
    controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

def on_frame(controller):
    # Get the most recent frame and report some basic information
    frame = controller.frame()

    print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
          frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

    # Get hands
    for hand in frame.hands:

        handType = "Left hand" if hand.is_left else "Right hand"

        print "  %s, id %d, position: %s" % (
            handType, hand.id, hand.palm_position)

        # Get the hand's normal vector and direction
        normal = hand.palm_normal
        direction = hand.direction

        # Calculate the hand's pitch, roll, and yaw angles
        print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            direction.pitch * Leap.RAD_TO_DEG,
            normal.roll * Leap.RAD_TO_DEG,
            direction.yaw * Leap.RAD_TO_DEG)

        # Get arm bone
        arm = hand.arm
        print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
            arm.direction,
            arm.wrist_position,
            arm.elbow_position)

        # Get fingers
        for finger in hand.fingers:

            print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                finger_names[finger.type],
                finger.id,
                finger.length,
                finger.width)

            # Get bones
            for b in range(0, 4):
                bone = finger.bone(b)
                print "      Bone: %s, start: %s, end: %s, direction: %s" % (
                    bone_names[bone.type],
                    bone.prev_joint,
                    bone.next_joint,
                    bone.direction)

    # Get tools
    for tool in frame.tools:

        print "  Tool id: %d, position: %s, direction: %s" % (
            tool.id, tool.tip_position, tool.direction)

    # Get gestures
    for gesture in frame.gestures():
        if gesture.type == Leap.Gesture.TYPE_CIRCLE:
            circle = CircleGesture(gesture)

            # Determine clock direction using the angle between the pointable and the circle normal
            if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                clockwiseness = "clockwise"
            else:
                clockwiseness = "counterclockwise"

            # Calculate the angle swept since the last frame
            swept_angle = 0
            if circle.state != Leap.Gesture.STATE_START:
                previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

            print "  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
                    gesture.id, state_names[gesture.state],
                    circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)

        if gesture.type == Leap.Gesture.TYPE_SWIPE:
            swipe = SwipeGesture(gesture)
            print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                    gesture.id, state_names[gesture.state],
                    swipe.position, swipe.direction, swipe.speed)

        if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
            keytap = KeyTapGesture(gesture)
            print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                    gesture.id, state_names[gesture.state],
                    keytap.position, keytap.direction )

        if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
            screentap = ScreenTapGesture(gesture)
            print "  Screen Tap id: %d, %s, position: %s, direction: %s" % (
                    gesture.id, state_names[gesture.state],
                    screentap.position, screentap.direction )

    if not (frame.hands.is_empty and frame.gestures().is_empty):
        print ""

def state_string(state):
    if state == Leap.Gesture.STATE_START:
        return "STATE_START"

    if state == Leap.Gesture.STATE_UPDATE:
        return "STATE_UPDATE"

    if state == Leap.Gesture.STATE_STOP:
        return "STATE_STOP"

    if state == Leap.Gesture.STATE_INVALID:
        return "STATE_INVALID"

def main():

    # Create a controller
    controller = Leap.Controller()

    on_connect(controller)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        while 1:
            # sys.stdin.readline()
            on_frame(controller)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
