# 044. Lifecycle Node - State Machine

**Difficulty:** 🟡 Medium  
**Category:** ROS2 Core  
**Tags:**   
**Execution Type:** `ros2_lifecycle`  


## 💡 Why This Problem Matters

Lifecycle nodes allow a supervisor to boot a robot in stages: 1. Load Drivers (Configure) 2. Verify Health 3. Start Motors (Activate). If safety check fails, you can Deactivate immediately.

## Problem Statement

## Problem Statement
Implement a Managed (Lifecycle) Node. These nodes have a state machine (Unconfigured, Inactive, Active, Finalized) and transitions (Configure, Activate, Deactivate, Cleanup).

### Requirements
- Create a class `MyLifecycleNode` inheriting from `LifecycleNode`
- Implement `on_configure` (return SUCCESS)
- Implement `on_activate` (return SUCCESS, start publisher)
- Implement `on_deactivate` (return SUCCESS, stop publisher)
- Implement `on_cleanup` (return SUCCESS)

### Input/Output Format
**Output:**
- Logs indicating state transitions.

### ⚠️ Common Pitfalls
- Using a regular `Node` instead of `LifecycleNode`.
- Forgetting to call `super().__init__(...)`.

### 📚 Helpful Resources
- [Lifecycle Nodes](https://github.com/ros2/demos/blob/humble/lifecycle/README.rst)

## Test Cases

- **Lifecycle methods:** on_configure/on_activate exist
- **Transition success:** State becomes active
- **Run handling:** Runs when triggered in active state

## Learning Objective

Implement a lifecycle node with proper state transitions

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
