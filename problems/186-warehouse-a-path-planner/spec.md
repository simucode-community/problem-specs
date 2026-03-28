# 186. Warehouse A* Path Planner

**Difficulty:** 🔴 Hard  
**Category:** Motion Planning  
**Tags:** `python`, `ros2`, `path-planning`, `astar`, `warehouse`  
**Execution Type:** `ros2_python_node`  

**Seen at:** Amazon, Ocado, AutoStore, GreyOrange  
**Frequency:** very-high  

## 💡 Why This Problem Matters

This problem is fundamental to every autonomous warehouse system deployed by Amazon, Ocado, and AutoStore. Efficient path planning directly impacts throughput in facilities with hundreds of robots operating simultaneously.

## Problem Statement

## Problem Statement

Implement an **efficient A* path planner** for a warehouse robot that finds near-optimal paths through dynamic obstacle fields while meeting strict performance requirements.

### Requirements

Your path planner must:
- **Find paths within 10% of optimal length** (compared to Dijkstra's solution)
- **Execute faster than baseline** median solution time
- **Use ≤100MB memory** during execution
- **Support dynamic replanning** when obstacles move or appear
- Use **Manhattan or Euclidean heuristic** for A* search

### Input/Output Format

**Input:**
- Occupancy grid on `/map` (nav_msgs/OccupancyGrid)
- Start pose on `/start_pose` (geometry_msgs/PoseStamped)
- Goal pose on `/goal_pose` (geometry_msgs/PoseStamped)

**Output:**
- Computed path on `/planned_path` (nav_msgs/Path)
- Must log **"A* Planner Ready"** when initialized

## Test Cases

- **Path Optimality:** Within 10% of Dijkstra's solution
- **Execution Time:** Faster than median baseline
- **Memory Usage:** ≤100MB
- **Dynamic Replanning:** Adapt when obstacles move

## Learning Objective

Implement A* path planning for a grid-based warehouse environment

## Similar Problems

- Problem #154
- Problem #155

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
