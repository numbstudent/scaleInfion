import serial

def run_conveyor():
    # try:
    ser = serial.Serial('/dev/ttyUSB3', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    msg = bytearray()
    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

    msg.append(0x41)
    msg.append(0xD)
    ser.write(msg)
    time.sleep(2)
    msg.append(0x42)
    msg.append(0xD)
    ser.write(msg)
    ser.close()

    # return True
    # except:
    #     return False