# 184. The RTOS Control Loop Stability

**Difficulty:** 🔴 Hard  
**Category:** Real-Time Systems  
**Tags:** `cpp`, `ros2`, `control-theory`, `rtos`, `industry`  
**Execution Type:** `ros2_cpp_node`  

**Seen at:** ABB Robotics, FANUC, KUKA, Universal Robots  
**Frequency:** high  

## 💡 Why This Problem Matters

Real-time constraints are non-negotiable in industrial automation. A missed deadline in a control loop can cause physical damage to the robot or workpiece. This problem tests your ability to write deterministic C++ code for safety-critical systems.

## Problem Statement

## Problem Statement

Implement a **stable PID control loop** for a 6-DOF industrial robot arm (ABB/KUKA style) that maintains a strictly periodic 100Hz execution rate.

### Requirements

Your controller must:
- **Run at exactly 100Hz** (±1% jitter allowed)
- **Settle within 2 seconds** for a step input
- **Steady-state error < 0.1 radians**
- **Overshoot < 5%**
- **Implement anti-windup** for integral term
- **Use RELIABLE QoS** for critical command topics

### Input/Output Format

**Input:**
- Joint State on `/joint_states` (sensor_msgs/JointState)
- Target Pose on `/target_pose` (geometry_msgs/PoseStamped)

**Output:**
- Joint Commands on `/joint_commands` (std_msgs/Float64MultiArray)
- Must log **"PID Controller Ready"** when initialized
- Loop rate status logs

## Test Cases

- **Settling Time:** ≤1.5 seconds
- **Steady State Error:** ≤0.01m
- **Overshoot:** ≤15%
- **QoS Compliance:** No message drops

## Similar Problems

- Problem #178

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
