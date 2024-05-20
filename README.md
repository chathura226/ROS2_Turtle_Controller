# ROS2_Turtle_Controller
This ROS2 project is to demonstrate basic usage of ROS2 colcon workspace and ROS2 topic,services,nodes.

## Controlling turtlesim node using a custom package


In this project I have created a package that can interact with turtlesim node using various methods

- Usage of 'Topics' to create custom publishers, subscribers to control turtle
- Usage of 'Service; to change settings of turtle

After building the project and sourcing, use following to start turtle simulation node.
```
ros2 run turtlesim turtlesim_node
```
Then use following to try 
  - draw_circle : Turtle moving in circular path (Publishing to a topic)
  - pose_subscriber : Gives current coordinates of turtle (Subscribing to a topic)
  - turtle_controller : Turtle moves around without hitting walls and changes pen color (Usage of services , publishing and subscribing to a topic)

```
ros2 run my_robot_controller draw_circle
ros2 run my_robot_controller pose_subscriber
ros2 run my_robot_controller turtle_controller
```

# Usage of custom docker template
For this project I have used my custom docker template for easier development. Can check that out using following link:
```
https://github.com/chathura226/ROS2_Docker_Template
```




