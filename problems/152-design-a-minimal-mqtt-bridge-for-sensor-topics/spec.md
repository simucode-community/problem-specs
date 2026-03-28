# 152. Design a Minimal MQTT Bridge for Sensor Topics

**Difficulty:** 🟡 Medium  
**Category:** Integration  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

Fleet management dashboards (web apps) don't speak DDS. They speak MQTT/HTTP. Bridges connect the operational technology (OT) to information technology (IT).

## Problem Statement

## Problem Statement
Bridge ROS2 (local robot network) to MQTT (IoT/Cloud). Send sensor data to the cloud.

### Requirements
- Node `mqtt_bridge`
- Subscribe: `/battery_level` (Float32)
- Connect to MQTT Broker (e.g., `localhost:1883`)
- On callback: Publish value to MQTT topic `robot/battery`

### Input/Output Format
**Input:**
- ROS topic updates.

**Output:**
- MQTT messages.

### ⚠️ Common Pitfalls
- Blocking the ROS callback waiting for network I/O.

### 📚 Helpful Resources
- [ROS2 MQTT Bridge](https://github.com/start-robotics/mqtt_bridge)

## Test Cases

- **PublishesToMQTT:** message on mqtt_topic
- **SubscribesFromMQTT:** ros topic receives message

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
