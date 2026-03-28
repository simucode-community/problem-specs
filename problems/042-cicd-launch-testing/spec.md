# 042. CI/CD - Launch Testing

**Difficulty:** 🔴 Hard  
**Category:** Integration Testing  
**Tags:**   
**Execution Type:** `launch_file`  


## 💡 Why This Problem Matters

Manual testing is unscalable. Launch tests run automatically on every Pull Request to ensure new code doesn't break existing simulations or hardware drivers.

## Problem Statement

## Problem Statement
Write a `launch_testing` script to verify that a node starts up and publishes data correctly. This is unit testing for entire processes.

### Requirements
- Create a test file `test_launch.py`
- Define `generate_test_description`
- Start a `talker` node
- Use `unittest` to verify it publishes to `/chatter` (or just check process exit code for this exercise)

### Input/Output Format
**Output:**
- A passing test execution.

### ⚠️ Common Pitfalls
- Not giving the process enough time to start before asserting.

### 📚 Helpful Resources
- [Launch Testing Tutorial](https://github.com/ros2/launch/tree/humble/launch_testing)

## Test Cases

- **Launch test:** launch_testing used
- **Multi-node test:** Multiple nodes tested
- **Post-shutdown:** Exit codes checked

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
