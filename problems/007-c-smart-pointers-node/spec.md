# 007. C++ - Smart Pointers Node

**Difficulty:** 🟡 Medium  
**Category:** C++ for ROS2  
**Tags:** `cpp`, `smart-pointers`, `memory`, `modern-cpp`  
**Execution Type:** `basic_python`  

**Seen at:** Boston Dynamics, NVIDIA  
**Frequency:** medium  

## 💡 Why This Problem Matters

C++ is the standard for performance-critical robotics (drivers, control loops, SLAM). Smart pointers (`std::shared_ptr`, `std::unique_ptr`) prevent memory leaks, which is critical for robots that run for weeks without restarting.

## Problem Statement

## Problem Statement
Create a minimal C++ ROS2 node using modern C++ features like smart pointers (`std::shared_ptr`).

### Requirements
- Language: **C++**
- Create a class inheriting from `rclcpp::Node`
- Node name: `cpp_smart_node`
- Use `RCLCPP_INFO` to log "C++ Node Started" in the constructor
- Ensure standard main function with `rclcpp::init`, `rclcpp::spin`, `rclcpp::shutdown`

### Input/Output Format
**Output:**
- Console Log: "C++ Node Started"

### ⚠️ Common Pitfalls
- Compilation errors due to missing semicolons or headers.
- Forgetting `public` inheritance: `class MyNode : public rclcpp::Node`

### 📚 Helpful Resources
- [Writing a simple C++ publisher/subscriber](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html)

## Test Cases

- **Smart pointers:** shared_ptr and unique_ptr used
- **Memory management:** No memory leaks
- **Lambda callbacks:** Modern C++ syntax

## Similar Problems

- Problem #8

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
