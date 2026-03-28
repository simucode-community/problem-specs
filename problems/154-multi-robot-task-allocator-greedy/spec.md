# 154. Multi-Robot Task Allocator (Greedy)

**Difficulty:** 🟡 Medium  
**Category:** Multi-Robot  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

Uber for Robots. Efficiently assigning 1000 orders to 100 robots determines the profitability of an automated warehouse.

## Problem Statement

## Problem Statement
Assign tasks to the nearest available robot. A basic fleet management algorithm.

### Requirements
- Node `dispatcher`
- Subscribe: `/robot_poses` (Array of poses) and `/pending_tasks` (Array of locations)
- Logic: For the next task, find the robot with minimum Euclidean distance.
- Publish: `/assignments` (RobotID, TaskID)

### Input/Output Format
**Output:**
- Assignment messages.

### ⚠️ Common Pitfalls
- Race conditions: Assigning the same robot to two tasks.

### 📚 Helpful Resources
- [Multi-Robot Systems](https://dist.hu/ros-multi-robot)

## Test Cases

- **AllTasksAssigned:** no unassigned tasks if robots >= tasks
- **RespectsAvailability:** assigned start >= robot.available_time

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
