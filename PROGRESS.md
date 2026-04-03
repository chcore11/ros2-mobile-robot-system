
---

# PROGRESS.md

```md
# PROGRESS

## Project Identity

**Repository:** `ros2-mobile-robot-system`  
**Current Phase Role:** Competition-Oriented Embedded Mobile Robot Project  
**Near-Term Goal:** Deliver an STM32-based AGV chassis closed-loop control system for the 2026 embedded competition

---

## Stage 0: Background Foundation (Completed)

This repository is built on top of an already completed simulation-stage robotics foundation.

- [✅] ROS2 navigation simulation project completed
- [✅] Gazebo simulation environment setup
- [✅] SLAM mapping
- [✅] Map saving and loading
- [✅] AMCL localization
- [✅] Nav2 navigation pipeline verification
- [✅] TF tree understanding (`map → odom → base_link`)
- [✅] End-to-end simulation navigation workflow understanding

---

## Stage 1: Competition Positioning (Completed)

This stage focused on redefining the project from a general real-robot extension effort into a competition-deliverable engineering project.

- [✅] Competition direction investigated
- [✅] Current project objective aligned with embedded competition delivery
- [✅] ST track selected as main direction
- [✅] Topic direction narrowed to:
  - Industry 4.0 / Motor Control / Robotics
- [✅] Project positioning updated toward:
  - STM32-based AGV chassis closed-loop control system
- [✅] Registration information draft prepared
- [✅] Initial teammate recruitment started
- [✅] Advisor consultation preparation started

---

## Stage 2: Embedded Bring-up (In Progress)

### Hardware Preparation

- [✅] Robot chassis assembled
- [ ] Power system fully prepared
- [ ] Stable mobile power solution verified
- [ ] Full wiring cleanup and reinforcement completed

### STM32 Basic Control

- [✅] STM32 development environment set up
- [✅] Basic GPIO output verified
- [✅] Basic input logic verified
- [✅] PWM output basic verification completed
- [ ] Single motor stable control completed
- [ ] Dual motor stable control completed
- [ ] Forward / backward / turning control completed
- [ ] Stop / restart behavior verified

### Motor Driver Integration (TB6612)

- [ ] STM32 ↔ TB6612 wiring completed
- [ ] Driver logic verified
- [ ] Motor direction control verified
- [ ] Stable motor output achieved

---

## Stage 3: Feedback and Closed-Loop Control (Core Target)

This is one of the most important stages for transforming the project from a “moving car demo” into a real competition work.

### Encoder Feedback

- [ ] Encoder wiring completed
- [ ] Encoder pulse reading verified
- [ ] Basic wheel speed estimation implemented
- [ ] Left / right wheel feedback consistency checked

### Closed-Loop Control

- [ ] Basic speed closed-loop design completed
- [ ] First version of speed control implemented
- [ ] Left / right wheel speed consistency improved
- [ ] Start / stop smoothness improved
- [ ] Basic dynamic response optimization started
- [ ] Control effect comparison recorded

### Odometry Preparation

- [ ] Basic odometry estimation path defined
- [ ] Motion state output prepared
- [ ] Distance / speed / wheel-state feedback organized

---

## Stage 4: Competition Demo Version

This stage focuses on building a small but complete AGV-style embedded system demo.

### Basic Demonstration Capability

- [ ] Stable straight-line motion
- [ ] Stable turning behavior
- [ ] Fixed-route motion demonstration
- [ ] Repeatable demo process prepared
- [ ] Continuous operation test performed

### Basic System Features

- [ ] Parameter tuning interface prepared
- [ ] Runtime state output available
- [ ] Basic fault / stop strategy considered
- [ ] Demo-oriented chassis behavior stabilized

---

## Stage 5: Engineering Packaging

This stage determines whether the project looks like a competition-grade engineering deliverable.

### Documentation

- [ ] README reconstructed for competition version
- [ ] PROGRESS reconstructed for competition version
- [ ] Hardware architecture notes written
- [ ] Motor control notes written
- [ ] Closed-loop design notes written
- [ ] Debug records organized
- [ ] Key design decisions documented

### Presentation Materials

- [ ] Demo video recorded
- [ ] System architecture diagram prepared
- [ ] Data / control flow diagram prepared
- [ ] Project introduction slides prepared
- [ ] Competition description materials refined

---

## Stage 6: Optional ROS2 Extension (Deferred / Non-Mainline)

ROS2 integration remains valuable, but it is currently treated as a secondary extension rather than the main development line.

### Host-Side Integration

- [ ] Serial communication setup
- [ ] Command protocol definition
- [ ] ROS2 command → STM32 motion mapping
- [ ] `cmd_vel` mapping experiment
- [ ] Host-side monitoring interface

### Extended Real Robot System

- [ ] Lidar integration
- [ ] Real-world SLAM
- [ ] Real-world map saving
- [ ] AMCL localization
- [ ] Nav2 integration
- [ ] Goal-based autonomous navigation

---

## 🎯 Current Focus

> **Stage 2 — Embedded Bring-up**  
> Goal: make the chassis move stably under STM32 control and prepare the feedback path required for closed-loop control.

Current top priorities:

- STM32 ↔ TB6612 integration  
- single-motor and dual-motor verification  
- forward / backward / turning control  
- encoder access preparation  
- competition-oriented embedded control pipeline bring-up  

---

## 🚩 Milestone Definition

### Milestone 1 — Motion Bring-up
✔ The robot chassis moves stably under STM32 control

### Milestone 2 — Feedback Established
✔ Encoder signals are readable and basic speed feedback is available

### Milestone 3 — Closed-Loop Prototype
✔ Basic speed closed-loop control works and improves motion consistency

### Milestone 4 — Competition Demo Version
✔ A small but complete AGV chassis demo can be repeatedly demonstrated

### Milestone 5 — Engineering Delivery
✔ Repository, documentation, demo video, and presentation materials are ready for competition use

---

## 📌 Strategic Note

This project is no longer being pushed as an unrestricted long-term exploration repo at the current stage.

The current strategy is:

> **competition delivery first, system expansion later**

That means:

- embedded chassis control is the current mainline
- closed-loop control is the current technical core
- ROS2 integration is valuable but secondary for now
- engineering packaging is part of the deliverable, not an afterthought