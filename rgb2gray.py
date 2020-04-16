import cv2


def rgb2gray(file1, file2):
    img = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(file2, img)
    print('%s已转为灰色图%s' % (file1, file2))


def rgb2binary(file1, file2):
    img = cv2.imread(file1)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grayimg, 12, 255, cv2.THRESH_TOZERO)
    cv2.imwrite(file2, thresh)
    print('%s已转为二值图%s' % (file1, file2))


f1 = '1.jpg'
f2 = '2.jpg'
f3 = '3.jpg'
rgb2gray(f1, f2)
rgb2binary(f1, f3)
