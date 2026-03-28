# 183. The Sensor Fusion Latency Challenge

**Difficulty:** 🔴 Hard  
**Category:** Real-Time Performance  
**Tags:** `cpp`, `ros2`, `real-time`, `multi-threading`, `sensor-fusion`, `industry`  
**Execution Type:** `ros2_cpp_node`  

**Seen at:** Waymo, Tesla, Boston Dynamics, Aurora  
**Frequency:** very-high  

## Problem Statement

Implement a multi-threaded ROS2 node that fuses IMU, LIDAR, and camera data in real-time. Your solution must maintain a consistent loop rate of ≥100Hz while processing all sensor streams simultaneously.

Key Requirements:
• Use ROS2 Message Filters for time synchronization
• Implement multi-threading for parallel sensor processing
• Maintain CPU usage below 40% and memory under 512MB
• Handle sensor dropout gracefully without crashing

Industry Context: This mirrors real-world autonomous vehicle perception pipelines used at companies like Waymo and Tesla.

## Test Cases

- **Loop Rate:** ≥100Hz sustained for 30 seconds
- **CPU Usage:** ≤40% average
- **Memory Usage:** ≤512MB peak
- **Sensor Dropout:** No crashes when 1 sensor drops

## Similar Problems

- Problem #35
- Problem #144

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
