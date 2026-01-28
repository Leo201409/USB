import serial

# Windows example:
# port = "COM3"

# Linux / Android / Mac:
# port = "/dev/ttyACM0"

ser = serial.Serial(port="COM3", baudrate=115200, timeout=1)

while True:
    line = ser.readline().decode("utf-8").strip()
    if line:
        print("micro:bit says:", line)
