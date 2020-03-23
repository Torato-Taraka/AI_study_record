"""
	说明一下可以修改的几个地方：
	1、string
	2、imgs = video2imgs("")里的内容，即你的视频名字
	3、fps
	4、videowriter = cv2.VideoWriter("***.avi",...)，***是你想做成的视频的名字
"""
import cv2

#string的选取是有限制的，不能是中文符
string = ".,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"
count = len(string)

number = 0

def video2imgs(video):
    """
        param video: 字符串，视频文件路径
        return 一个img的列表
    """
    #用来存放从视频中切出来的图片
    img_list = []
    
    #创建一个VideoCapture对象
    cap = cv2.VideoCapture(video)
    
    #如果cap对象初始化完成了，就返回true
    while cap.isOpened():
        #cap.read()返回两个值ret:表示是否读取到图像，frame:图像矩阵，ndarray数组
        ret, frame = cap.read()
        if ret:
            #frame就是这一帧一帧的图片信息
            img_list.append(frame)
        else:
            break
        
    #释放空间
    cap.release()
    
    return img_list

def img2video(img):
    """
        param img: 图像矩阵
        return 字符串列表
    """
    #img = cv2.imread('1.jpg')

    #获取图像分辨率信息，w用不到，是RGB颜色信息
    u, v, w = img.shape
    
    #新图
    new_img = img*0 + 255
    
    #灰度化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    for i in range(0, u, 6):
        for j in range(0, v, 6):
            #获取灰度信息（其实就是颜色的深浅，用来确定到底放哪个字符）
            pix = gray[i, j]
            #RGB颜色信息
            b, g, r = img[i, j]
            #选取放入的字符
            zifu = string[ int( ( ( count - 1 ) * pix ) / 256 ) ]
            #把字符放进新图里，参数依次是：目标，字符，放入位置，字体，大小，颜色，透明度
            cv2.putText(new_img, zifu, (j, i),
                        cv2.FONT_HERSHEY_COMPLEX, 0.2,
                        (int(b), int(g), int(r)), 1)
    
    return new_img

    
if __name__ == "__main__":
    #当然你可以换成自己的视频名称
    imgs = video2imgs("1.mp4")
        
    #fps可以通过右键你的视频，查看详尽信息得到
    fps = 30
    #获取图片的分辨率信息
    width, height, x = imgs[0].shape
    size = (height, width)

    #创建一个视频写入对象
    videowriter = cv2.VideoWriter("result.avi", cv2.VideoWriter_fourcc("I", "4", "2", "0"), fps, size)
   
    #遍历切割出来的图像，先转换成字符画，再写入新的视频
    for img in imgs:
        videowriter.write(img2video(img))
    
    #释放空间
    videowriter.release()

    