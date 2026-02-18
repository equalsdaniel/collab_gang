"""Launch file to start the navigation scripts (state estimator + frontier + navigator).

This launch file runs the Python scripts in `ros2_ws/src/navigation` directly using
`ExecuteProcess` and sets `PYTHONPATH` so the local modules (e.g., `asl_tb3_lib`,
`mod_asl3_lib`) are importable. This is a convenience for development; when
packaging navigation as a ROS2 package you can replace these with `Node` entries.

Usage:
    ros2 launch tidybot_bringup navigation.launch.py
"""

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, ExecuteProcess
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    # Ensure PYTHONPATH includes ros2_ws/src
    pythonpath = os.path.join(workspace_root, 'ros2_ws', 'src')

    state_estimator_cmd = [
        'python3', os.path.join(workspace_root, 'ros2_ws', 'src', 'navigation', 'base_state_estimator.py')
    ]

    frontier_cmd = [
        'python3', os.path.join(workspace_root, 'ros2_ws', 'src', 'navigation', 'frontier_exploration.py')
    ]

    astar_cmd = [
        'python3', os.path.join(workspace_root, 'ros2_ws', 'src', 'navigation', 'astar_navigator.py')
    ]

    return LaunchDescription([
        ExecuteProcess(
            cmd=state_estimator_cmd,
            name='base_state_estimator',
            output='screen',
            additional_env={'PYTHONPATH': pythonpath}
        ),
        ExecuteProcess(
            cmd=frontier_cmd,
            name='frontier_explorer',
            output='screen',
            additional_env={'PYTHONPATH': pythonpath}
        ),
        ExecuteProcess(
            cmd=astar_cmd,
            name='astar_navigator',
            output='screen',
            additional_env={'PYTHONPATH': pythonpath}
        ),
    ])
