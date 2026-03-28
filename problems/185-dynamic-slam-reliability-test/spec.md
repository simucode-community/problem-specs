# 185. Dynamic SLAM Reliability Test

**Difficulty:** 🔴 Hard  
**Category:** Localization & Mapping  
**Tags:** `python`, `ros2`, `slam`, `algorithms`, `industry`  
**Execution Type:** `ros2_python_node`  

**Seen at:** Amazon Robotics, Fetch Robotics, Clearpath, Boston Dynamics  
**Frequency:** very-high  

## 💡 Why This Problem Matters

This problem mirrors the challenges faced by warehouse robots (Amazon Robotics, Fetch Robotics) that must navigate reliably in dynamic environments with moving people and obstacles. Robust localization during sensor occlusion is critical for safety certification.

## Problem Statement

## Problem Statement

Implement a **particle filter-based SLAM system** that maintains accurate localization even when sensor data is temporarily unavailable due to dynamic obstacles.

### Requirements

Your SLAM system must:
- **Maintain localization error ≤ 0.15m** during normal operation
- **Prevent divergence** when LIDAR is occluded for up to 3 seconds
- **Recover within 2 seconds** after occlusion ends
- **Detect loop closures** and correct accumulated drift
- Use **adaptive resampling** to prevent particle depletion

### Input/Output Format

**Input:**
- LIDAR scans on `/scan` (sensor_msgs/LaserScan)
- Odometry on `/odom` (nav_msgs/Odometry)

**Output:**
- Estimated pose on `/particle_filter/pose` (geometry_msgs/PoseStamped)
- Particle cloud on `/particle_filter/particles` (geometry_msgs/PoseArray)
- Must log **"Particle Filter SLAM Ready"** when initialized

## Test Cases

- **Normal Operation:** Localization error ≤0.15m
- **During Occlusion:** No divergence
- **Recovery Time:** ≤2 seconds post-occlusion
- **Loop Closure:** Detect and correct drift

## Similar Problems

- Problem #119
- Problem #161

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
