# 016. Launch Arguments & Substitutions

**Difficulty:** 🟡 Medium  
**Category:** Python Launch  
**Tags:** `launch`, `arguments`, `substitutions`, `configuration`  
**Execution Type:** `launch_file`  

**Frequency:** high  

## 💡 Why This Problem Matters

Reusable launch files are key. You shouldn't have `lidar_front.launch.py` and `lidar_back.launch.py`. You should have `lidar.launch.py` and call it twice with `arg:name=front` and `arg:name=back`.

## Problem Statement

## Problem Statement
Make your launch file dynamic using `DeclareLaunchArgument`. This allows users to pass configuration from the command line (e.g., `ros2 launch my.launch.py speed:=10`).

### Requirements
- Declare argument named `message` with default `"Hello"`
- Launch `demo_nodes_cpp/talker`
- Pass this argument as a parameter to the node using `LaunchConfiguration`

### Input/Output Format
**Output:**
- `LaunchDescription` with arguments and node.

### ⚠️ Common Pitfalls
- Trying to read `LaunchConfiguration` as a string directly in Python code (it's resolved at runtime, not parse time).

### 📚 Helpful Resources
- [Launch Arguments](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Using-ROS2-Launch-For-Large-Projects.html)

## Test Cases

- **Arguments declared:** 2 launch arguments
- **Substitutions used:** LaunchConfiguration used
- **Dynamic parameters:** Parameters from arguments

## Similar Problems

- Problem #15
- Problem #17

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
