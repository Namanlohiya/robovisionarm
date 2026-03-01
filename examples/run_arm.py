from robovisionarm import RoboVisionArm

arm = RoboVisionArm(

    port="COM3",
    camera_index=0
)

arm.run()