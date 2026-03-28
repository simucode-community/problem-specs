# 018. Include Launch Files

**Difficulty:** 🔴 Hard  
**Category:** Advanced Launch  
**Tags:** `launch`, `include`, `modular`, `composition`  
**Execution Type:** `launch_file`  

**Frequency:** medium  

## 💡 Why This Problem Matters

A full robot launch file is basically a tree of includes: `robot.launch` -> (`sensors.launch`, `navigation.launch`, `control.launch`).

## Problem Statement

## Problem Statement
Build complex systems by including other launch files. This allows for modularity (e.g., including `nav2_bringup` inside your `robot_bringup`).

### Requirements
- Include a launch file named `other.launch.py` from package `other_package`
- Pass an argument `my_arg:='value'` to the included file

### Input/Output Format
**Output:**
- `LaunchDescription` with `IncludeLaunchDescription`

### ⚠️ Common Pitfalls
- Syntax around `PythonLaunchDescriptionSource` (it takes a path string).
- Passing arguments requires `launch_arguments={'key': 'val'}.items()`.

### 📚 Helpful Resources
- [Including Launch Files](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Using-ROS2-Launch-For-Large-Projects.html)

## Test Cases

- **Include action:** IncludeLaunchDescription used
- **Path substitution:** PathJoinSubstitution used
- **Parameter passing:** Parameters forwarded

## Similar Problems

- Problem #17

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
