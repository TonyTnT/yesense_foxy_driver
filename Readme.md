# ROS Foxy Driver fo Yesense IMU

## Introduction

This is a ros foxy driver for yesense imu sensor.
Source Code for ROS1 from https://github.com/HViktorTsoi/yesense_ros_driver


## Install Dependence

Asume that you are using **ROS Foxy** 

```
cd ros2_ws/src
git clone https://github.com/RoverRobotics-forks/serial-ros2.git
cd ..
colcon build --packages-select serial --symlink-install
```

## Build

```
cd src && git clone https://github.com/TonyTnT/yesense_ros2_driver.git
cd .. && colcon build --packages-select yesense_imu --symlink-install
```

## Usage

```shell
roslaunch yesense_imu yesense_imu.py
```

**note: **change the params in launch to your own
