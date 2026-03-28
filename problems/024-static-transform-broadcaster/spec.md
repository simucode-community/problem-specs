# 024. Static Transform Broadcaster

**Difficulty:** 🟢 Easy  
**Category:** TF2 Broadcasting  
**Tags:** `tf2`, `transform`, `static`, `broadcaster`  
**Execution Type:** `gazebo_sim`  

**Seen at:** Boston Dynamics, Clearpath  
**Frequency:** very-high  

## 💡 Why This Problem Matters

The TF tree is the single most important concept in ROS geometry. Static transforms define the robot's physical structure (URDF often generates these automagically via `robot_state_publisher`, but knowing how to do it manually is essential for external sensors).

## Problem Statement

## Problem Statement
Broadcast a static coordinate transformation between two frames. This defines the physical relationship between robot parts (e.g., Lidar is 10cm above Base).

### Requirements
- Create a node that broadcasts a static TF
- Parent Frame: `world`
- Child Frame: `robot_base`
- Translation: x=1.0, y=2.0, z=0.0
- Rotation: 0,0,0 (identity quaternion)

### Input/Output Format
**Output:**
- Publishes to `/tf_static` topic.

### ⚠️ Common Pitfalls
- Publishing to `/tf` instead of `/tf_static` (static transforms should be latched and published once or rarely).
- Forgetting the timestamp (`now()`).

### 📚 Helpful Resources
- [Writing a Static Broadcaster](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Writing-A-Tf2-Static-Broadcaster-Py.html)

## Learning Objective

Broadcast a static transform between two coordinate frames

## Similar Problems

- Problem #25
- Problem #26

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
