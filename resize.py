from PIL import Image
import glob


img_file = '/home/dell/Desktop/face-mask-detection/NMSK'
img_list = glob.glob(img_file + '/*.jpg')

for i in img_list:
    img = Image.open(i)
    name=(i.split('.')[0]).split('/')[-1]+'.jpg'
    print(name,img.size[0],img.size[1])
    # baseheight = 544
    # hpercent = (baseheight / float(img.size[1]))
    # wsize = int((float(img.size[0]) * float(hpercent)))

    img = img.resize((224,224), Image.ANTIALIAS)

    # if wsize < 960:
    #     print(".....................")
    img.save('/home/dell/Desktop/face-mask-detection/newNMSK/' + name, 'JPEG')
    # else:
    #     pass
       #img.save('/home/dell/Desktop/SCUT/496_672/amax/' + name, 'JPEG')


