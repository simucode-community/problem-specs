# 032. Navigation - Waypoint Publisher

**Difficulty:** 🟡 Medium  
**Category:** Navigation (Nav2)  
**Tags:** `navigation`, `nav2`, `waypoint`, `goal`  
**Execution Type:** `nav2`  

**Seen at:** Fetch Robotics, Clearpath  
**Frequency:** high  

## 💡 Why This Problem Matters

Patrolling robots (security, cleaning, warehouse delivery) execute lists of waypoints. In a real system, you'd use the `NavigateToPose` Action, but publishing to the goal topic is a simple interface for testing.

## Problem Statement

## Problem Statement
Send a sequence of navigation goals to the robot. This simulates a patrol mission.

### Requirements
- Create a node `patrol_node`
- Publisher: `/goal_pose` (`geometry_msgs/PoseStamped`)
- List of 3 waypoints (x,y)
- Publish the next waypoint every 5 seconds (simplification of waiting for arrival)

### Input/Output Format
**Output:**
- Publishes PoseStamped messages to `/goal_pose`.

### ⚠️ Common Pitfalls
- Publishing with an empty header (frame_id is crucial).

### 📚 Helpful Resources
- [Nav2 Documentation](https://navigation.ros.org/)

## Learning Objective

Send sequential waypoint goals to the Nav2 navigation stack

## Similar Problems

- Problem #33
- Problem #34

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
