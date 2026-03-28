# 028. Gazebo - Spawn Model

**Difficulty:** 🟡 Medium  
**Category:** Gazebo Simulation  
**Tags:** `gazebo`, `spawn`, `simulation`, `service`  
**Execution Type:** `gazebo_sim`  

**Frequency:** medium  

## 💡 Why This Problem Matters

Automated testing environments need to spawn robots and obstacles dynamically at the start of each test scenario.

## Problem Statement

## Problem Statement
Programmatically spawn a robot model into the Gazebo simulation using the `/spawn_entity` service.

### Requirements
- Create a node `spawner`
- Service Client for `/spawn_entity` (`gazebo_msgs/srv/SpawnEntity`)
- Request arguments:
  - `name`: "my_robot"
  - `xml`: Simple Box URDF string
  - `initial_pose`: (0,0,1)

### Input/Output Format
**Output:**
- Successfully calls service to spawn object.

### ⚠️ Common Pitfalls
- Call blocking `call()` inside a callback (causes deadlock). Use `call_async()`.

### 📚 Helpful Resources
- [Gazebo Service API](https://classic.gazebosim.org/tutorials?tut=ros2_comm)

## Similar Problems

- Problem #29
- Problem #30

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
