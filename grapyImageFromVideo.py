#!/usr/local/bin/python

'''

for gopro's file structure 

├── Cam01
│   ├── 327
│   ├── elevator
│   └── windows
├── Cam02
│   ├── 327
│   ├── elevator
│   └── windows
├── Cam03
│   ├── 327
│   ├── elevator
│   └── windows
├── Cam04
│   ├── 327
│   ├── elevator
│   └── windows
├── Cam05
│   ├── 327
│   ├── elevator
│   └── windows
├── Cam06
    ├── 327
    ├── elevator
    └── windows


'''

import  cv2
import  os
import shutil


cam_num = 1
path = './Cam0'

# assume only one video in '327' 
video_file = '327'

image_size = 1

# allImageIndex means image's index
allImageIndex = 1

if os.path.exists('./output') == False:
    os.mkdir('./output')

# for each camera
while cam_num < 7:
    video_path = os.path.join(path+str(cam_num),video_file)
    filelist = os.listdir(video_path)
    video = []
    for x in filelist:
        if x[-3:] == 'mp4':
            video = x

    if video != []:
        fp = cv2.VideoCapture( os.path.join(video_path, str(video[0])) )
    else:
        print('ERROR, no video in ['+video_path+']')
        exit(-1)

    # for each video, grasp image_size
    imgsize = 0
    while imgsize < image_size:
        fx,img = fp.read()
        cv2.imwrite( os.path.join('./output',str(allImageIndex)+'.jpg'),img)
        allImageIndex = allImageIndex + 1

    fp.close()




