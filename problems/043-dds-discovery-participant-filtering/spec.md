# 043. DDS Discovery - Participant Filtering

**Difficulty:** 🔴 Hard  
**Category:** ROS2 Core  
**Tags:**   
**Execution Type:** `urdf_xacro`  


## 💡 Why This Problem Matters

In a warehouse with 50 robots, you don't want Robot A to hear Robot B's "Move Forward" command. DDS Domains isolate traffic.

## Problem Statement

## Problem Statement
Understand how ROS2 nodes discover each other. Configure a node to ignore participants from other domains or specific contexts (simulated filtering logic).

### Requirements
- Create a node `secure_node`
- Set the `ROS_DOMAIN_ID` environment variable (simulated check or parameter)
- Log "Operating in Domain ID: [value]"
- Ensure it can communicate only with nodes in the same domain (simulated by checking a 'domain' parameter)

### Input/Output Format
**Output:**
- Console Log confirming domain configuration.

### ⚠️ Common Pitfalls
- Forgetting that Domain ID must be an integer between 0 and 232 (approx).

### 📚 Helpful Resources
- [ROS2 DDS Concepts](https://docs.ros.org/en/humble/Concepts/About-Domain-ID.html)

## Test Cases

- **Config present:** DDS config snippet provided
- **Domain set:** domain id configured
- **Node launches:** ROS2 node started with DDS config

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
