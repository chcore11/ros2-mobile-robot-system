# Control Model

## 1. System
This robot is a differential-drive chassis.

Current platform:
- STM32 Nucleo-F401RE
- TB6612FNG motor driver
- two DC motors
- two encoders

The chassis motion depends on left and right wheel speeds.

## 2. Basic Motion
Define:
- `v_l`: left wheel speed
- `v_r`: right wheel speed

Basic cases:
- forward: `v_l > 0`, `v_r > 0`
- backward: `v_l < 0`, `v_r < 0`
- left turn: `v_l < 0`, `v_r > 0`
- right turn: `v_l > 0`, `v_r < 0`
- stop: `v_l = 0`, `v_r = 0`

## 3. Motion Commands
Motion commands should be mapped to target wheel speeds.

Examples:
- `FORWARD`:
  - `target_speed_left = +v`
  - `target_speed_right = +v`

- `BACKWARD`:
  - `target_speed_left = -v`
  - `target_speed_right = -v`

- `LEFT_TURN`:
  - `target_speed_left = -v_t`
  - `target_speed_right = +v_t`

- `RIGHT_TURN`:
  - `target_speed_left = +v_t`
  - `target_speed_right = -v_t`

- `STOP`:
  - `target_speed_left = 0`
  - `target_speed_right = 0`

## 4. Speed Estimation
The encoder does not give speed directly.

It gives pulse counts.

We estimate wheel speed from encoder count increments in a fixed time window.

Define:
- `dt`: sampling period
- `delta_count_left`
- `delta_count_right`
- `N`: pulses per wheel revolution

Then:

- `rps_left = delta_count_left / (N * dt)`
- `rps_right = delta_count_right / (N * dt)`

At the current stage, count-per-window or RPM is enough for control testing.

## 5. Control Variables
The software should separate these variables:

- `target_speed_left`
- `target_speed_right`
- `measured_speed_left`
- `measured_speed_right`
- `error_left`
- `error_right`
- `pwm_left`
- `pwm_right`

Where:
- `error_left = target_speed_left - measured_speed_left`
- `error_right = target_speed_right - measured_speed_right`

## 6. Motor Difference
The two motors are not exactly the same.

With the same PWM:
- left speed may be different from right speed

So the robot may drift in open-loop motion.

## 7. PWM-Speed Calibration
A useful idea is to build a mapping between PWM and wheel speed:

- `v_l = f_l(PWM_l)`
- `v_r = f_r(PWM_r)`

This is used for feedforward compensation.

It can reduce static mismatch between left and right wheels.

But it cannot solve all dynamic errors.

## 8. Next Step
The next software goal is:

- define target wheel speeds
- estimate measured wheel speeds
- compute speed errors
- prepare for future closed-loop control