import cv2
img=cv2.imread('banana.jpg')
dim=img.shape
print(dim)
cv2.imshow('Original Image',img)
cv2.waitKey(0)      #without this the image will be displayed only for 1 ms. this will make the image to be shown till some key is entered

''' part  '''

some_pixel=img[300:400,500:1000]  #to access a particluar pixel img[x,y]
cv2.imshow('pixel',some_pixel)
cv2.waitKey(0)

''' gray or any scale'''

gray_Scale=cv2.imread('banana.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('GRAY SCALE',gray_Scale)
cv2.waitKey(0)

'''deleting some part'''

to_delete=cv2.imread('random.jpg')
to_delete[0:100,0:200]=0
cv2.imshow('deleted',to_delete)
cv2.waitKey(0)

'''  bgr --> rgb and chnages incorporated'''

img_bgr=cv2.imread('banana.jpg')
cv2.imshow('original',img_bgr)
cv2.waitKey(0)
b,g,r=cv2.split(img_bgr)
changed_rgb=cv2.merge([r,g,b])
cv2.imshow('rgb',changed_rgb)
cv2.waitKey(0)



""" playing with bgr"""


img_bgr=cv2.imread('banana.jpg')
b,g,r=cv2.split(img_bgr)
b-=20
r-=20
g-=20
changed_rgb=cv2.merge([b,g,r])
cv2.imshow('original',img_bgr)
cv2.imshow('rgb',changed_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()