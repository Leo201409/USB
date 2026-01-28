import serial
import serial.tools.list_ports
import time


class MicrobitDriver:
    def __init__(self, baudrate=115200, timeout=1):
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        self.port = None

    def find_microbit(self):
        """Auto-detect micro:bit USB serial port"""
        ports = serial.tools.list_ports.comports()
        for p in ports:
            desc = (p.description or "").lower()
            hwid = (p.hwid or "").lower()

            if "microbit" in desc or "mbed" in desc or "vid:pid=0d28" in hwid:
                self.port = p.device
                return self.port

        raise RuntimeError("micro:bit not found (driver or cable issue)")

    def connect(self):
        """Open serial connection"""
        if not self.port:
            self.find_microbit()

        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout
        )

        # micro:bit resets on serial open
        time.sleep(2)

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

    def read_line(self):
        if not self.ser:
            raise RuntimeError("Not connected")
        line = self.ser.readline().decode("utf-8", errors="ignore").strip()
        return line

    def write(self, data):
        if not self.ser:
            raise RuntimeError("Not connected")
        if isinstance(data, str):
            data = data.encode("utf-8")
        self.ser.write(data + b"\n")

    def is_connected(self):
        return self.ser is not None and self.ser.is_open
