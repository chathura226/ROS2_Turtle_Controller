If using editor inside windows to change files in src, make sue to use END OF LINE SEQUENCE as 'LF' so that it uses unix system ending
or coonfigure endofline to '\n' instead of '\r'
or else you can use dos2unix convertor inside the container too


rqt_graph
ros2 topic list
ros2 node list
ros2 topic info <topic>
ros2 topic hz <topic>
ros2 node info <node>
ros2 interface show <data type of topic >


ros topics are mainly for publisher subscriber pattern

to make a request and et a response like in client server , we can use ros services

in rqt_graph , we cannot see services

we can make req to services using cmd:
ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{'r':0,'g':0,'b':0,'width':1,'off':0}"