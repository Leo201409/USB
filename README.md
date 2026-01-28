# microbit-python-driver

A clean, user-space **Python driver layer** for communicating with a **BBC micro:bit** over **USB serial**.

This is **not** a kernel or OS driver. Instead, it is a **production-style Python abstraction** that behaves like a driver: it auto-detects the device, manages the serial connection, and provides a simple API for reading and writing data.

If you are building tools, games, experiments, or automation around a micro:bit, this is the correct and sane way to do it.

---

## ✨ Features

- Auto-detects micro:bit USB serial port  
- Cross-platform (Windows, Linux, macOS)  
- Handles micro:bit auto-reset on connection  
- Simple, clean API (`connect`, `read_line`, `write`)  
- Easy to extend into a full protocol or framework  

---

## 📦 Requirements

- Python **3.7+**
- `pyserial`
- BBC micro:bit (v1 or v2)
- **USB data cable** (not power-only)

Install dependency:

```bash
pip install pyserial
```

---

## 📁 Project Structure

```text
microbit-python-driver/
│
├── microbit_driver.py   # The driver layer
├── example.py           # Example usage (optional)
└── README.md            # This file
```

---

## 🚀 Quick Start

### 1️⃣ Flash the micro:bit (MicroPython)

Flash this code to your micro:bit:

```python
from microbit import *

while True:
    print("READY")
    sleep(1000)
```

This sends data over USB serial once per second.

---

### 2️⃣ Use the Python Driver

```python
from microbit_driver import MicrobitDriver

mb = MicrobitDriver()
mb.connect()

print("Connected to micro:bit")

while True:
    msg = mb.read_line()
    if msg:
        print("micro:bit >", msg)
```

---

## 🧠 How It Works

- The micro:bit appears as a **USB CDC serial device**
- This driver auto-detects it using USB descriptors
- Opening the serial port resets the micro:bit (normal behavior)
- Data is exchanged as UTF-8 text over serial

---

## ⚠️ Common Issues

- **No COM port appears**  
  → Install the micro:bit/mbed serial driver (Windows only)

- **Permission denied (Linux)**  
  → Add your user to the `dialout` group

- **Nothing prints**  
  → Close Mu / Thonny / MakeCode serial console

- **micro:bit powers on but not detected**  
  → USB cable is likely power-only

---

## 🚀 Future Extensions

This driver can be extended into:

- Two-way command protocols
- Binary packet framing (CRC, headers)
- Event-based callbacks (buttons, accelerometer)
- Game controllers or sensor hubs
- Custom languages or APIs on top of micro:bit

---

## 📜 License

MIT License — use it, modify it, break it, improve it.

---

Built for people who want **control**, not magic.
