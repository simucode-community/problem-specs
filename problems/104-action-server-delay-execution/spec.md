# 104. Action Server: Delay Execution

**Difficulty:** 🟡 Medium  
**Category:** Actions  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

"Wait actions" are used in behavior trees. "Docking" is an action that takes time and reports progress.

## Problem Statement

## Problem Statement
Implement an action that simulates work by sleeping. This tests your understanding of concurrency in Actions.

### Requirements
- Action Name `sleep_action`
- Goal: `seconds` (int)
- Feedback: `time_left`
- Result: `success` (bool)
- Logic: Sleep for `seconds`, publishing feedback every 1s.

### Input/Output Format
**Input:**
- Goal: 5 seconds

**Output:**
- Feedback: 4, 3, 2, 1
- Result: True

### ⚠️ Common Pitfalls
- Blocking the main thread if not using `MultiThreadedExecutor` or async/await patterns.

### 📚 Helpful Resources
- [Action Servers](https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html)

## Test Cases

- **DelayWorks:** N seconds delay
- **PublishesFeedback:** feedback messages

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
