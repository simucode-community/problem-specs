# 155. Robust YAML Launch Parameter Validator

**Difficulty:** 🟡 Medium  
**Category:** Configuration  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

Misconfiguration (e.g., max_vel=100) is a top cause of hardware damage. Validation at startup is a cheap insurance policy.

## Problem Statement

## Problem Statement
Validate configuration files before starting the robot to prevent runtime crashes.

### Requirements
- Node `config_validator`
- Read file `robot_params.yaml`
- Schema:
  - `max_vel`: float within [0.0, 5.0]
  - `name`: non-empty string
- Output: Log "Valid" or "Invalid: [Reason]"

### Input/Output Format
**Output:**
- Validation report in logs.

### ⚠️ Common Pitfalls
- Assuming the file exists (check `os.path.exists`).

### 📚 Helpful Resources
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

## Test Cases

- **DetectsMissingKey:** error reported
- **TypeMismatch:** error reported

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
