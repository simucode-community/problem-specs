# 150. Robust Grasp Pose Selector using Point Cloud Clustering

**Difficulty:** 🔴 Hard  
**Category:** Manipulation  
**Tags:** `grasping`, `manipulation`, `point-cloud`, `clustering`, `segmentation`, `normals`, `pose-estimation`, `pcl`  
**Execution Type:** `basic_python`  

**Seen at:** ABB, Universal Robots, NVIDIA, Boston Dynamics  
**Frequency:** high  

## 💡 Why This Problem Matters

"Bin Picking" is the holy grail of logistics. Robots must look into a bin of random parts, identify one, and pick it up reliably.

## Problem Statement

## Problem Statement
Analyze a 3D point cloud to find the best object to pick up. This involves clustering points and selecting a centroid.

### Requirements
- Node `grasp_selector`
- Subscribe: `/camera/points` (`sensor_msgs/PointCloud2`)
- Logic:
  1. Filter points (remove floor/background)
  2. Cluster remaining points (Euclidean clustering)
  3. Find the cluster with the most points
  4. Publish its centroid as a Pose

### Input/Output Format
**Input:**
- `sensor_msgs/PointCloud2`

**Output:**
- `/grasp_pose` (`geometry_msgs/PoseStamped`)

### ⚠️ Common Pitfalls
- Processing every single point (too slow). Voxel grid downsampling is usually step 1.

### 📚 Helpful Resources
- [PCL with ROS2](https://github.com/ros-perception/perception_pcl)

## Similar Problems

- Problem #148
- Problem #167
- Problem #160

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
