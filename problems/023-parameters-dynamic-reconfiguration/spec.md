# 023. Parameters - Dynamic Reconfiguration

**Difficulty:** 🟡 Medium  
**Category:** Parameters  
**Tags:** `parameters`, `dynamic`, `reconfigure`, `validation`  
**Execution Type:** `basic_python`  

**Frequency:** high  

## 💡 Why This Problem Matters

Prevents operators from setting dangerous values (e.g., setting robot speed to 100 m/s) while the robot is running.

## Problem Statement

## Problem Statement
Implement a parameter callback to validate and react to parameter changes at runtime.

### Requirements
- Node `param_validator`
- Parameter `max_speed` (double, default: 1.0)
- Add a callback `add_on_set_parameters_callback`
- Validation Logic: Reject negative values or values > 10.0
- If valid, update the parameter and log "Speed updated to X"
- If invalid, reject the change and log "Invalid speed"

### Input/Output Format
**Output:**
- Logs indicating success or failure of parameter updates.

### ⚠️ Common Pitfalls
- Not returning a `SetParametersResult` object causes the parameter client to hang or error.

### 📚 Helpful Resources
- [Parameter Callbacks](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python.html#using-parameters-in-a-class-python)

## Similar Problems

- Problem #12
- Problem #22

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
