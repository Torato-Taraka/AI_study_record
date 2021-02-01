from PIL import Image
import pytesseract
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np
import cv2
"""
img = Image.open('text\\2.png')
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)
"""

def recognize(image):
    text = pytesseract.image_to_string(image, lang='chi_sim')
    print(text)

def show_image(image):
    i = Image.fromarray(image)
    i.show()
    
def px_filter(image, min_px, max_px):
    for i in range(len(image)):
        for j in range(len(image[0])):
            if sum(image[i][j]) > min_px and sum(image[i][j]) < max_px:
                image[i][j] = np.array([255, 255, 255])
            else:
                image[i][j] = np.array([0, 0, 0])
    return image
    
def Chinese_OCR(image, target):
    file = open(target, 'w+')
    # 读取图像
    image = cv2.cv2.imread(image)
    # 像素过滤，二值化
    # min_px, max_px = 90, 600
    #px = px_filter(image, min_px, max_px)
    #show_image(px)
    # 调整对比度
    #img_contrast = cv2.convertScaleAbs(image, alpha = 1.5, beta = 0)
    # 灰度图像
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #show_image(gray)
    # 图像归一化
    #img_normalize = cv2.normalize(gray, 100, 250, cv2.NORM_MINMAX, cv2.CV_8U)
    #show_image(gray)
    # 均衡化
    #img_equalize = cv2.equalizeHist(gray)
    # 二值化  设置阈值
    #thresh = 190
    #ret, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    #cv2.bitwise_not(binary, binary)
    #show_image(binary)
    # 识别
    test_message = Image.fromarray(px)
    text = pytesseract.image_to_string(test_message, lang='chi_sim')
    print(text)
    file.write(text)

"""
import getopt
import sys
def main(argv):
    try:
        options, args = getopt.getopt(argv, "hp:i:", ["help", "ip=", "port="])
    except getopt.GetoptError:
        sys.exit()

    for option, value in options:
       if option in ("-h", "--help"):
           print("help")
       if option in ("-i", "--ip"):
           print("ip is: {0}".format(value))
       if option in ("-p", "--port"):
           print("port is: {0}".format(value))
    
    print("error args: {0}".format(args))
    
if __name__ == '__main__':
    main(sys.argv[1:])
"""

if __name__ == '__main__':
    #Chinese_OCR("text\\1.png", "text\\1.txt")
    #Chinese_OCR("text\\2.png", "text\\2.txt")
    #Chinese_OCR("text\\3.jpg", "text\\3.txt")
    Chinese_OCR("text\\4.jpg", "text\\4.txt")
