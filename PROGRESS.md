# PROGRESS

## Stage 1: Simulation System (Completed)

- [✅️] Gazebo simulation environment setup  
- [✅️] SLAM mapping  
- [✅️] Map saving and loading  
- [✅️] AMCL localization  
- [✅️] Nav2 navigation pipeline  
- [✅️] TF tree understanding (map → odom → base_link)  
- [✅️] Full navigation pipeline verification  

---

## Stage 2: Execution Layer (In Progress)

### Hardware Setup

- [ ] Assemble robot chassis  
- [ ] Install motors and caster wheel  
- [ ] Prepare power system (battery + wiring)  

---

### Motor Control (STM32)

- [ ] PWM output configuration  
- [ ] Basic motor control (forward / backward)  
- [ ] Differential drive control (left / right turning)  
- [ ] Speed control via PWM  

---

### Motor Driver Integration (TB6612)

- [ ] Wire STM32 ↔ TB6612  
- [ ] Verify driver functionality  
- [ ] Enable stable motor output  

---

### Encoder Feedback (Optional Upgrade)

- [ ] Read encoder signals  
- [ ] Basic speed estimation  
- [ ] Prepare for odometry  

---

## Stage 3: Communication Layer

### ROS2 ↔ STM32

- [ ] Serial communication setup  
- [ ] Send command from ROS2  
- [ ] Receive command on STM32  
- [ ] Define simple command protocol  

---

### cmd_vel Mapping

- [ ] Convert linear/angular velocity  
- [ ] Map to left/right wheel speeds  
- [ ] Verify motion consistency  

---

## Stage 4: Real Robot Integration

- [ ] Integrate Lidar (/scan)  
- [ ] Run SLAM in real environment  
- [ ] Save real-world map  

---

## Stage 5: Autonomous Navigation

- [ ] AMCL localization (real robot)  
- [ ] Nav2 integration  
- [ ] Goal-based navigation  
- [ ] Obstacle avoidance verification  

---

## Stage 6: Engineering Optimization

- [ ] System architecture diagram  
- [ ] Data flow diagram  
- [ ] Code modularization  
- [ ] Debugging tools and logs  
- [ ] Demo video recording  
- [ ] Documentation refinement  

---

## 🎯 Current Focus

> Stage 2 — Execution Layer

Goal:

- Make the robot move  
- Build a stable control pipeline  
- Prepare for system integration  

---

## 🚩 Milestone Definition

### Milestone 1
✔ Robot moves under STM32 control  

---

### Milestone 2
✔ ROS2 commands control robot motion  

---

### Milestone 3
✔ Autonomous navigation in real world  

---