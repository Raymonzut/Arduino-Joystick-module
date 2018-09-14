from Connect_v002 import Connection
from time import sleep
import re
import pyautogui


class Cursor(Connection):
    """Class that can move the cursor on your monitor, to inprove peformance, adjust the cursor_animation_time and the data_limit"""

    def __init__(self, baud=9600, com='COM4', cursor_speed=50, cursor_animation_time=0.007, cursor_data_minimum=0.06, cursor_data_maximum=0.94, data_limit=120):
        """Sets the required variables to be able to connect when start is called"""
        self.cursor_speed = cursor_speed
        self.cursor_animation_time = cursor_animation_time
        self.cursor_data_minimum = cursor_data_minimum
        self.cursor_data_maximum = cursor_data_maximum

        self.data_limit = data_limit

        Connection.__init__(self, baud=baud, com=com)

    def moveRel(self, x, y):
        """Moves the cursor accordingly"""
        pyautogui.moveRel(x * self.cursor_speed, y * self.cursor_speed, self.cursor_animation_time)

    def start(self):
        """This is called when you want to establish connection and when you want the cursor to be moved by the joystick"""
        self.connect()
        self.run()

    def run(self):
        """Will read and process the data, will stop when the pyautogui.FailSafeException is called, it is called when the cursor is at x=0 and y=0)"""
        try:
            while True:
                # Reads raw data, needs to be filtered
                data = self.read(data_limit=120)
                self.data_regex = '(-?\d.\d\d)(,)(-?\d.\d\d)'
                # Search
                result = re.search(self.data_regex, str(data))
                x = float(result.group(1))
                y = float(result.group(3))
                # move the cursor

                if abs(x) < self.cursor_data_minimum:
                    x = 0
                elif abs(x) > self.cursor_data_maximum and x < 0:
                    x = -1
                elif abs(x) > self.cursor_data_maximum and x > 0:
                    x = 1

                if abs(y) < self.cursor_data_minimum:
                    y = 0
                elif abs(y) > self.cursor_data_maximum and y < 0:
                    y = -1
                elif abs(y) > self.cursor_data_maximum and y > 0:
                    y = 1

                self.moveRel(x,y)

                # print the data, not needed
                print(x,y)

        # Manual trigger
        except pyautogui.FailSafeException:
            print('Fail safe raised, stopping cursor')
            self.stop()


    def stop(self):
        """Will be called istead of the FailSafeException"""
        self.disconnect()

if __name__=='__main__':
    cursor = Cursor(baud=9600, com='COM3', data_limit=110)
    cursor.start()
