# hand_urdf_discription

![Screenshot from 2022-06-03 16-23-37](https://user-images.githubusercontent.com/40191598/171807711-2bd708b4-ef03-4bdb-b5b6-6e91d5b93c4c.png)




## To visulize 4-finger hand with joint coupler node
```
roslaunch hand_urdf_discription hand_display.launch
```

### Finger index
* 1 : Thumb
* 2 : Index
* 3 : Middle
* 4 : Ring


**'/hand_joint_coupler'** node subscribe **'/hand_joint_command'**(JointState with 8 joint position values) and publish **'/joint_states'**(JointState with 20 joint values). Publishing rate of '/joint_states' is 200 Hz.
The message '/hand_joint_command' requires 8 joint position values(rad) and the order of it is [AA1, AA2, AA3, AA4, FE1 .FE2. FE3. FE4].
Please check example codes below.




### Example code
#### Flexion-Extension mode
```
rosrun hand_urdf_description command_tester.py
```

#### Adduction-Abduction mode
```
rosrun hand_urdf_description command_tester2.py
```
