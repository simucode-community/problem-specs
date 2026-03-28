# 020. QoS - Reliable vs Best Effort

**Difficulty:** 🔴 Hard  
**Category:** Topics  
**Tags:** `qos`, `reliability`, `topics`, `configuration`  
**Execution Type:** `ros2_node`  

**Seen at:** Amazon Robotics  
**Frequency:** low  

## 💡 Why This Problem Matters

**Reliable** (TCP-like) is for critical data like "Mission Status". **Best Effort** (UDP-like) is for high-freq sensor data (Video, Lidar) where dropping a packet is better than delaying the stream.

## Problem Statement

## Problem Statement
Understand Quality of Service (QoS) policies. Create a publisher with `Reliable` QoS and one with `Best Effort`.

### Requirements
- Create node `qos_test`
- Publisher 1: `/reliable_topic`, QoS: Reliable
- Publisher 2: `/best_effort_topic`, QoS: Best Effort
- Message type: `std_msgs/String`

### Input/Output Format
**Output:**
- Node with 2 publishers configured correctly.

### ⚠️ Common Pitfalls
- Mismatched QoS: A Reliable subscriber cannot receive data from a Best Effort publisher (ROS2 compatibility rules).

### 📚 Helpful Resources
- [ROS2 QoS Policies](https://docs.ros.org/en/humble/Concepts/About-Quality-of-Service-Settings.html)

## Test Cases

- **QoS profiles:** 2 different QoS profiles
- **Reliability settings:** RELIABLE and BEST_EFFORT
- **Compatibility:** Matching QoS for pub/sub

## Similar Problems

- Problem #19
- Problem #21

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
