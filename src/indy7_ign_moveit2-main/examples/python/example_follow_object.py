#!/usr/bin/env python3

from geometry_msgs.msg import Pose
from moveit2 import MoveIt2Interface
from rclpy.node import Node
import rclpy
import time
class ObjectFollower(Node):

    def __init__(self):
        super().__init__("object_follower")

        # Create a subscriber for object pose
        self.previous_object_pose_ = Pose()
        self.object_pose_sub_ = self.create_subscription(Pose, '/model/box/pose',
                                                         self.object_pose_callback, 1)

        # Create MoveIt2 interface node
        self.moveit2_ = MoveIt2Interface()

        # Spin up multi-threaded executor
        self.executor_ = rclpy.executors.MultiThreadedExecutor(2)
        self.executor_.add_node(self)
        self.executor_.add_node(self.moveit2_)
        self.executor_.spin()

    def object_pose_callback(self, pose_msg):
            self.throw(pose_msg.position)
            self.destroy_subscription(self._object_pose_sub)
            rclpy.shutdown()
            exit(0)

    def throw(self, object_position):
        a=1
        if (a==1) :
        # Open gripper
            self.moveit2_.gripper_open()
            self.moveit2_.wait_until_executed()
            a=3
        # if (a==2):
        #     # Move above object
        #     position = [object_position.x,
        #                 object_position.y+0.05, object_position.z + 0.1]
        #     quaternion = [1.0, 0.0, 0.0, 0.0]
        #     self.moveit2_.set_pose_goal(position, quaternion)
        #     self.moveit2_.plan_kinematic_path()
        #     self.moveit2_.execute()
        #     self.moveit2_.wait_until_executed()
        #     a=3
        if(a==3):
            # Move above object
            position = [object_position.x,
                        object_position.y+0.03, object_position.z + 0.05]
            quaternion = [1.0, 0.0, 0.0, 0.0]
            self.moveit2_.set_pose_goal(position, quaternion)
            self.moveit2_.plan_kinematic_path()
            self.moveit2_.execute()
            self.moveit2_.wait_until_executed()
            a=4
        if(a==4):
            # Close gripper
            self.moveit2_.gripper_close(width=0.05, speed=0.2, force=20.0)
            self.moveit2_.wait_until_executed()
            a=0




        # self.moveit2_.set_max_velocity(0.5)
        # self.moveit2_.set_max_acceleration(0.5)




        # if Yolo Object Detection executed and if voice recognition successed
        # only chase the ordered object
        # if()




    # def object_pose_callback(self, pose_msg):
    #     # Plan trajectory only if object was moved
    #     if self.previous_object_pose_ != pose_msg:
    #         self.GripperOpen()

    #         self.moveit2_.set_pose_goal([pose_msg.position.x,
    #                                         pose_msg.position.y+0.03,
    #                                         pose_msg.position.z+0.05],
    #                                     [pose_msg.orientation.x,
    #                                         pose_msg.orientation.y,
    #                                         pose_msg.orientation.z,
    #                                         pose_msg.orientation.w])
    #         self.moveit2_.plan_kinematic_path()
    #         self.moveit2_.execute()

    #         # Update for next callback
    #         self.previous_object_pose_ = pose_msg

    # def GripperOpen(self):
    #     self.moveit2_.gripper_open()
    #     self.moveit2_.wait_until_executed()

    # def GripperClose(self):

    #     self.moveit2_.gripper_close(width=0.02, speed=0.2, force=20.0)
    #     self.moveit2_.wait_until_executed()




def main(args=None):
    rclpy.init(args=args)

    _object_follower = ObjectFollower()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
