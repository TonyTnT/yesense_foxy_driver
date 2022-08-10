from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="yesense_imu",
            executable="yesense_imu_node",
            name="yesense_imu_node",
            output="screen",
            emulate_tty=True,
            parameters=[
                {"port": "/dev/yesense_imu"},
                {"baud_rate": 460800},
                {"tf_parent_frame_id": "imu_base"},
                {"tf_frame_id": "imu_link"},
                {"frame_id": "imu_link"}
            ]
        )
    ])