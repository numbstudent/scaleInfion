import serial
import time

nousb = 0
def run_conveyor():
    result = False
    for i in range(0,4):
        if not result:
            try:
                ser = serial.Serial('/dev/ttyUSB'+str(i), baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
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
                nousb = i
            except:
                result = False
    return result

# print(run_conveyor())
# print(nousb)
