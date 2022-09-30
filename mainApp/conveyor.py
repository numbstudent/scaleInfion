import serial
import time

def run_conveyor():
    try:
        ser = serial.Serial('/dev/relay', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        msg = bytearray()

        msg.append(0x41)
        msg.append(0xD)
        ser.write(msg)
        time.sleep(2)
        msg.append(0x42)
        msg.append(0xD)
        ser.write(msg)
        ser.close()
        result = True
    except:
        result = False
    return result

def debug_conveyor():
    ser = serial.Serial('/dev/relay', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    msg = bytearray()

    msg.append(0x41)
    msg.append(0xD)
    ser.write(msg)
    time.sleep(2)
    msg.append(0x42)
    msg.append(0xD)
    ser.write(msg)
    ser.close()
    result = True
