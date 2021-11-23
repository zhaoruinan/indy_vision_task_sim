# indy_vision_task_sim

PBL기반로봇제어

Indy 시뮬레이터에 음성+비전 인식 기반 작업 Plug-in

## "사과 집어 하면 사과 인식해서 집는 것"

### ros2+vnc docker img 사용:
```
git clone https://github.com/zhaoruinan/indy_vision_task_sim.git
cd indy_vision_task_sim
cd docker-ros2-desktop-vnc/foxy
docker build -t zrn/ros2-vnc-terminator
docker run -p 6080:80 --rm  zrn/ros2-vnc-terminator
```
Run with source code directory:
```
docker run -p 6080:80 --rm -v Your_Directory_of_robot_ws:/home/ubuntu/robot_ws zrn/ros2-vnc-terminator
```
Task list:
- [x] Choose platform for simulation: pybullet, mujoco
- [ ] Add simulation development envirment to docker file.
- [ ] Choose voice recognition solution
- [ ] 
- [ ] 
