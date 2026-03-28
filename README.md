# 🚀 ROS2 Mobile Robot System

<div align="center">

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue?style=flat-square\&logo=ros)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange?style=flat-square\&logo=ubuntu)
![Status](https://img.shields.io/badge/Stage--2-Execution--Layer-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

**A ROS2-based mobile robot system transitioning from simulation to real-world execution, with system-level architecture and engineering design.**

</div>

---

## 👤 About This Project

This project is the next stage of my ROS2 robotics journey.

After building a complete navigation system in simulation, this project focuses on extending that system into the real world by integrating embedded hardware and execution layers.

Instead of only making the system run in simulation, the goal here is to understand and implement how a robot actually **moves, executes commands, and interacts with the physical world**.

---

## 🎯 What This Project Does

This project builds a **real-world extension of the ROS2 navigation system**:

Simulation → Execution Layer → Real Robot → Autonomous Navigation

It focuses on:

* bridging ROS2 with embedded systems  
* building a physical robot execution pipeline  
* enabling real robot motion based on ROS2 commands  

---

## 🧠 Key Insight

A working robot system is not just software.

It is a complete system composed of:

* **Perception (SLAM / Lidar)** → understanding the environment  
* **Planning (Nav2)** → deciding where to go  
* **Execution (STM32 + Motor Driver)** → making the robot move  

The execution layer is the missing link between simulation and reality.

---

## ⚙️ System Pipeline

ROS2 cmd_vel
→ Serial Communication
→ STM32 (Execution Layer)
→ TB6612 Motor Driver
→ Motor Output
→ Robot Motion



Supporting flows (future integration):

* `/scan → SLAM → map`
* `map + odom → AMCL → pose`
* `Nav2 → cmd_vel → execution`

---

## 📍 Current Status

🟡 Stage 2 In Progress — Execution Layer Development

Current focus:

* STM32 PWM motor control  
* TB6612 motor driver integration  
* basic motion (forward / backward / turning)  

---

## 🖥️ Environment

* OS: Ubuntu 22.04 (WSL2)
* ROS2: Humble
* Simulator: Gazebo (Stage 1)
* Embedded: STM32 Nucleo-F401RE
* Motor Driver: TB6612FNG

---

## 📂 Project Structure

ros2-mobile-robot-system/
├── docs/ # System architecture and hardware explanations
├── logs/ # Daily progress logs
├── assets/ # Diagrams (architecture, data flow)
├── scripts/ # Launch / control scripts
├── workspace/ # ROS2 packages
└── README.md

---

## 📚 Documentation

Core system topics:

* Execution Layer Design
* ROS2 ↔ STM32 Communication
* Differential Drive Control
* System Architecture (Simulation → Real World)

---

## 🚀 Project Focus

This project emphasizes:

* robotics system architecture  
* simulation → real-world transition  
* embedded system integration  
* execution layer design  
* engineering workflow  

---

## 🏆 Stage 2 Milestone (Target)

The goal of this stage is to achieve:

* stable motor control via STM32  
* real robot movement  
* ROS2 command → physical execution  

This marks the transition from:

> “system runs in simulation” → “system controls a real robot”

---

## 🔜 Next Steps

The next phase will focus on completing the full autonomous loop:

- ROS2 ↔ STM32 communication  
- cmd_vel mapping to motor control  
- encoder-based odometry  
- lidar integration  
- real-world SLAM and navigation  

This represents the evolution from:

> Execution layer → Autonomous real robot system

---

## 📌 Note

This project is continuously evolving as part of a long-term robotics engineering journey.
