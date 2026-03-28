# 009. C++ vs Python - Performance Comparison

**Difficulty:** 🟡 Medium  
**Category:** Language Comparison  
**Tags:** `python`, `cpp`, `performance`, `benchmarking`  
**Execution Type:** `ros2_publisher`  

**Frequency:** low  

## 💡 Why This Problem Matters

Python is great for prototyping, logic, and glue code. C++ is used for tight control loops (1kHz+) and image processing. Knowing when to switch languages is a senior robotics engineer skill.

## Problem Statement

## Problem Statement
Performance is critical in robotics. Although Python is easier to write, high-frequency tasks often drift or consume high CPU. In this problem, you will implement a high-frequency publisher and measure its actual performance.

### Requirements
- Create a Python node named `high_frequency_publisher`
- Publish an `Int64` message to `counter_topic` at exactly 100 Hz (0.01s interval).
- Logic: Increment a `self.counter` in every callback.
- Performance Check: Every 100 messages, calculate and log the average frequency (Hz) or elapsed time.

### Input/Output Format
**Output:**
- Console Log: A message containing "Hz", "frequency", or "time" every 100 messages.

### ⚠️ Common Pitfalls
- Timer drift: Python timers are not real-time; actual frequency may be slightly lower than 100Hz.
- Blocking callbacks: Heavy logic in the callback will drop the frequency significantly.

### 📚 Helpful Resources
- [ROS2 Timers (Python)](https://docs.ros.org/en/humble/Concepts/About-Quality-of-Service-Settings.html)

## Test Cases

- **High frequency:** 100 Hz publishing
- **Performance metrics:** Timing logged
- **Counter accuracy:** Correct increment

## Similar Problems

- Problem #7
- Problem #8

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
