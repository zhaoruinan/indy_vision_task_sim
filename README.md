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
cp -r src/ Your_Directory_of_robot_ws/src
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
## Task list:
- [x] Choose platform for simulation: pybullet, mujoco
- [x] Add simulation development envirment to docker file.
- [ ] Choose voice recognition solution
- [ ] Simple demo

## License
## Acknowledgements
This Dockerfile is based on [tiryoh/ros2-desktop-vnc:foxy](https://github.com/Tiryoh/docker-ros2-desktop-vnc)., licensed under the Apache License 2.0.