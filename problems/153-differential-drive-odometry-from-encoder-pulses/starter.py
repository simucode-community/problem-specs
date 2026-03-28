import math

def integrate_odometry(ticks_l, ticks_r, params):
    """
    Compute robot pose by integrating wheel encoder ticks.
    
    Args:
        ticks_l (int): Left wheel encoder count since last step
        ticks_r (int): Right wheel encoder count since last step
        params (dict): Robot parameters:
            - 'r': Wheel radius (meters)
            - 'L': Wheelbase width (meters)
            - 'N': Ticks per revolution
            - 'x': Previous x position
            - 'y': Previous y position
            - 'theta': Previous heading (radians)
            
    Returns:
        tuple: (new_x, new_y, new_theta)
    """
    # TODO: Calculate distance per tick
    # TODO: Calculate left and right wheel distances (dl, dr)
    # TODO: Calculate center distance (dc) and angle change (dtheta)
    # TODO: Update pose (x, y, theta)
    # TODO: Return new pose
    pass
