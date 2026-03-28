# 022. Actions - Fibonacci with Feedback

**Difficulty:** 🔴 Hard  
**Category:** Actions  
**Tags:** `actions`, `feedback`, `server`, `fibonacci`  
**Execution Type:** `basic_python`  

**Frequency:** medium  

## 💡 Why This Problem Matters

Navigation (move to goal) and Manipulation (pick and place) are almost always implemented as Actions. This allows the robot to report "I'm 50% there" or accept a "Cancel" command if an obstacle appears.

## Problem Statement

## Problem Statement
Actions are for long-running tasks that provide feedback and can be cancelled. Implement an Action Server that computes the Fibonacci sequence.

### Requirements
- Create an action server for the `Fibonacci` action (custom or example)
- Action Name: `fibonacci`
- Logic: Compute sequence up to `order` (from goal)
- Publish feedback (partial sequence) at each step
- Return result (full sequence) when done
- Simluated delay: 1 second per step

### Input/Output Format
**Input:**
- Action Goal: `order=5`

**Output:**
- Feedback: `[0, 1]`, `[0, 1, 1]`, ...
- Result: `[0, 1, 1, 2, 3, 5]`

### ⚠️ Common Pitfalls
- Blocking the callback. You must mark the callback as `async` or use threads.
- Forgetting to set the goal state to `succeed`.

### 📚 Helpful Resources
- [ROS2 Actions Tutorial](https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html)

## Similar Problems

- Problem #21
- Problem #23

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
