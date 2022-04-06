#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Accel
from std_msgs.msg import Float32
import math

class Listener():

  def __init__(self):
      rospy.init_node('listener', anonymous=True)
      rospy.Subscriber("entregavel", Accel, self.callback)
      self.pub = rospy.Publisher('valoreslinear', Float32, queue_size=10)
      self.pub2 = rospy.Publisher('valoresangular', Float32, queue_size=10)
  
  def callback(self, msg):
      linearx, lineary, linearz = msg.linear.x, msg.linear.y, msg.linear.z  
      quadrados = linearx**2 + lineary**2 + linearz*2
      resultado = math.sqrt(quadrados)
      f = Float32()
      f.data = resultado
      self.pub.publish(f)

      angularx, angulary, angularz = msg.angular.x, msg.angular.y, msg.angular.z
      quadrados2 = angularx**2 + angulary**2 + angularz*2
      resultado2 = math.sqrt(quadrados2)
      f2 = Float32()
      f2.data = resultado2
      self.pub2.publish(f2)



if __name__ == '__main__':
    l = Listener()
    rospy.spin()