# 025. Dynamic Transform Broadcaster

**Difficulty:** 🟡 Medium  
**Category:** TF2 Broadcasting  
**Tags:** `tf2`, `dynamic`, `broadcaster`, `moving`  
**Execution Type:** `basic_python`  

**Frequency:** high  

## 💡 Why This Problem Matters

This represents the robot's estimated position (Odometry) relative to its start point. Localization algorithms (AMCL, SLAM) rely on this transform chain.

## Problem Statement

## Problem Statement
Broadcast a dynamic transform that changes over time (e.g., a moving robot or a spinning sensor).

### Requirements
- Create a node `dynamic_broadcaster`
- Broadcast transform from `odom` to `base_link`
- Calculate x, y based on a circular path (radius 2m)
- Update rate: 10 Hz
- Proper timestamping

### Input/Output Format
**Output:**
- Continuous publishing to `/tf` topic.

### ⚠️ Common Pitfalls
- Using `time.time()` python function instead of ROS `self.get_clock().now()` for header timestamps (causes sync issues).

### 📚 Helpful Resources
- [Writing a Broadcaster](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Writing-A-Tf2-Broadcaster-Py.html)

## Learning Objective

Publish a dynamic transform that updates in real time

## Similar Problems

- Problem #24
- Problem #26

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
