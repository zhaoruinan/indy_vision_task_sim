import time
import numpy as np
import threading
from time import sleep
import pybullet as p
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class ImagePublisher(Node):
    def __init__(self):
        # Initiate the Node class's constructor and give it a name
        super().__init__('image_publisher')
        # Create the publisher. This publisher will publish an Image
        # to the video_frames topic. The queue size is 10 messages.
        self.rgb_ = self.create_publisher(Image, 'bullet_camera/rgbimg', 10)
        self.depth_ = self.create_publisher(Image, 'bullet_camera/depth', 10)
        # We will publish a message every 0.1 seconds
        timer_period = 0.1    # seconds
        # Create the timer
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # Used to convert between ROS and OpenCV images
        self.br = CvBridge()
    def timer_callback(self):
        """
        Callback function.
        This function gets called every 0.1 seconds.
        """
        # Capture frame-by-frame
        # This method returns True/False as well
        # as the video frame.
        #global rgbImg
        rgbImg,depthImg = camera()
        print(depthImg.shape)
        #depthImg = depthImg *127+128
        depthImg = (depthImg* 255*3-255*2).astype(np.uint8)  
        print(depthImg)
        #cv2.imshow("depthImg", depthImg)
        rgbImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGBA2RGB)
        #depthImg =  cv2.cvtColor(depthImg, cv2.COLOR_BGR2GRAY)
        #depthImg = cv2.cvtColor(depthImg, cv2.COLOR_RGBA2RGB)
        print(depthImg.shape)
        #self.publisher_.publish(self.br.cv2_to_imgmsg(rgbImg[:]))
        self.rgb_.publish(self.br.cv2_to_imgmsg(rgbImg,encoding="rgb8"))
        self.depth_.publish(self.br.cv2_to_imgmsg(depthImg ,encoding="passthrough")) 
        # Display the message on the console
        self.get_logger().info('Publishing video frame')
    
def main(args=None):
    rclpy.init(args=args)
    print('Hi from ros2_sim_indy_pybullet.')
    objects = ['apple', 'orange', 'banana', 'milk', 'orange']
    p.connect(p.GUI)
    p.setGravity(0, 0, -9.8)
    TableId = p.loadURDF("src/ros2_sim_indy_pybullet/ros2_sim_indy_pybullet/table/table.urdf", [0.45, 0.35, -0.65])
    indyId= p.loadURDF("src/ros2_sim_indy_pybullet/ros2_sim_indy_pybullet/indy7.urdf", [0, 0, 0])
    num_obj = len(objects)
    obj_postions = np.random.rand(num_obj,2)
    z_postion = np.empty(num_obj); z_postion.fill(0.2)
    obj_postions = np.c_[ obj_postions, z_postion ] 
    print(obj_postions)
    for object in objects:
        obj_path = "src/ros2_sim_indy_pybullet/ros2_sim_indy_pybullet/models/urdf/"+object+".urdf"
        objId = p.loadURDF(obj_path, obj_postions[-1,])
        obj_postions = np.delete(obj_postions, -1, 0)
    p.resetBasePositionAndOrientation(indyId, [0, 0, 0.03], [0, 0, 0, 1])
    p.setRealTimeSimulation(1) 
    # Create the node
    image_publisher = ImagePublisher()    
    # Spin the node so the callback function is called.
    rclpy.spin(image_publisher)    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_publisher.destroy_node()
    rclpy.shutdown()
    p.disconnect()
def camera():
    viewMatrix = p.computeViewMatrix(
        cameraEyePosition=[0.3, 0.3, 1.5],
        cameraTargetPosition=[0.3, 0.3, 0],
        cameraUpVector=[0, 1, 0])
    projectionMatrix = p.computeProjectionMatrixFOV(
        fov=45.0,
        aspect=1.0,
        nearVal=0.1,
        farVal=3.1)
    width, height, rgbImg, depthImg, segImg = p.getCameraImage(
        width=224,
        height=224,
        viewMatrix=viewMatrix,
        projectionMatrix=projectionMatrix)
    return rgbImg,depthImg
if __name__ == '__main__':
    main()
