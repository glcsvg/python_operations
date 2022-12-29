import glob
from os import listdir, getcwd
from os.path import join
from os import path

img_path2 = '/home/dell/Desktop/image'

img_path = glob.glob('/home/dell/Desktop/images2/*.jpg')
for a in img_path:

    img = img_path2 + '/'+ ( a.split('.')[0]).split('/')[-1] + '.jpg'
    if not path.exists(img):
        pass       
    else:
        #pass
        print("Exist..",a)
