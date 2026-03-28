# 101. Publish Robot Temperature Status

**Difficulty:** 🟢 Easy  
**Category:** Topics  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

Monitoring battery and motor driver temperatures is critical. Algorithms throttle performance if temps get too high.

## Problem Statement

## Problem Statement
A foundational task: Create a publisher that simulates a temperature sensor.

### Requirements
- Node `temp_sensor`
- Topic `/robot_temp`
- Type `std_msgs/Float32`
- Logic: Start at 20.0, increase by 0.5 every second.

### Input/Output Format
**Output:**
- Streams 20.0, 20.5, 21.0... to local topic.

### ⚠️ Common Pitfalls
- Resetting the variable inside the callback (so it never increases).

### 📚 Helpful Resources
- [ROS2 Publishers](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

## Test Cases

- **PublishesTemperature:** Float32
- **IncreasesOverTime:** monotonically increasing

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
