# 045. QoS Profiles - Deadline & Lifespan

**Difficulty:** 🟡 Medium  
**Category:** ROS2 Core  
**Tags:**   
**Execution Type:** `ros2_node`  


## 💡 Why This Problem Matters

**Deadline**: Safety watchdog. If the "Heartbeat" stops, trigger E-Stop. 
**Lifespan**: Don't use old camera frames for obstacle avoidance (latency is dangerous).

## Problem Statement

## Problem Statement
Advanced QoS settings. `Deadline` requires messages to arrive at a certain rate. `Lifespan` invalidates old messages.

### Requirements
- Create `qos_demo` node
- Publisher `/deadline_topic`: Deadline 1000ms
- Publisher `/lifespan_topic`: Lifespan 500ms
- Publish to `/deadline_topic` slower than the deadline (e.g. 2000ms) to trigger a deadline missed event (simulated or logged).

### Input/Output Format
**Output:**
- Publishers configured with correct QoS policies.

### ⚠️ Common Pitfalls
- Mixing `rclpy.duration` (objects) with simple floats/ints for QoS duration fields.

### 📚 Helpful Resources
- [ROS2 QoS Deadlines](https://docs.ros.org/en/humble/Concepts/About-Quality-of-Service-Settings.html)

## Test Cases

- **QoS created:** deadline and lifespan set
- **Missed deadline:** Logs missed deadline
- **Lifespan effect:** Messages expire per lifespan

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
