# 036. Debugging - Node Diagnostics

**Difficulty:** 🟢 Easy  
**Category:** Debugging Tools  
**Tags:** `diagnostics`, `debugging`, `monitoring`, `health`  
**Execution Type:** `ros2_publisher`  

**Frequency:** high  

## 💡 Why This Problem Matters

System health monitoring is vital. If a camera driver fails or overheats, it should report distinct diagnostic errors so the supervisor system can take action (reboot, stop robot).

## Problem Statement

## Problem Statement
Publish diagnostic data to standard topics usually monitored by tools like `rqt_runtime_monitor`.

### Requirements
- Create node `diagnostics_publisher`
- Publish to `/diagnostics` topic
- Message type: `diagnostic_msgs/DiagnosticArray`
- Add a status with level: OK, name: "My Node", message: "Running"
- Rate: 1 Hz

### Input/Output Format
**Output:**
- Diagnostic messages on `/diagnostics`.

### ⚠️ Common Pitfalls
- Incorrect Log Levels (0=OK, 1=WARN, 2=ERROR).

### 📚 Helpful Resources
- [Diagnostic Msgs](https://docs.ros2.org/latest/api/diagnostic_msgs/index.html)

## Test Cases

- **Diagnostic publisher:** Diagnostics topic created
- **Status levels:** OK/WARN/ERROR used
- **Key-value data:** Diagnostic info included

## Learning Objective

Publish diagnostic health data to the /diagnostics topic

## Similar Problems

- Problem #37

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
