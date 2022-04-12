import os
import launch

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from app_common_modules.remappings import get_remappings


def generate_launch_description():

    config_dir = os.path.join(get_package_share_directory('bobcat_tests'), 'config')

    remappings = get_remappings(config_dir)

    start_daq_comms_node = Node(
        package='daq_comms',
        executable='daq_comms_node',
        parameters=[os.path.join(config_dir, 'daq_comms.yaml')],
        remappings=remappings,
        output='screen'
    )

    start_imu_filter_node = Node(
        package='imu_filter_madgwick',
        executable='imu_filter_madgwick_node',
        parameters=[os.path.join(config_dir, 'imu.yaml')],
        remappings=remappings,
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(start_daq_comms_node)
    ld.add_action(start_imu_filter_node)

    return ld
