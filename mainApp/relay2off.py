import serial
import time

def relay_off():
    try:
        ser = serial.Serial('/dev/relay', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        msg = bytearray()

        msg.append(0x44)
        msg.append(0xD)
        ser.write(msg)
        ser.close()

        result = True
    except:
        result = False
    return 
    
def debug_relay_off():
    ser = serial.Serial('/dev/relay', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    msg = bytearray()

    msg.append(0x44)
    msg.append(0xD)
    ser.write(msg)
    ser.close()

    result = True