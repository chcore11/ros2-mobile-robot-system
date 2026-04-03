# 🚀 ROS2 Mobile Robot System

<div align="center">

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue?style=flat-square&logo=ros)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange?style=flat-square&logo=ubuntu)
![MCU](https://img.shields.io/badge/MCU-STM32G4-green?style=flat-square)
![Status](https://img.shields.io/badge/Current--Phase-Competition--Track-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

**A competition-oriented embedded mobile robot project focused on STM32-based AGV chassis closed-loop control.**

</div>

---

## 👤 About This Project

`ros2-mobile-robot-system` is the second major stage of my robotics engineering journey.

After completing a ROS2 navigation project in simulation, I started this repository to move from system-level understanding into real embedded execution and physical robot control.

At the current stage, this repository is no longer treated as an open-ended “simulation to real robot” expansion project.

Instead, its near-term objective has been explicitly aligned with the **2026 National Embedded Chip and System Design Contest**, with the project focus shifted toward building a **competition-deliverable STM32-based AGV chassis control system**.

---

## 🎯 Current Project Positioning

**Current competition direction:**

- **Track:** STMicroelectronics Track  
- **Topic:** Industry 4.0 / Motor Control / Robotics  
- **Project Title:** AGV Chassis Closed-Loop Control System Based on STM32G4  

**Current engineering goal:**

Build a **small but complete embedded mobile robot chassis platform** centered on:

- dual-motor drive  
- PWM-based speed control  
- encoder feedback  
- basic closed-loop control  
- odometry estimation  
- stable motion demonstration  
- competition-oriented engineering documentation  

---

## 🧠 Core Idea

At this stage, the project is **not** centered on full ROS2 autonomy.

The main task now is to build the **embedded control core** of the robot.

That means the project priority is:

**STM32 → Motor Driver → Motor Control → Chassis Motion → Closed-Loop Stability**

ROS2 remains important, but for now it serves as:

- background technical foundation  
- future host-side extension  
- optional communication interface for later integration  

In other words:

> the current main subject is the embedded chassis control system,  
> not the full ROS2 autonomous navigation stack.

---

## ⚙️ Current System Pipeline

### Main Competition Pipeline

STM32G4  
→ PWM / GPIO / Timer Control  
→ TB6612 Motor Driver  
→ Dual DC Motors  
→ Encoder Feedback  
→ Speed Closed-Loop Control  
→ Chassis Motion

### Optional Future Extension

ROS2 / Host Computer  
→ Serial Communication  
→ STM32 Control Layer  
→ Motion Execution

---

## 📍 Current Status

🟡 **Current Phase: Competition Delivery Track**

The repository is currently focused on building the first competition-ready version of the system.

### Current priorities

- STM32 motor control bring-up  
- TB6612 integration  
- forward / backward / turning control  
- encoder signal reading  
- basic speed closed-loop preparation  
- chassis-level stable motion verification  

---

## 🏁 Development Strategy

This project now follows a competition-oriented development path:

### Phase A — Bring-up and Verification
Use the existing hardware platform to quickly verify:

- GPIO / PWM output  
- motor direction control  
- driver wiring correctness  
- basic motion capability  

### Phase B — Competition Version Construction
Move toward the formal competition-oriented embedded system:

- STM32G4-based platform alignment  
- encoder feedback integration  
- speed closed-loop control  
- odometry-related estimation  
- stable AGV-style demo  
- engineering documentation and demonstration materials  

---

## 🖥️ Environment

### Software
- OS: Ubuntu 22.04 (WSL2)
- ROS2: Humble
- Simulator: Gazebo
- IDE: STM32CubeIDE
- Version Control: Git + GitHub

### Hardware
- MCU (current training platform): STM32 Nucleo-F401RE
- MCU (competition target platform): STM32G4 series
- Motor Driver: TB6612FNG
- Robot Base: 2WD mobile chassis
- Motors: DC geared motors with encoder
- Power: battery-powered mobile robot platform

---

## 📂 Project Structure

```text
ros2-mobile-robot-system/
├── docs/        # architecture, hardware notes, competition-related writeups
├── logs/        # daily engineering progress logs
├── assets/      # diagrams, figures, screenshots
├── scripts/     # helper scripts
├── firmware/    # STM32 firmware projects
├── workspace/   # optional ROS2 workspace / host-side packages
├── README.md
└── PROGRESS.md

📚 Documentation Focus

The current documentation work will focus on:

embedded chassis system architecture
STM32 motor control design
TB6612 wiring and driver logic
encoder feedback and speed estimation
closed-loop control strategy
competition-oriented engineering packaging
🏆 Current Milestone Target

The current milestone is not full autonomous navigation.

The current milestone is:

build a stable embedded AGV chassis prototype that can be demonstrated, explained, iterated, and packaged as a competition project.

This includes:

stable dual-motor drive
controllable chassis motion
encoder-based feedback path
basic closed-loop capability
clean repository structure
logs, documentation, and demo materials
🔜 Next Steps

The next major tasks are:

complete dual-motor control on STM32
finish TB6612 integration and stable chassis motion
read encoder signals and establish speed feedback
implement the first version of speed closed-loop control
prepare AGV-style fixed-route / stable-motion demo
refine documentation, logs, and project packaging

Optional later extension:

ROS2 ↔ STM32 communication
cmd_vel mapping
host-side monitoring
lidar integration
real-world SLAM and navigation

These are valuable, but they are not the current main battle.