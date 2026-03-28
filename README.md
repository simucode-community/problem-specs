# SimuCode Problem Specs

> Open specifications for all ROS2 practice problems on [simucode.online](https://simucode.online)

[![Problems](https://img.shields.io/badge/Problems-49-cyan)](./problems)
[![Platform](https://img.shields.io/badge/Platform-simucode.online-blue)](https://simucode.online)
[![ROS2](https://img.shields.io/badge/ROS2-Humble-orange)](https://docs.ros.org/en/humble)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-green)](./LICENSE)

---

## What is this?

SimuCode is a browser-based ROS2 practice platform — think LeetCode but for robotics.  
Write code in the browser, run it in a real ROS2 Humble container, get instant pass/fail feedback.

This repository contains the **open specifications** for every problem:
- `spec.md` — problem description, requirements, test cases, learning objectives
- `starter.py` — the starter code students see in the editor
- `hints.json` — progressive hints (levels 1-3)

> **Note:** TestScripts and reference solutions are maintained privately by the SimuCode team.  
> This keeps grading integrity intact while making problem content open for improvement.

---

## Problem List

| # | Problem | Difficulty | Category |
|---|---------|-----------|----------|
|   1 | [Simple Publisher](./problems/001-simple-publisher/spec.md) | 🟢 Easy | ROS2 Basics |
|   2 | [Command Line - Topic Echo](./problems/002-command-line-topic-echo/spec.md) | 🟢 Easy | CLI Tools |
|   3 | [Workspace Structure - Package Creation](./problems/003-workspace-structure-package-creation/spec.md) | 🟢 Easy | Package Management |
|   4 | [Environment Setup - Parameter Sourcing](./problems/004-environment-setup-parameter-sourcing/spec.md) | 🟡 Medium | ROS2 Basics |
|   5 | [Python - OOP Node Creation](./problems/005-python-oop-node-creation/spec.md) | 🟢 Easy | Python for ROS2 |
|   6 | [Python - Type Hints & Logging](./problems/006-python-type-hints-logging/spec.md) | 🟡 Medium | Python for ROS2 |
|   7 | [C++ - Smart Pointers Node](./problems/007-c-smart-pointers-node/spec.md) | 🟡 Medium | C++ for ROS2 |
|   8 | [Python - Multi-threading Executor](./problems/008-python-multi-threading-executor/spec.md) | 🔴 Hard | Python for ROS2 |
|   9 | [C++ vs Python - Performance Comparison](./problems/009-c-vs-python-performance-comparison/spec.md) | 🟡 Medium | Language Comparison |
|  10 | [URDF - Simple Robot Description](./problems/010-urdf-simple-robot-description/spec.md) | 🟢 Easy | URDF |
|  11 | [Xacro - Parameterized Robot](./problems/011-xacro-parameterized-robot/spec.md) | 🟡 Medium | Xacro |
|  12 | [YAML - Parameter Loading](./problems/012-yaml-parameter-loading/spec.md) | 🟢 Easy | YAML Configuration |
|  15 | [Python Launch - Basic Node Launch](./problems/015-python-launch-basic-node-launch/spec.md) | 🟢 Easy | Python Launch |
|  16 | [Launch Arguments & Substitutions](./problems/016-launch-arguments-substitutions/spec.md) | 🟡 Medium | Python Launch |
|  17 | [Conditional Launch](./problems/017-conditional-launch/spec.md) | 🟡 Medium | Advanced Launch |
|  18 | [Include Launch Files](./problems/018-include-launch-files/spec.md) | 🔴 Hard | Advanced Launch |
|  19 | [Topics - Custom Message](./problems/019-topics-custom-message/spec.md) | 🟡 Medium | Topics |
|  20 | [QoS - Reliable vs Best Effort](./problems/020-qos-reliable-vs-best-effort/spec.md) | 🔴 Hard | Topics |
|  21 | [Services - Basic Service Server](./problems/021-services-basic-service-server/spec.md) | 🔴 Hard | ROS2 Services |
|  22 | [Actions - Fibonacci with Feedback](./problems/022-actions-fibonacci-with-feedback/spec.md) | 🔴 Hard | Actions |
|  23 | [Parameters - Dynamic Reconfiguration](./problems/023-parameters-dynamic-reconfiguration/spec.md) | 🟡 Medium | Parameters |
|  24 | [Static Transform Broadcaster](./problems/024-static-transform-broadcaster/spec.md) | 🟢 Easy | TF2 Broadcasting |
|  25 | [Dynamic Transform Broadcaster](./problems/025-dynamic-transform-broadcaster/spec.md) | 🟡 Medium | TF2 Broadcasting |
|  28 | [Gazebo - Spawn Model](./problems/028-gazebo-spawn-model/spec.md) | 🟡 Medium | Gazebo Simulation |
|  32 | [Navigation - Waypoint Publisher](./problems/032-navigation-waypoint-publisher/spec.md) | 🟡 Medium | Navigation (Nav2) |
|  36 | [Debugging - Node Diagnostics](./problems/036-debugging-node-diagnostics/spec.md) | 🟢 Easy | Debugging Tools |
|  37 | [Data Recording - Custom Bag Recorder](./problems/037-data-recording-custom-bag-recorder/spec.md) | 🟡 Medium | rosbag2 |
|  41 | [Code Quality - Linting](./problems/041-code-quality-linting/spec.md) | 🟢 Easy | Code Quality |
|  42 | [CI/CD - Launch Testing](./problems/042-cicd-launch-testing/spec.md) | 🔴 Hard | Integration Testing |
|  43 | [DDS Discovery - Participant Filtering](./problems/043-dds-discovery-participant-filtering/spec.md) | 🔴 Hard | ROS2 Core |
|  44 | [Lifecycle Node - State Machine](./problems/044-lifecycle-node-state-machine/spec.md) | 🟡 Medium | ROS2 Core |
|  45 | [QoS Profiles - Deadline & Lifespan](./problems/045-qos-profiles-deadline-lifespan/spec.md) | 🟡 Medium | ROS2 Core |
|  67 | [Cobot - IO Integration (Digital I/O)](./problems/067-cobot-io-integration-digital-io/spec.md) | 🟢 Easy | Cobot Programming |
| 101 | [Publish Robot Temperature Status](./problems/101-publish-robot-temperature-status/spec.md) | 🟢 Easy | Topics |
| 102 | [ROS2 Parameter: Dynamic Speed Update](./problems/102-ros2-parameter-dynamic-speed-update/spec.md) | 🟢 Easy | Parameters |
| 103 | [Service Server: Multiply Two Floats](./problems/103-service-server-multiply-two-floats/spec.md) | 🟢 Easy | Services |
| 104 | [Action Server: Delay Execution](./problems/104-action-server-delay-execution/spec.md) | 🟡 Medium | Actions |
| 105 | [Write Launch File for Multi-Robot Simulation](./problems/105-write-launch-file-for-multi-robot-simulation/spec.md) | 🟡 Medium | Launch |
| 150 | [Robust Grasp Pose Selector using Point Cloud Clustering](./problems/150-robust-grasp-pose-selector-using-point-cloud-clustering/spec.md) | 🔴 Hard | Manipulation |
| 151 | [Latency Measurement Utility for ROS2 Topics](./problems/151-latency-measurement-utility-for-ros2-topics/spec.md) | 🟡 Medium | Tools / Testing |
| 152 | [Design a Minimal MQTT Bridge for Sensor Topics](./problems/152-design-a-minimal-mqtt-bridge-for-sensor-topics/spec.md) | 🟡 Medium | Integration |
| 153 | [Differential Drive Odometry from Encoder Pulses](./problems/153-differential-drive-odometry-from-encoder-pulses/spec.md) | 🟡 Medium | Kinematics |
| 154 | [Multi-Robot Task Allocator (Greedy)](./problems/154-multi-robot-task-allocator-greedy/spec.md) | 🟡 Medium | Multi-Robot |
| 155 | [Robust YAML Launch Parameter Validator](./problems/155-robust-yaml-launch-parameter-validator/spec.md) | 🟡 Medium | Configuration |
| 183 | [The Sensor Fusion Latency Challenge](./problems/183-the-sensor-fusion-latency-challenge/spec.md) | 🔴 Hard | Real-Time Performance |
| 184 | [The RTOS Control Loop Stability](./problems/184-the-rtos-control-loop-stability/spec.md) | 🔴 Hard | Real-Time Systems |
| 185 | [Dynamic SLAM Reliability Test](./problems/185-dynamic-slam-reliability-test/spec.md) | 🔴 Hard | Localization & Mapping |
| 186 | [Warehouse A* Path Planner](./problems/186-warehouse-a-path-planner/spec.md) | 🔴 Hard | Motion Planning |
| 187 | [Vision-Based Object Detection](./problems/187-vision-based-object-detection/spec.md) | 🔴 Hard | Perception & Vision |

---

## How to Contribute

We welcome contributions to **problem specs** — not testscripts or solutions.

### What you can contribute
- ✅ Fix typos or unclear requirements in `spec.md`
- ✅ Improve or add hints in `hints.json`
- ✅ Suggest a new problem in [Discussions → 💡 Problem Ideas](https://github.com/simucode-community/problem-specs/discussions/categories/problem-ideas)
- ✅ Report a bug in [Discussions → 🐛 Bug Reports](https://github.com/simucode-community/problem-specs/discussions/categories/bug-reports)
- ✅ Share how you solved a problem in [Discussions → 🎯 Show & Tell](https://github.com/simucode-community/problem-specs/discussions/categories/show-tell)

### What we maintain privately
- ❌ TestScripts (grading logic)
- ❌ Reference solutions

### Steps to contribute a fix

1. Fork this repository
2. Edit the relevant `spec.md` or `hints.json`
3. Open a Pull Request with a clear description of what you changed and why
4. A maintainer will review within 48 hours

### How to suggest a new problem

Open a [Discussion in 💡 Problem Ideas](https://github.com/simucode-community/problem-specs/discussions/categories/problem-ideas) with:

```
**Problem Title:** [e.g. "ROS2 Action Server with Timeout Handling"]
**ROS2 Concept:** [e.g. rclpy actions, GoalHandle, CancelCallback]
**Difficulty:** Easy / Medium / Hard
**Why useful:** [e.g. "Addverb asks this in interviews. Tests whether you can handle preemption."]
**Example input/output:** [brief description]
```

The SimuCode team writes and validates the testScript. Once accepted, your name appears  
on the problem page as "Suggested by @username".

---

## Problem Template

When we build new problems based on community suggestions, we use this structure:

```
problems/
└── 050-your-problem-name/
    ├── spec.md          ← problem statement, requirements, test cases
    ├── starter.py       ← starter code students see
    └── hints.json       ← 3 progressive hints
```

---

## Community

- 💬 [Discussions](https://github.com/simucode-community/problem-specs/discussions) — ideas, bugs, solutions
- 🌐 [simucode.online](https://simucode.online) — the platform
- 📨 Built in Bengaluru, India by [@rrg2003](https://github.com/rrg2003)

---

## License

Problem specifications (descriptions, starter code, hints) are licensed under  
[Creative Commons Attribution 4.0](./LICENSE).  
The SimuCode platform and testscripts are proprietary.
