import cv2
import mediapipe as mp
import time

from .serial_comm import ArduinoController
from .config import HOME_POSITION


class RoboVisionArm:

    def __init__(

        self,
        port="COM3",
        camera_index=0,
        debug=False
    ):

        self.arduino = ArduinoController(port, debug=debug)

        self.cap = cv2.VideoCapture(camera_index)

        self.current_angles = HOME_POSITION.copy()

        self.mp_hands = mp.solutions.hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )


    def compute_angles(self, hand):

        wrist = hand.landmark[0]

        base = int(wrist.x * 180)

        shoulder = int(wrist.y * 180)

        elbow = 90

        wrist_rot = 60

        gripper = 90

        return [

            base,
            shoulder,
            elbow,
            wrist_rot,
            gripper
        ]


    def step(self):

        success, frame = self.cap.read()

        if not success:
            return True

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.mp_hands.process(rgb)

        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]

            angles = self.compute_angles(hand)

            self.current_angles = angles

            self.arduino.send_angles(angles)

        cv2.imshow("RoboVisionArm", frame)

        if cv2.waitKey(1) == 27:
            return False

        return True


    def run(self):

        print("Starting RoboVisionArm...")

        while True:

            if not self.step():
                break

        self.shutdown()


    def shutdown(self):

        print("Shutting down")

        self.cap.release()

        self.arduino.close()

        cv2.destroyAllWindows()