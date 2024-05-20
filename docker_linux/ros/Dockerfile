FROM osrf/ros:humble-desktop-full

#to make default shell bash - to make 'source' command work
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update

#if want to convert dos2unix files
RUN sudo apt install -y dos2unix

RUN sudo apt install -y python3-pip 

#colcon is a build tool
RUN sudo apt install -y python3-colcon-common-extensions

#for setup global ros2 installation 
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

#to setup autocomplete
RUN echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc

#to source bashrc so that it reflect changes
RUN source ~/.bashrc

RUN cd ~ && \
    mkdir ros2_ws && \
    cd ros2_ws && \
    mkdir src && \
    colcon build --symlink-install
# --symlink-install no need to build everytime we change the python files

#to setup custom workspace we created
RUN echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
RUN source ~/.bashrc