# 008. Python - Multi-threading Executor

**Difficulty:** 🔴 Hard  
**Category:** Python for ROS2  
**Tags:** `python`, `threading`, `executor`, `concurrent`  
**Execution Type:** `ros2_node`  

**Seen at:** Cruise, Aurora  
**Frequency:** low  

## 💡 Why This Problem Matters

Complex robots have many sensors. You don't want processing a camera image (slow) to block your emergency stop button check (fast). Multi-threaded executors allow high-priority or independent tasks to run concurrently.

## Problem Statement

## Problem Statement
By default, ROS2 callbacks in Python run in a single thread (sequentially). Use a `MultiThreadedExecutor` to allow parallel execution of callbacks.

### Requirements
- Create two nodes: `node_a` and `node_b`
- Each node should log a message every 1 second (e.g., "node_a is running")
- Use `MultiThreadedExecutor` to spin both nodes concurrently
- Ensure both nodes are added to the same executor instance

### Input/Output Format
**Output:**
- Console logs showing both nodes are active simultaneously.

### ⚠️ Common Pitfalls
- Forgetting to call `executor.add_node(node)`.
- Using `rclpy.spin(node)` which blocks and prevents multi-node execution.

### 📚 Helpful Resources
- [ROS2 Executors](https://docs.ros.org/en/humble/Concepts/About-Executors.html)

## Test Cases

- **Multiple nodes:** 2 nodes created
- **MultiThreadedExecutor:** Executor created
- **Concurrent execution:** Both nodes spinning

## Similar Problems

- Problem #7
- Problem #9

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
