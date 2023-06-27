import os
import glob
import os.path
from os import path
import cv2
import random
from pathlib import Path
img_list = glob.glob('/home/dell/Desktop/face-mask-detection/labellar/train/images/*.jpg')
kitti_label_path = '/home/dell/Desktop/face-mask-detection/labellar/train/labels'
path = '/home/dell/Desktop/face-mask-detection/MSK'
path1 = '/home/dell/Desktop/face-mask-detection/NMSK'

for img in img_list:
    image = cv2.imread(img)
    
    #cv2.imshow('Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # #closing all open windo
    image_name = (img.split('/')[-1]).split('.')[0]

    filename = image_name + '.txt'
    print(filename)

    labelfilename = os.path.join(kitti_label_path,filename)
    with open(labelfilename) as txt_file:
        for (i, line) in enumerate(txt_file):
            # tmp = [int(t.strip()) for t in line.split()]
            tmp = line.split()
            xmin,ymin = int(float(tmp[4])), int(float(tmp[5]))
            xmax,ymax = int(float(tmp[6])), int(float(tmp[7]))
            crop_img = image[ymin:ymax, xmin:xmax]
            print(xmin,ymin,xmax,ymax)

            name_i =  'fmd' + str(random.randint(0,90000)) + '.jpg'

            print(type(crop_img))

            # if cls == 'mask':
            print("burda...............")

            if tmp[0] == 'Mask':
                print("mask")
                file_path = os.path.join(path , name_i)
            else :
                file_path = os.path.join(path1 , name_i)

            try:
                cv2.imwrite(file_path, crop_img)
            except:
                print('hata')

            # try:
            #     if temp[0] == 'Mask':
            #         print("mask")
            #         # file_path = os.path.join(path , name_i)
            #         # cv2.imwrite(file_path, crop_img)
            # except:
            #     print("An exception occurred")

           



            # if path.exists(path):
            #     cv2.imwrite(file_path, crop_img)
            # else:
            #     continue
    print(".........................")