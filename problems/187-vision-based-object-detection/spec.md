# 187. Vision-Based Object Detection

**Difficulty:** 🔴 Hard  
**Category:** Perception & Vision  
**Tags:** `python`, `ros2`, `opencv`, `computer-vision`, `perception`  
**Execution Type:** `ros2_python_node`  

**Seen at:** KUKA, ABB, Rethink Robotics, Covariant  
**Frequency:** high  

## 💡 Why This Problem Matters

This pipeline is essential for pick-and-place robots in manufacturing (KUKA, ABB, Rethink Robotics). Real-time object detection and accurate pose estimation enable automated bin picking, assembly, and quality inspection tasks.

## Problem Statement

## Problem Statement

Build a **real-time object detection and pose estimation pipeline** using computer vision that identifies objects and publishes their 6-DOF poses for robotic manipulation.

### Requirements

Your vision pipeline must:
- **Detect objects with ≥90% accuracy** (9/10 objects detected)
- **Process frames with <200ms latency** per frame
- **Estimate 6-DOF pose** with position error ≤2cm and rotation error ≤5°
- **Handle varying lighting conditions** (3 different scenarios)
- Integrate a **pre-trained deep learning model** (YOLO/SSD)
- Use **PnP algorithm** for pose estimation

### Input/Output Format

**Input:**
- Camera images on `/camera/image_raw` (sensor_msgs/Image)
- Camera calibration parameters (intrinsic matrix)

**Output:**
- Detected object poses on `/detected_objects` (geometry_msgs/PoseArray)
- Annotated images on `/detection/image` (sensor_msgs/Image) [optional]
- Must log **"Object Detection Node Ready"** when initialized

## Test Cases

- **Detection Accuracy:** 9/10 objects detected
- **Latency:** ≤200ms per frame
- **Pose Error:** Position ≤2cm, Rotation ≤5°
- **Lighting Robustness:** Works in 3 lighting scenarios

## Similar Problems

- Problem #34
- Problem #135
- Problem #148

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
