# 021. Services - Basic Service Server

**Difficulty:** 🔴 Hard  
**Category:** ROS2 Services  
**Tags:** `services`, `server`, `request-response`, `python`, `ros2`  
**Execution Type:** `basic_python`  

**Frequency:** high  

## 💡 Why This Problem Matters

Use Services for quick, blocking operations like "Grip Object", "Calibrate Sensor", or "Get Map". Don't use them for continuous data (use Topics) or long-running tasks (use Actions).

## Problem Statement

## Problem Statement
Services provide a synchronous Request/Response communication pattern. Create a service server that adds two integers.

### Requirements
- Create a node named `add_two_ints_server`
- Create a service named `add_two_ints`
- Service Type: `example_interfaces/AddTwoInts`
- Callback: Sums `request.a` and `request.b` into `response.sum`
- Log "Incoming request: a=[a] b=[b]" inside the callback

### Input/Output Format
**Input:**
- Service Request: `a=2`, `b=3`

**Output:**
- Service Response: `sum=5`
- Console Log: "Incoming request: a=2 b=3"

### ⚠️ Common Pitfalls
- Returning `None` instead of `response`.
- Forgetting to import the service type definition.

### 📚 Helpful Resources
- [ROS2 Services Tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html)

## Similar Problems

- Problem #19
- Problem #20

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
