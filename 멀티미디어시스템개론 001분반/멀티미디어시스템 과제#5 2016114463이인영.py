import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from multiprocessing import Process

road = []
query = []

result = [[]]

def init_s():
    num = 0
    global road
    global query
    for i in range(1,151) :
        num += 1
        tmp = str(num)
        while len(tmp) < 3:
            tmp = "0" + tmp
        tmp += ".jpg"
        img1 = cv.imread(tmp,cv.IMREAD_GRAYSCALE)
        road.append(img1)
        print(tmp + " is import")

    num = 0
    for i in range(1,11) :
        num += 1
        tmp = str(num)
        while len(tmp) < 2:
            tmp = "0" + tmp
        tmp = "query" + tmp + ".jpg"
        img2 = cv.imread(tmp,cv.IMREAD_GRAYSCALE)
        query.append(img2)
        print(tmp + " is import")


def a(tb,img2,road) : 
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    top = [0,0,0]
    top_img = [0,0,0]
    num = 0
    for img1 in road :
        num+=1
        print(str(tb) + " " + str(num) + "th work")
        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1,None)
        kp2, des2 = sift.detectAndCompute(img2,None)
        # BFMatcher with default params
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)
        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.5*n.distance:
                good.append([m])
        st = 0
        for i in range(3) :
            if(top[i] < len(good)) :
                for j in reversed(range(i,2)) : 
                    top[j+1] = top[j]
                    top_img[j+1] = top_img[j]
                top[i] = len(good)
                top_img[i] = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                break
        # cv.drawMatchesKnn expects list of lists as matches.    
    for i in  range(3) :
        cv.imwrite("query"+ str(tb+1)+" top" + str(i+1) +" "+str(top[i])+".png" , top_img[i])
if __name__ == '__main__':
    init_s()
    p=[0]*10
    for i in range(len(p)):
        Process(target=a, args=(i,query[i],road)).start()


