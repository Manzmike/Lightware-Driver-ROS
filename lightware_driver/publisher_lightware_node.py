import os
import pkg_resources
import serial
import time

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range


class LightwareDriver(Node):

    def __init__(self):
        super().__init__('lightware_driver')
        self.publisher_ = self.create_publisher(Range, 'lightware_node', 10)

        timer_period = 0.01667  # seconds 60 Hz's
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.serialPortName = '/dev/ttyACM0'
        self.serialPortBaudRate = 115200
        self.port = serial.Serial(self.serialPortName, self.serialPortBaudRate)


    def timer_callback(self):
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
            
        temp_val = self.port.readline().decode('utf8')
        print(f"temp val:{temp_val}")


        splitStr = temp_val.split()
        distance = float(splitStr[0])

        msg.range = distance
        msg.min_range = 0.001
        msg.max_range = 249.99


        if(distance > 0.1 and distance < 249.9):
            self.publisher_.publish(msg)

       
def main(args=None):
    rclpy.init(args=args)

    lightware_driver = LightwareDriver()

    rclpy.spin(lightware_driver)


    lightware_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()