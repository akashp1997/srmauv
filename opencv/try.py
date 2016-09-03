import cv2
import numpy

#reading the image
img = cv2.imread('buoysf.jpg',1)


#useless snippet
"""circle_co = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,2.5,80,
                            param1=50,param2=30,minRadius=12,maxRadius=20)

circle_co = numpy.uint16(numpy.around(circle_co))"""

def pseudo(x):
    pass

#global variable buoy_co which contains buoy center coordinates
buoy_co = ""

def render(x):
    global buoy_co
    #switch to render image; error correction
    if x==0:
        return None

    """Getting the parameters of HSV of the image from the trackbars"""
    hmin = cv2.getTrackbarPos('hMin', 'HueComp')
    hmax = cv2.getTrackbarPos('hMax', 'HueComp')

    smin = cv2.getTrackbarPos('sMin', 'SatComp')
    smax = cv2.getTrackbarPos('sMax', 'SatComp')

    vmin = cv2.getTrackbarPos('vMin', 'SatComp')
    vmax = cv2.getTrackbarPos('vMax', 'SatComp')

    #converting image to hsv
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue,sat,val = cv2.split(img_hsv)
    #thresholding image according to user input of hsv
    hThresh = cv2.inRange(numpy.array(hue),numpy.array(hmin), numpy.array(hmax))
    sThresh = cv2.inRange(numpy.array(sat),numpy.array(smin), numpy.array(smax))
    vThresh = cv2.inRange(numpy.array(val),numpy.array(vmin), numpy.array(vmax))
    #threshold image for selection to further processing
    thres_img = cv2.bitwise_and(hThresh,sThresh)
    cv2.imshow('HSVFiltered', thres_img)
    #img_filtered = cv2.bitwise_and(hThresh,cv2.bitwise_and(sThresh,vThresh))
    conf = cv2.waitKey(0)
    if chr(conf).lower()=='y':
        cv2.destroyWindow('Render')
        #Blurring the image to avoid false positives
        gray = cv2.GaussianBlur(thres_img,(9,9), 2, 2)
        buoy_co = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,2.5,80, \
                                     param1=50,param2=30,minRadius=8,maxRadius=26)
        buoy_co = numpy.uint16(numpy.around(buoy_co))
        cv2.destroyAllWindows()
        #center stored to buoy_co variable globally
        draw()
        return None
    cv2.destroyWindow('Render')
    cv2.namedWindow('Render')
    cv2.createTrackbar('switch', 'Render', 0, 1, render)

cv2.namedWindow('HueComp')
cv2.namedWindow('SatComp')
cv2.namedWindow('ValComp')
cv2.namedWindow('Render')



cv2.createTrackbar('hMin', 'HueComp', 10, 179, pseudo)
cv2.createTrackbar('hMax', 'HueComp', 40, 179, pseudo)
cv2.createTrackbar('sMin', 'SatComp', 100, 255, pseudo)
cv2.createTrackbar('sMax', 'SatComp', 255, 255, pseudo)
cv2.createTrackbar('vMin', 'ValComp', 190, 255, pseudo)
cv2.createTrackbar('vMax', 'ValComp', 255, 255, pseudo)
t = cv2.createTrackbar('switch', 'Render', 0, 1, render)

"""while True:


    hmin = cv2.getTrackbarPos('hMin', 'HueComp')
    hmax = cv2.getTrackbarPos('hMax', 'HueComp')

    smin = cv2.getTrackbarPos('sMin', 'SatComp')
    smax = cv2.getTrackbarPos('sMax', 'SatComp')

    vmin = cv2.getTrackbarPos('vMin', 'SatComp')
    vmax = cv2.getTrackbarPos('vMax', 'SatComp')

    #Thresholding
    hThresh = cv2.inRange(numpy.array(hue),numpy.array(hmin), numpy.array(hmax))
    sThresh = cv2.inRange(numpy.array(sat),numpy.array(smin), numpy.array(smax))
    vThresh = cv2.inRange(numpy.array(val),numpy.array(vmin), numpy.array(vmax))

    img_filtered = cv2.bitwise_and(hThresh,cv2.bitwise_and(sThresh,vThresh))
    break
"""
def draw():
    global buoy_co
    for i in buoy_co[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('img',img)


print buoy_co
#cv2.imshow('Buoys',img)
#cv2.imshow('Image', img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
