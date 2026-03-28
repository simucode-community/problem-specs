# 006. Python - Type Hints & Logging

**Difficulty:** 🟡 Medium  
**Category:** Python for ROS2  
**Tags:** `python`, `type-hints`, `logging`, `best-practices`  
**Execution Type:** `ros2_node`  

**Frequency:** medium  

## 💡 Why This Problem Matters

Robotics codebases are huge and long-lived. Type hints help catch bugs early (via static analysis) and make code readable. Logging levels (INFO, WARN, ERROR) allow operators to filter noise and focus on critical issues during robot operation.

## Problem Statement

## Problem Statement
Write clean, maintainable ROS2 code using Python type hints and proper logging levels.

### Requirements
- Create a node named `clean_node`
- Define a function `calculate_sum(a: int, b: int) -> int` with type hints
- In the node's timer callback (1 Hz):
    - Call `calculate_sum(5, 10)`
    - Log the result using `WARN` level
    - Log format: "Sum is: 15"

### Input/Output Format
**Output:**
- Console Log (WARN): "Sum is: 15"

### ⚠️ Common Pitfalls
- Using `print()` instead of ROS2 logging. Print statements don't show up in `rqt_console` or logs correctly in all launch configurations.

### 📚 Helpful Resources
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [ROS2 Logging](https://docs.ros.org/en/humble/Concepts/About-Logging.html)

## Test Cases

- **Type hints used:** Type annotations present
- **Logging levels:** DEBUG, INFO, WARN, ERROR used
- **Return types:** Optional types handled

## Similar Problems

- Problem #5
- Problem #7

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
