

import pyrealsense2 as rs
import cv2
import numpy as np
import os


pipeline = rs.pipeline()
config = rs.config()
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)




Ncamera_frames = 1000

count = 0
if __name__ == '__main__':

    # Detect a shape
    for countframes in range(0, Ncamera_frames):

      # Wait for a coherent pair of frames: depth and color
      frames = pipeline.wait_for_frames()
      color_frame = frames.get_color_frame()
      

      # Convert images to numpy arrays
      color_image = np.asanyarray(color_frame.get_data())

      cv2.imshow('RealSense', color_image)
      cv2.waitKey(3)

      filename = os.path.join("Images", "frame_" + str(count) + ".jpg")
      cv2.imwrite(filename, color_image)

      count = count + 1
