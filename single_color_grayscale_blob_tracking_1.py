# Single Color Grayscale Blob Tracking Example
#
# This example shows off single color grayscale tracking using the OpenMV Cam.

import sensor, image, time

# Color Tracking Thresholds (Grayscale Min, Grayscale Max)
# The below grayscale threshold is set to only find extremely bright white areas.
thresholds = (65, 255)

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
sensor.set_auto_exposure(False, \
      exposure_us = int(6000))
clock = time.clock()

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" merges all overlapping blobs in the image.

while(True):
    clock.tick()
    # Take a picture
    img = sensor.snapshot()

    # Find all the "blobs" (see note above about thresholds)
    blobs = img.find_blobs([thresholds], pixels_threshold=100, area_threshold=100, merge=True)

    # IF there's two blobs and they're rotated at the right angle, then figure out where the target is
    if len(blobs) == 2:
        if (((blobs[0]).rotation()*180/3.14 > 90) and ((blobs[1]).rotation()*180/3.14 < 90)) \
        or (((blobs[0]).rotation()*180/3.14 < 90) and ((blobs[1]).rotation()*180/3.14 > 90)):

            # Draw where we think the rectangles are
            for blob in blobs:
                img.draw_rectangle(blob.rect(), thickness=5)
                img.draw_cross(blob.cx(), blob.cy())
                #print(blob.area())
               # print(blob.rotation()*180/3.14)

            # Calculate the distance between the two blobs in pixels
            distance = abs(blobs[0].cx() - blobs[1].cx())
            to_target = -(distance - 390) / 5.8

            #find the point in the center of the two blobs, in pixels from center of image
            center = (blobs[0].cx() + blobs[1].cx()) / 2 - img.width() / 2
            print(center)

            #find the rotation of the robot

           # print( to_target)
            #print(blobs[0].pixels())
#            #print(center)
            #print(img.width())
            angle_1 = blobs[1].rotation()
            angle_0 = blobs[0].rotation()
            #print(angle_1)
            #print(angle_0)

            # to do (first two are done):
            # 1) how far away is the target? (sort of done, see "distance")
            # 2) where is the target? (done for left/right: "center")
            # 3) what angle is the target? (should we rotate the robot?)

#    else: print( len(blobs))
       # if (blob[1]).rotation()*180/3.14 > 90:
#    for blob in img.find_blobs([thresholds], pixels_threshold=100, area_threshold=100, merge=True):
        #img.draw_rectangle(blob.rect(), thickness=5)
        #img.draw_cross(blob.cx(), blob.cy())
 #       if blob.rotation()*180/3.14 < 90:
  #          print("red")
   #     if blob.rotation()*180/3.14 >90:
    #        print("blue")

        #print(blob.rotation()*180/3.14)
        #color blobs with positive angle blue
        #color blobs with negative angle red
        #if we have one positive on the left, and one negative on the right, color them both green
