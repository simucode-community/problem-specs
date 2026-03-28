# 037. Data Recording - Custom Bag Recorder

**Difficulty:** 🟡 Medium  
**Category:** rosbag2  
**Tags:** `rosbag`, `recording`, `data`, `topics`  
**Execution Type:** `ros2_parameters`  

**Frequency:** medium  

## 💡 Why This Problem Matters

"Black Box" recording is essential for failure analysis. Robots often trigger recording automatically when an error is detected.

## Problem Statement

## Problem Statement
Programmatically invoke `ros2 bag record` functionality via a subprocess or direct API (if available) to record specific topics.

### Requirements
- Create a node that uses `subprocess` to start regular recording
- Record topic `/chatter`
- Create a file/directory named `my_bag`
- Stop recording after 5 seconds

### Input/Output Format
**Output:**
- A bag directory created on the filesystem.

### ⚠️ Common Pitfalls
- Not waiting long enough for data to be captured.
- Path issues (use absolute paths or know your CWD).

### 📚 Helpful Resources
- [Rosbag2](https://github.com/ros2/rosbag2)

## Test Cases

- **Bag writer:** rosbag2 writer initialized
- **Topic selection:** Specific topics recorded
- **File path:** Custom bag path used

## Learning Objective

Record and stop ROS 2 bag files from a node using subprocess

## Similar Problems

- Problem #36
- Problem #38

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
