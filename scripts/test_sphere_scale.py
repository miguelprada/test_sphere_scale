#!/usr/bin/env python

import rospy

from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

rospy.init_node( 'test_sphere_scale' )

pub = rospy.Publisher( "test_sphere_scale", MarkerArray, queue_size = 1 )

marker_array = MarkerArray()

sphere_marker = Marker()

sphere_marker.header.frame_id = '/world'
sphere_marker.ns = "spheres"
sphere_marker.id = 1
sphere_marker.type = Marker.SPHERE
sphere_marker.action = Marker.ADD

sphere_marker.pose.position.x = 0.5
sphere_marker.pose.orientation.w = 1.0

sphere_marker.scale.x = 0.1
sphere_marker.scale.y = 0.2
sphere_marker.scale.z = 0.3

sphere_marker.color.r = 1.0
sphere_marker.color.a = 1.0

marker_array.markers.append( sphere_marker )

sphere_list_marker = Marker()

sphere_list_marker.header.frame_id = '/world'
sphere_list_marker.ns = "spheres"
sphere_list_marker.id = 2
sphere_list_marker.type = Marker.SPHERE_LIST
sphere_list_marker.action = Marker.ADD

sphere_list_marker.pose.position.x = -0.5
sphere_list_marker.pose.orientation.w = 1.0

sphere_list_marker.scale.x = 0.1
sphere_list_marker.scale.y = 0.2
sphere_list_marker.scale.z = 0.3

sphere_list_marker.color.g = 1.0
sphere_list_marker.color.a = 1.0

sphere_list_marker.points.append( Point() )

marker_array.markers.append( sphere_list_marker )

while not rospy.is_shutdown():

    pub.publish( marker_array )
    rospy.sleep( 0.1 )
