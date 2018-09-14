from time import sleep
import serial

# Info: https://www.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html
# Info: https://playground.arduino.cc/interfacing/python
# Info: https://pyserial.readthedocs.io/en/latest/shortintro.html

# Info: https://arduinobasics.blogspot.com/2012/07/arduino-basics-simple-arduino-serial.html
class Connection:
    """Class that handles the connection with the arduino board, can read and write to the arduino"""

    def __init__(self, baud=9600, com='COM4'):
        """Sets up the connection"""
        self.baud = baud
        self.com = com
        self.serial = serial.Serial()
        self.serial.baudrate = self.baud
        self.serial.port = self.com
        sleep(2)
        print('Setup complete')

    def connect(self):
        """Connects on the selected baud rate and on the selected com, make sure that no other program is using this port,
        like the arduino IDE"""
        # Checks if serial is already open
        if not self.serial.is_open:
            print('Opening')
            self.serial.open()
            print('Opended')
            sleep(1)

    def disconnect(self):
        """Disconnects"""
        # Checks if serial is already open
        if self.serial.is_open:
            self.serial.close()


    def write(self, msg=b''):
        """Writes to the serial, message must be in bytes: b'' is used for this, or the str.encode() method"""
        self.serial.write(msg)

    def read(self, data_limit=10):
        """Returns the data on the serial connection, you can specify the data read size"""
        if self.serial.is_open:
            read_out = self.serial.read(data_limit)

            return read_out


if __name__ == '__main__':
    # Inits the connection, specify your COM here
    conn = Connection(com='COM5')


    while True:
        a = input()
        conn.connect()
        # str.encode returns the byte like object
        conn.write(a.encode())
        conn.disconnect()
