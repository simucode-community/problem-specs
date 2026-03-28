# 067. Cobot - IO Integration (Digital I/O)

**Difficulty:** 🟢 Easy  
**Category:** Cobot Programming  
**Tags:**   
**Execution Type:** `ros2_node`  


## 💡 Why This Problem Matters

Universal Robots (UR) and Fanuc robots use digital I/O for grippers, conveyor belts, and safety curtains.

## Problem Statement

## Problem Statement
Simulate interacting with a Cobot's Digital I/O (Input/Output) board. Read a sensor state and trigger an effector.

### Requirements
- Node `io_controller`
- Subscribe to `/digital_inputs` (`im_msgs/DigitalInputs` or similar std_msgs)
- Publish to `/digital_outputs` (`std_msgs/Bool`)
- Logic: If input[0] is TRUE, set output[0] to TRUE (turn on light).

### Input/Output Format
**Input:**
- `/digital_inputs` array

**Output:**
- `/digital_outputs` (Bool)

### ⚠️ Common Pitfalls
- Logic inversion (Active Low vs Active High).

### 📚 Helpful Resources
- [Industrial IO Control](https://wiki.ros.org/Industrial)

## Test Cases

- **Reads input:** Subscribes to digital input topic
- **Toggles output:** Publishes digital output on condition
- **No duplicate IO:** Debounce logic or simple guard present

## Learning Objective

Implement behavioral logic to map digital sensor input to actuator output

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
