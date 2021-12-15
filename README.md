# Indy7+hand(panda hand) MoveIt2 

hand 추가로 달아서 gazebo에서 throw동작 수행하는 example 실행 가능
- rviz쪽에서는 잘 안 움직임

# 의존성
    ROS2 Foxy
    Ignition Fortress
    MoveIt 2
        Binary Install
        Source Build(권장)
    ros_ign
    Ignition package for indy7
        indy7_ign
        indy7_moveit2_config

## 1팀 예제에서 변경사항
- urdf, sdf, srdf 등 수정
- indy7_ign 의 urdf 파일 수정 
- indy7_moveit_config>launch 내부 move_group_action_server.launch.py & fake control파일 수정 : srdf2 디렉토리에서 불러오도록
- indy7_ign_moveit2>worlds 내부 indy7_throw.sdf 수정 : indy7 모델을 indywhand 디렉토리에서 불러오도록
- 그 밖의 throw 관련 파일 수정 

## 추가해야 할 것
- indy7_moveit_config>config 내부 .yaml 파일들 수정 필요

## 설치 및 세팅
- 해당 브랜치로 들어와서 git clone 수행 
- 환경변수 설정(필수!) : export IGN_GAZEBO_RESOURCE_PATH=~{개인ws}/src/indy7_ign-main:${GAZEBO_MODEL_PATH}

## 예제 실행
1. colcon build --symlink-install
2. source source ~/{개인ws}/install/setup.bash
3. ros2 launch indy7_ign_moveit2 example_throw.launch.py

## 참고 
- https://github.com/AndrejOrsula/ign_moveit2
- 1팀이 참고한 예제인 듯 함
