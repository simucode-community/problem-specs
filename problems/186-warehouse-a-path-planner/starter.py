import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped
import heapq
import numpy as np
import math

class AStarPlanner(Node):
    """
    A* path planning implementation for warehouse navigation.
    
    TODO: Implement A* search with efficient priority queue
    TODO: Handle dynamic obstacle updates
    TODO: Optimize memory usage
    """
    
    def __init__(self):
        super().__init__('astar_planner')
        
        # Subscribers
        self.map_sub = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10
        )
        
        self.start_sub = self.create_subscription(
            PoseStamped,
            '/start_pose',
            self.start_callback,
            10
        )
        
        self.goal_sub = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.goal_callback,
            10
        )
        
        # Publisher
        self.path_pub = self.create_publisher(Path, '/planned_path', 10)
        
        # State
        self.current_map = None
        self.start_pose = None
        self.goal_pose = None
        
        # Planning parameters
        self.declare_parameter('heuristic_type', 'euclidean')  # or 'manhattan'
        self.declare_parameter('occupancy_threshold', 50)  # 0-100
        
        self.get_logger().info('A* Planner Ready')
    
    def heuristic(self, a, b):
        """
        Heuristic function for A*.
        
        TODO: Implement Manhattan or Euclidean distance
        """
        heuristic_type = self.get_parameter('heuristic_type').value
        
        if heuristic_type == 'manhattan':
            # Manhattan distance (L1 norm)
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        else:
            # Euclidean distance (L2 norm)
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
    def plan(self, start, goal, grid):
        """
        A* path planning algorithm.
        
        TODO: Implement A* search
        TODO: Use heapq for priority queue
        TODO: Return path as list of waypoints
        """
        if grid is None:
            self.get_logger().warn('No map available')
            return []
        
        height, width = grid.shape
        
        # Validate start and goal
        if not self.is_valid(start[0], start[1], grid):
            self.get_logger().error(f'Start position {start} is invalid')
            return []
        
        if not self.is_valid(goal[0], goal[1], grid):
            self.get_logger().error(f'Goal position {goal} is invalid')
            return []
        
        # TODO: Initialize open and closed sets
        # Open set: priority queue of (f_score, counter, node)
        # counter prevents comparison of nodes when f_scores are equal
        open_set = []
        counter = 0
        heapq.heappush(open_set, (0, counter, start))
        counter += 1
        
        # Track visited nodes
        closed_set = set()
        
        # Cost from start to node
        g_score = {start: 0}
        
        # Estimated total cost (g + h)
        f_score = {start: self.heuristic(start, goal)}
        
        # Parent tracking for path reconstruction
        came_from = {}
        
        # 8-connected grid (or use 4-connected for simpler navigation)
        neighbors = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # 4-connected
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonals
        ]
        
        # TODO: A* main loop
        while open_set:
            # Get node with lowest f_score
            current_f, _, current = heapq.heappop(open_set)
            
            # Goal reached
            if current == goal:
                return self.reconstruct_path(came_from, current)
            
            # Skip if already processed
            if current in closed_set:
                continue
            
            closed_set.add(current)
            
            # Explore neighbors
            for dx, dy in neighbors:
                neighbor = (current[0] + dx, current[1] + dy)
                
                # Check if valid
                if not self.is_valid(neighbor[0], neighbor[1], grid):
                    continue
                
                # Skip if already processed
                if neighbor in closed_set:
                    continue
                
                # Calculate cost
                # Diagonal moves cost sqrt(2), straight moves cost 1
                move_cost = math.sqrt(2) if abs(dx) + abs(dy) == 2 else 1.0
                tentative_g = g_score[current] + move_cost
                
                # If this path to neighbor is better
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor, goal)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, counter, neighbor))
                    counter += 1
        
        # No path found
        self.get_logger().warn('No path found to goal')
        return []
    
    def reconstruct_path(self, came_from, current):
        """Reconstruct path from goal to start."""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
    
    def is_valid(self, x, y, grid):
        """
        Check if cell is traversable.
        
        TODO: Check bounds and obstacles
        """
        height, width = grid.shape
        
        # Check bounds
        if x < 0 or x >= width or y < 0 or y >= height:
            return False
        
        # Check obstacle
        threshold = self.get_parameter('occupancy_threshold').value
        if grid[y, x] > threshold:  # Note: grid is [row, col] = [y, x]
            return False
        
        return True
    
    def grid_to_path_msg(self, grid_path, map_info):
        """Convert grid coordinates to Path message."""
        path_msg = Path()
        path_msg.header.stamp = self.get_clock().now().to_msg()
        path_msg.header.frame_id = 'map'
        
        for grid_x, grid_y in grid_path:
            pose = PoseStamped()
            pose.header.stamp = path_msg.header.stamp
            pose.header.frame_id = 'map'
            
            # Convert grid to world coordinates
            pose.pose.position.x = map_info.origin.position.x + grid_x * map_info.resolution
            pose.pose.position.y = map_info.origin.position.y + grid_y * map_info.resolution
            pose.pose.position.z = 0.0
            pose.pose.orientation.w = 1.0
            
            path_msg.poses.append(pose)
        
        return path_msg
    
    def world_to_grid(self, x, y, map_info):
        """Convert world coordinates to grid coordinates."""
        grid_x = int((x - map_info.origin.position.x) / map_info.resolution)
        grid_y = int((y - map_info.origin.position.y) / map_info.resolution)
        return (grid_x, grid_y)
    
    def map_callback(self, msg):
        """Store latest map."""
        # Convert occupancy grid to numpy array
        width = msg.info.width
        height = msg.info.height
        self.current_map = np.array(msg.data).reshape((height, width))
        self.map_info = msg.info
        
        self.get_logger().info(f'Received map: {width}x{height}')
        
        # Trigger replanning if we have start and goal
        if self.start_pose and self.goal_pose:
            self.compute_path()
    
    def start_callback(self, msg):
        """Store start pose."""
        self.start_pose = msg
        self.get_logger().info(f'Start: ({msg.pose.position.x:.2f}, {msg.pose.position.y:.2f})')
        
        # Trigger planning if we have all inputs
        if self.current_map is not None and self.goal_pose:
            self.compute_path()
    
    def goal_callback(self, msg):
        """Store goal pose."""
        self.goal_pose = msg
        self.get_logger().info(f'Goal: ({msg.pose.position.x:.2f}, {msg.pose.position.y:.2f})')
        
        # Trigger planning if we have all inputs
        if self.current_map is not None and self.start_pose:
            self.compute_path()
    
    def compute_path(self):
        """Compute and publish path."""
        if self.current_map is None or self.start_pose is None or self.goal_pose is None:
            return
        
        # Convert world coordinates to grid
        start_grid = self.world_to_grid(
            self.start_pose.pose.position.x,
            self.start_pose.pose.position.y,
            self.map_info
        )
        
        goal_grid = self.world_to_grid(
            self.goal_pose.pose.position.x,
            self.goal_pose.pose.position.y,
            self.map_info
        )
        
        self.get_logger().info(f'Planning from {start_grid} to {goal_grid}')
        
        # Plan path
        import time
        start_time = time.time()
        grid_path = self.plan(start_grid, goal_grid, self.current_map)
        planning_time = time.time() - start_time
        
        if grid_path:
            self.get_logger().info(
                f'Path found: {len(grid_path)} waypoints in {planning_time*1000:.1f}ms'
            )
            
            # Convert to Path message and publish
            path_msg = self.grid_to_path_msg(grid_path, self.map_info)
            self.path_pub.publish(path_msg)
        else:
            self.get_logger().error('Failed to find path')

def main(args=None):
    rclpy.init(args=args)
    node = AStarPlanner()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
