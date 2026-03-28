# 103. Service Server: Multiply Two Floats

**Difficulty:** 🟢 Easy  
**Category:** Services  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

"Get Inverse Kinematics" or "Plan Path" are often implemented as services that take a goal and return a plan.

## Problem Statement

## Problem Statement
Create a computation service. This is a common pattern for offloading heavy math or logic.

### Requirements
- Node `multiplier_service`
- Service `multiply_floats`
- Type (custom or example): `example_interfaces/AddTwoInts` (Adapt logic) or if `Floats` available use that. 
- *Update: Use `example_interfaces/AddTwoInts` but pretend they are floats for the logic vs use `my_interfaces/MultiplyFloats` if indicated.* 
- **Assumption:** Use `example_interfaces/AddTwoInts` (since it's standard) but just multiply them.

### Input/Output Format
**Input:**
- Request (a, b)

**Output:**
- Response (product)

### ⚠️ Common Pitfalls
- Using the wrong field names of the service type.

### 📚 Helpful Resources
- [Services](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html)

## Test Cases

- **MultiplyPositive:** correct product
- **MultiplyNegative:** correct product

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
