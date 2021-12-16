# Enables command line input
import sys
 
from yolo_interfaces.srv import YoloInterface
import rclpy
from rclpy.node import Node
 
class MinimalClientAsync(Node):
 
    def __init__(self):
        # Create a client    
        super().__init__('minimal_client_async')
        self.cli = self.create_client(YoloInterface, 'yolo_det')
       
        # Check if the a service is available  
        while not self.cli.wait_for_service(timeout_sec=10.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = YoloInterface.Request()
 
    def send_request(self):
        self.req.img_ros_topic = sys.argv[1]
        self.future = self.cli.call_async(self.req)
 
 
def main(args=None):
    rclpy.init(args=args)
 
    minimal_client = MinimalClientAsync()
    minimal_client.send_request()
 
    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        # See if the service has replied
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Yolo det Result of image topic: for %s is %s  %s' %
                    (minimal_client.req.img_ros_topic, str(response.success), response.message))
            break
 
    minimal_client.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()