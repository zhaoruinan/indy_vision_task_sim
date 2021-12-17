# README

# indy7_ign_moveit

make vision environment

## add rgab_camera

![Screenshot from 2021-12-17 12-32-23.png](README%201f82af5bb26a4dae80e549e6c7e14acd/Screenshot_from_2021-12-17_12-32-23.png)

indy7_ign_moveit2-main/worlds/indy7_follow.sdf

```xml
<!--line266-310 -->
<!-- RGBD camera -->
<link name="link">
    <pose relative_to="indy7::indy7_link7">0 0.05 0 0 -1.57 0</pose>
    <visual name="visual">
    <geometry>
        <box>
        <size>0.02 0.02 0.05</size>
        </box>
    </geometry>
    </visual>
    <sensor name="rgbd_camera" type="rgbd_camera">
<!-- camera parameter -->
    <camera>
        <horizontal_fov>1.047</horizontal_fov>
        <image>
        <width>320</width>
        <height>240</height>
        </image>
        <clip>
        <near>0.1</near>
        <far>100</far>
        </clip>
    </camera>
    <always_on>1</always_on>
    <update_rate>30</update_rate>
    <visualize>true</visualize>
    <topic>rgbd_camera</topic>
    <enable_metrics>true</enable_metrics>
    </sensor>
</link>
</model>
```

## add ros_ign_bridge


indy7_ign_moveit2_main/launch/ign_moveit2.launch.py

- add RGDB Image bridge

![Screenshot from 2021-12-17 12-32-38.png](README%201f82af5bb26a4dae80e549e6c7e14acd/Screenshot_from_2021-12-17_12-32-38.png)

```xml
ros2 run rqt_image_view rqt_image_view /rgbd_camera/image
```

- add RGDB camera info bridge

```xml
ros2 topic echo /rgdb_camera/camera_info
```
