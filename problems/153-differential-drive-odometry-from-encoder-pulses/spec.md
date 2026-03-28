# 153. Differential Drive Odometry from Encoder Pulses

**Difficulty:** 🟡 Medium  
**Category:** Kinematics  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

GPS doesn't work indoors. Encoders are the first line of defense for localization. Fusing this with IMU (Kalman Filter) is standard practice.

## Problem Statement

## Problem Statement
Calculate where the robot is (Odometry) based on how much its wheels have turned (Dead Reckoning).

### Requirements
- Node `odometry_calculator`
- Subscribe: `/wheel_ticks` (Left/Right integers)
- Parameters: `radius` (m), `base_width` (m), `ticks_per_rev`
- Publish: `/odom` (`nav_msgs/Odometry`)

### Input/Output Format
**Input:**
- Wheel Encoder Ticks

**Output:**
- Odometry message with Position (x,y) and Orientation (yaw/quaternion).

### ⚠️ Common Pitfalls
- Integer overflow (ticks wrap around).
- Not handling the very first tick message (delta requires previous state).

### 📚 Helpful Resources
- [Diff Drive Kinematics](https://www.cs.columbia.edu/~allen/F17/NOTES/icckinematics.pdf)

## Test Cases

- **IntegratesForward:** x increases for forward ticks
- **HandlesWrap:** no large jump on wrap

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
