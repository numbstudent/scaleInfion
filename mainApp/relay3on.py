import serial
import time

def relay3_on():
    try:
        ser = serial.Serial('/dev/relay', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        msg = bytearray()

        msg.append(0x45)
        msg.append(0xD)
        ser.write(msg)
        ser.close()

        result = True
    except:
        result = False
    return result

def debug_relay_on():
    ser = serial.Serial('/dev/relay', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    msg = bytearray()

    msg.append(0x45)
    msg.append(0xD)
    ser.write(msg)
    ser.close()

    result = True
