import serial

def run_conveyor():
    try:
        ser = serial.Serial('/dev/ttyUSB3', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        msg = bytearray()

        # Change this
        msg.append(0x41)

        msg.append(0xD)
        ser.write(msg)
        ser.close()
        return True
    except:
        return False