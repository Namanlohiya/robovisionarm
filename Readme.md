# 🤖 RoboVisionArm

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Robotics](https://img.shields.io/badge/Field-Robotics-orange.svg)
![Computer Vision](https://img.shields.io/badge/Technology-Computer%20Vision-red.svg)

**RoboVisionArm** is a Python library that enables **real-time control of a DIY robotic arm using computer vision and hand gestures**.
It uses **OpenCV**, **MediaPipe**, and **Arduino serial communication** to convert hand movements into robotic arm motion.

This library is ideal for:

* 🤖 DIY robotic arm projects
* 🎓 Engineering and robotics students
* 🧪 Science exhibitions and competitions
* 🔬 Robotics and computer vision research
* 🏭 Prototype automation systems

---

# 🎥 Demo Video

Upload your demo video (`robotarm.mp4`) to your GitHub repository and embed it here.

Example:

```
https://github.com/Namanlohiya/robovisionarm/robotarm.mp4
```

GitHub will automatically show a video player.

---

# 📦 Installation

Install from PyPI:

```
pip install robovisionarm
```

Or install dependencies manually:

```
pip install opencv-python mediapipe pyserial
```

---

# ⚡ Quick Start

This is the fastest way to run your robotic arm:

```python
from robovisionarm import RoboVisionArm

arm = RoboVisionArm(
    port="COM3",        # Change to your Arduino port (example: COM3 or /dev/ttyUSB0)
    camera_index=0,     # Default webcam
    debug=False         # True = print angles only
)

arm.run()
```

Press **ESC** to safely exit.

---

# 🎮 Gesture Controls

| Gesture                       | Robotic Arm Movement    |
| ----------------------------- | ----------------------- |
| Move hand LEFT / RIGHT        | Base rotation           |
| Move hand UP / DOWN           | Shoulder movement       |
| Move hand forward / backward  | Elbow movement          |
| Extend index & middle fingers | Wrist rotation          |
| Pinch thumb and index finger  | Open / Close gripper    |
| No hand detected              | Return to home position |

---

# 🔌 Arduino Setup

Upload this code to your Arduino:

```cpp
#include <Servo.h>

Servo base;
Servo shoulder;
Servo elbow;
Servo wrist;
Servo gripper;

void setup()
{
  Serial.begin(115200);

  base.attach(3);
  shoulder.attach(5);
  elbow.attach(6);
  wrist.attach(9);
  gripper.attach(10);
}

void loop()
{
  if (Serial.available() >= 5)
  {
    base.write(Serial.read());
    shoulder.write(Serial.read());
    elbow.write(Serial.read());
    wrist.write(Serial.read());
    gripper.write(Serial.read());
  }
}
```

---

# 🧠 How It Works

1. Webcam captures live video
2. MediaPipe detects hand landmarks
3. Landmarks convert into servo angles
4. Python sends angles via serial communication
5. Arduino moves servo motors

All of this happens in **real time**.

---

# 📂 Example Usage

Run example script:

```
python examples/run_arm.py
```

---

# ⚙️ Library Parameters

```
RoboVisionArm(
    port="COM3",
    camera_index=0,
    debug=False
)
```

| Parameter    | Description                     |
| ------------ | ------------------------------- |
| port         | Arduino serial port             |
| camera_index | Webcam index                    |
| debug        | Print angles instead of sending |

---

# 🦾 Hardware Requirements

* Arduino Uno / Nano / Mega
* Servo motors (SG90, MG996R, etc.)
* USB Webcam
* DIY robotic arm
* External power supply (recommended)

---

# 📊 Applications

* Gesture-controlled robotic arms
* Industrial robotic prototypes
* Educational robotics labs
* Computer vision research
* Automation demonstrations

---

# 📁 Project Structure

```
robovisionarm/
│
├── robovisionarm/
│   ├── controller.py
│   ├── gestures.py
│   ├── serial_comm.py
│   ├── config.py
│
├── examples/
│   └── run_arm.py
│
├── README.md
├── LICENSE
├── pyproject.toml
└── setup.py
```

---

# 🧑‍💻 Author

**Naman Lohiya**
Robotics and Computer Vision Developer

---

# 📜 License

MIT License

---

# ⭐ Support

If you like this project, consider starring the GitHub repository and sharing it with the robotics community.

  
