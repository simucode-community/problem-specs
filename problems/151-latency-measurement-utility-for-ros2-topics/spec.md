# 151. Latency Measurement Utility for ROS2 Topics

**Difficulty:** 🟡 Medium  
**Category:** Tools / Testing  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

In teleoperation (surgery, bomb disposal), high latency means the operator overshoots the target. Validating network performance is a safety requirement.

## Problem Statement

## Problem Statement
Measure the round-trip time (RTT) of messages to benchmark system performance.

### Requirements
- Node `latency_tester`
- Publisher: `/ping` (contains timestamp T1)
- Subscriber: `/pong` (echo of ping)
- Logic: On receipt, compute `RTT = Now() - T1`
- Log Mean/Median/StdDev every 100 samples.

### Input/Output Format
**Output:**
- Console logs with statistics.

### ⚠️ Common Pitfalls
- Clock synchronization issues if running on multiple machines (NTP required).

### 📚 Helpful Resources
- [ROS2 Analysis](https://docs.ros.org/en/humble/Concepts/About-Quality-of-Service-Settings.html)

## Test Cases

- **MeasuresLatency:** returns stats dict
- **HandlesLargeMessages:** no crashes

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
