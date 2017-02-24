#!/usr/bin/python

from pycocotools.coco import COCO
import numpy as np
import pylab
import xml.dom.minidom
import  xml.etree.ElementTree as ET


def writeXML(imageid,bbox,bboxName):
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root)

    nodefolder = doc.createElement('folder')
    nodefolder.appendChild(doc.createTextNode(str('sheng')))
    root.appendChild(nodefolder)

    nodefilename = doc.createElement('filename')
    filename = (coco.loadImgs(int(imageid)))[0]['file_name']
    nodefilename.appendChild(doc.createTextNode(str(filename)))
    root.appendChild(nodefilename)

    nodesize = doc.createElement('size')

    sizewid = doc.createElement('width')
    width = (coco.loadImgs(int(imageid)))[0]['width']
    sizewid.appendChild(doc.createTextNode(str(width)))
    nodesize.appendChild(sizewid)

    sizehe = doc.createElement('height')
    height = (coco.loadImgs(int(imageid)))[0]['height']
    sizehe.appendChild(doc.createTextNode(str(height)))
    nodesize.appendChild(sizehe)

    sizede = doc.createElement('depth')
    sizede.appendChild(doc.createTextNode('3'))
    nodesize.appendChild(sizede)

    root.appendChild(nodesize)

    nodeseg = doc.createElement('segmented')
    nodeseg.appendChild(doc.createTextNode(str('0')))
    root.appendChild(nodeseg)

    for nameID in range(len(bboxName)):
        name = bboxName[nameID]
        for eachbbox in bbox[nameID]:
            # save object
            nodeobj = doc.createElement('object')

            objname = doc.createElement('name')
            objname.appendChild(doc.createTextNode(str(name).replace(' ','')))
            nodeobj.appendChild(objname)

            objpose = doc.createElement('pose')
            objpose.appendChild(doc.createTextNode(str('Unspecified')))
            nodeobj.appendChild(objpose)

            objtrun = doc.createElement('truncated')
            objtrun.appendChild(doc.createTextNode(str('0')))
            nodeobj.appendChild(objtrun)

            objdiff = doc.createElement('difficult')
            objdiff.appendChild(doc.createTextNode(str('0')))
            nodeobj.appendChild(objdiff)

            objbndbox = doc.createElement('bndbox')

            objbndxmin = doc.createElement('xmin')
            objbndxmin.appendChild(doc.createTextNode(str(int(eachbbox[0]))))
            objbndbox.appendChild(objbndxmin)

            objbndymin = doc.createElement('ymin')
            objbndymin.appendChild(doc.createTextNode(str(int(eachbbox[1]))))
            objbndbox.appendChild(objbndymin)

            objbndxmax = doc.createElement('xmax')
            objbndxmax.appendChild(doc.createTextNode(str(int(eachbbox[2]))))
            objbndbox.appendChild(objbndxmax)

            objbndymax = doc.createElement('ymax')
            objbndymax.appendChild(doc.createTextNode(str(int(eachbbox[3]))))
            objbndbox.appendChild(objbndymax)

            nodeobj.appendChild(objbndbox)
        # you need to add to root
        root.appendChild(nodeobj)


    fp = open('/home/sheng/COCO/coco/coco_train/Annotations/'+'%06d'%imageid+'.xml','w')
    doc.writexml(fp,indent='\t',addindent='\t',newl='\n')
    fp.close()




if __name__ == '__main__':

    annFile = '/home/sheng/COCO/coco/coco_data/annotations/instances_train2014.json'
    coco = COCO(annFile)

    file_all = open('/home/sheng/COCO/coco/coco_train/ImageSets/Main/all_train.txt')
    lines = [int(line.strip()) for line in file_all.readlines()]

    catNMS = ['person', 'cup', 'bottle', 'potted plant',
              'tv', 'mouse', 'keyboard', 'cell phone',
              'book', 'teddy bear', 'toilet', 'backpack',
              'handbag', 'orange', 'apple', 'bed',
              'refrigerator', 'couch', 'vase', 'chair']

    for image_id in range(len(lines)):

        # lines[image_id]: image name
        bboxAnn = []
        bboxName = []
        for cat in catNMS:
            catID = coco.getCatIds(catNms=cat)
            annID = coco.getAnnIds(imgIds=int(lines[image_id]), catIds=catID, iscrowd=False)  # include box
            # annID: ann info for each label in one image
            if annID != []:
                bboxAnn.append(annID)
                bboxName.append(cat)

                # now bboxAnn [[],[]] has save the whoile annotation that one image has

        bbox = []
        # convert the bboxAnn to bbox_bbox, which convert the Ann's id to bbox information
        for each_cat in bboxAnn:
            tem = []
            for one_ann_id in each_cat:
                tem.append((coco.loadAnns(int(one_ann_id)))[0]['bbox'])
            bbox.append(tem)
        #
        # np.save('./imageid.npy',image_id)
        # np.save('./bbox.npy',bbox)
        # np.save('./bboxname.npy',bboxName)

        writeXML(int(lines[image_id]), bbox, bboxName)
