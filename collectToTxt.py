#!/usr/bin/python

from pycocotools.coco import COCO
import numpy as np
import pylab

annFile ='/home/sheng/COCO/coco/coco_data/annotations/instances_val2014.json'
coco = COCO(annFile)

catNMS=['person','cup','bottle','potted plant',
            'tv','mouse','keyboard','cell phone',
            'book','teddy bear','toilet','backpack',
            'handbag','orange','apple','bed',
            'refrigerator','couch','vase','chair']

# catIds = coco.getCatIds(catNms=catNMS) # !!! not map to the same place above

all_txt = open('/home/sheng/COCO/coco/coco_test/ImageSets/Main/all_test.txt','a')
all_set = set()
file_path = []

for each_obj in catNMS:
    catIds = coco.getCatIds(catNms=each_obj)
    imgIds = coco.getImgIds(catIds=catIds) #imgIds
    file = open('/home/sheng/COCO/coco/coco_test/ImageSets/Main/'+each_obj.replace(' ','')+'_test.txt','a')

    for id in imgIds:
        file.writelines(str('%06d'%id)+'\n')
        all_set.add(id)
    file.close()

all_set = list(all_set)
for set in all_set:
    all_txt.writelines(str('%06d'%set)+'\n')
all_txt.close()

