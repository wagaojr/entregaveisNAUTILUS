#!/usr/bin/env python3

import rospy 
import tf2_ros
import math
from geometry_msgs.msg import TransformStamped


rospy.init_node('sistemasolar', anonymous=True)
broadcaster = tf2_ros.TransformBroadcaster()

class sistemasolar():
    def __init__(self, planeta, raio):
        
        self.raio = raio
        self.tf = TransformStamped()
        self.tf.header.frame_id = 'sol'
        self.tf.child_frame_id = planeta
        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.rotation.w = 1
        self.tf.transform.translation.x = 1
        self.tf.transform.translation.y = 2    
        self.tf.transform.translation.z = 0

    def translation(self):
        variavel = 2* rospy.Time.now().to_sec() * math.pi / (self.raio**(3/2) * 60)
        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.translation.x = self.raio * math.cos(variavel)
        self.tf.transform.translation.y = self.raio * math.sin(variavel)
        self.tf.transform.translation.z = 0
        
        broadcaster.sendTransform(self.tf) 

raioterra = rospy.get_param("planetas/Terra/raio")
raiovenus = rospy.get_param("planetas/Venus/raio")
raiomercurio = rospy.get_param("planetas/Mercurio/raio")
raiomarte = rospy.get_param("planetas/Marte/raio")
raiojupiter = rospy.get_param("planetas/Jupiter/raio")
raiosaturno = rospy.get_param("planetas/Saturno/raio")
raiourano = rospy.get_param("planetas/Urano/raio")
raionetuno = rospy.get_param("planetas/Netuno/raio")

planetas = [sistemasolar("Terra",raioterra),
            sistemasolar("Venus",raiovenus),
            sistemasolar("Mercurio",raiomercurio),
            sistemasolar("Marte",raiomarte),
            sistemasolar("Jupiter",raiojupiter),
            sistemasolar("Saturno",raiosaturno),
            sistemasolar("Urano",raiourano),
            sistemasolar("Netuno",raionetuno),]


if __name__ == '__main__':
   
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():

        for i in planetas:
            i.translation()
        rate.sleep()    

