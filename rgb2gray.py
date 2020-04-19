import os
import shutil
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


if __name__ == "__main__":
    IMG_DIR = "./JPEGImages"  # 需要灰度化的图片文件夹路径
    XML_DIR = "./Annotations"  # 需要灰度化的XML文件夹路径

    # 灰度化
    for root, sub_folders, files in os.walk(XML_DIR):

        for name in files:

            img_ori = os.path.join(IMG_DIR, name[:-4] + '.jpg')
            img_gray = os.path.join(IMG_DIR, name[:-4] + '_gray' + '.jpg')
            rgb2gray(img_ori, img_gray)

            shutil.copy(os.path.join(XML_DIR, name[:-4] + '.xml'), os.path.join(XML_DIR, name[:-4] + '_gray' + '.xml'))
