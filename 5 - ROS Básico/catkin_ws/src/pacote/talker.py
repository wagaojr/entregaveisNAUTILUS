#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Accel
import random

class Talker:

   def _init__(self, lista, pub): 
      self.pub = pub
      self.lista = lista

   def start(self):
       self.pub = rospy.Publisher('entregavel', Accel, queue_size=10)
       self.lista = list(range(10))
       rospy.init_node('talker', anonymous=True) 
       rate = rospy.Rate(10) 
       while not rospy.is_shutdown():
          vetorvelocidade = Accel()
          vetorvelocidade.linear.x = random.choice(self.lista)
          vetorvelocidade.linear.y = random.choice(self.lista)
          vetorvelocidade.linear.z = random.choice(self.lista)
          vetorvelocidade.angular.x = random.choice(self.lista)
          vetorvelocidade.angular.y = random.choice(self.lista)
          vetorvelocidade.angular.z = random.choice(self.lista)
          rospy.loginfo(vetorvelocidade)
          self.pub.publish(vetorvelocidade)
          rate.sleep()
 
if __name__ == '__main__':
    try:
        t = Talker()
        t.start()
    except rospy.ROSInterruptException:
        pass