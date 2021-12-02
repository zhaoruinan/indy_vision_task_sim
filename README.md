# indy_vision_task_sim

## PBL기반로봇제어

# Indy 시뮬레이터에 음성+비전 인식 기반 작업 Plug-in

### "사과 집어 하면 사과 인식해서 집는 것"

## ros2+vnc docker img 사용:
```
git clone https://github.com/zhaoruinan/indy_vision_task_sim.git
cd indy_vision_task_sim/docker_ros2_foxy_vnc
docker build -t zrn/ros2-vnc-terminator .
docker run -p 6080:80 --rm  zrn/ros2-vnc-terminator
```
### Run with source code directory:
```
cd ..
cp -r src/ Your_Directory_of_robot_ws
docker run -p 6080:80 --rm -v Your_Directory_of_robot_ws:/home/ubuntu/robot_ws zrn/ros2-vnc-terminator
```
### Browse http://127.0.0.1:6080/.
![image](https://drive.google.com/uc?export=view&id=1y--w7AkzVEeZiPnKm2RK04HblnDSJOwY)

### Open terminator
![image](https://drive.google.com/uc?export=view&id=1vJrLM5m_PGW4r4tshQCVVFYkEQRlwaPT)
```
cd robot_ws/src/indy7_pybullet
python indy7_sim_test.py
```
![image](https://drive.google.com/uc?export=view&id=1OWpGmuWG2NcabbvsHzAyj8fhf3ymWNGM)

### Try Yolo_v4
```
cd ~/robot_ws/src
git clone https://github.com/AlexeyAB/darknet
cd darknet
```
Open Makefile and set as blew:
```
GPU=0
CUDNN=0
CUDNN_HALF=0
OPENCV=1
AVX=1
OPENMP=1
LIBSO=1  
ZED_CAMERA=0
ZED_CAMERA_v2_8=0 
```
After doing these changes,just exeute the following command.
```
make
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT' -O yolov4.weights -r -A 'uc*' -e robots=off -nd
```
Now try Yolo_v4 by the following command.
```
./darknet detect cfg/yolov4.cfg yolov4.weights data/person.jpg
```
![image](https://drive.google.com/uc?export=view&id=1Hdovr7VZ3_Ui6_pGOD8DN75uE3_nnTuZ)
This work is base on a work of https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/.

### Try camera in pybullet simulation env
```
cd robot_ws/src/indy7_pybullet
python indy7_fixed_cam.py
```
![image](https://drive.google.com/uc?export=view&id=1NJfLWYu2la53zWbTR2pf7rPufktNRMcT)
The 3D models is base on a work of https://github.com/reail-iitd/COL864-Task-Planning.
### Try Yolo_V4 with a camera by ROS2 in pybullet simulation env 
### Try grasping in pybullet simulation env
### Try GUI of ROS2 for our task
### Try GUI with voice recognitio
### Try to take all parts into one demo

## Task list:
- [x] Choose platform for simulation: pybullet, mujoco
- [x] Add simulation development envirment to docker file.
- [ ] Choose voice recognition solution
- [ ] Simple demo

## License
## Acknowledgements
This Dockerfile is based on [tiryoh/ros2-desktop-vnc:foxy](https://github.com/Tiryoh/docker-ros2-desktop-vnc)., licensed under the Apache License 2.0.
