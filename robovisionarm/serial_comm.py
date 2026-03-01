import serial

class ArduinoController:

    def __init__(self, port="COM3", baudrate=115200, debug=False):

        self.debug = debug
        self.ser = None

        if not debug:

            try:
                self.ser = serial.Serial(port, baudrate, timeout=1)
                print(f"Connected to Arduino on {port}")

            except Exception as e:

                print("Serial failed → Debug mode:", e)
                self.debug = True


    def send_angles(self, angles):

        if self.debug:

            print("DEBUG ANGLES:", angles)
            return

        self.ser.write(bytearray([int(a) for a in angles]))


    def close(self):

        if self.ser:
            self.ser.close()