import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Load the PNG image
img_path = r'C:\\temp\\HK.XG.03.png'
img = cv2.imread(img_path)

if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

texts=[]
texts.append( ((90,518,230,552), r'描述'))
texts.append( ((440,522,526,548), r'金额'))
texts.append( ((98,610,335,638), r'黑色巧克力'))
texts.append( ((96,822,170,846), r'总数'))
texts.append( ((94,852,180,878), r'支付宝'))

# 创建一个可以在给定图像上绘图的对象
draw = ImageDraw.Draw(img)

# 字体的格式
textSize=25
textColor=(0, 0,255)
fontStyle = ImageFont.truetype("simsun.ttc", textSize, encoding="utf-8")            



# 绘制文本
for text in texts:
    loc, textcontent = text
    x, y, x2, y2 = loc
    draw.rectangle([(x, y), (x2, y2)], fill ="#D3D3D3", outline ="pink") 
    draw.text((x, y), textcontent, textColor, font=fontStyle) 


# 转换回OpenCV格式
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


# Display the output
cv2.imshow('Image with rectangles and small text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

