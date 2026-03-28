# 010. URDF - Simple Robot Description

**Difficulty:** 🟢 Easy  
**Category:** URDF  
**Tags:** `urdf`, `robot-description`, `xml`, `validation`  
**Execution Type:** `ros2_node`  

**Seen at:** Fetch Robotics  
**Frequency:** high  

## 💡 Why This Problem Matters

URDF (Unified Robot Description Format) is the standard for define robot kinematics and visuals. It's used by Gazebo (simulation), RViz (visualization), and MoveIt (motion planning).

## Problem Statement

## Problem Statement
(Note: Since this environment runs Python/C++ code, this problem validates your understanding by generating strings, as we cannot render URDFs visually here).

Write a Python script that outputs a valid URDF XML string for a simple 2-link robot arm and parses it.

### Requirements
- Create a node that declares a `robot_description` parameter containing the URDF string.
- Define two links: `base_link` and `arm_link`
- Define one joint: `shoulder_joint` connecting them
- **Parsing**: Use the standard Python `xml.etree.ElementTree` library to parse your own URDF string and log completion.
- **Note**: Avoid using `urdf_parser_py` as it is not pre-installed in this environment.

### Input/Output Format
**Output:**
- Console Log: "URDF parsed successfully"
- Logic: Log the number of links found (should be 2).

### ⚠️ Common Pitfalls
- Mismatched tags (closing `<link>` with `</joint>`).
- Missing required attributes for joints (parent, child).

### 📚 Helpful Resources
- [Python ElementTree Documentation](https://docs.python.org/3/library/xml.etree.elementtree.html)

## Test Cases

- **Parameter declared:** robot_description parameter
- **URDF loaded:** URDF parsed successfully
- **Links counted:** Number of links logged

## Learning Objective

Describe a robot's physical structure using URDF

## Similar Problems

- Problem #11
- Problem #12

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
