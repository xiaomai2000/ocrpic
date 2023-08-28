import os

import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
import easyocr





if __name__ == "__main__":
    print("starts")
    # Changing the image path
    IMAGE_PATH = r'C:\Users\x\Documents\th.test.02.png'
    reader = easyocr.Reader(['id','en'], gpu=False)  #ch_sim, ch_tra, en, th, ko,ja,id,ms  (['th','en']) ['ko','en']  ['ja','en'] ['id','en'] ['ms','en']
    result = reader.readtext(IMAGE_PATH, detail=0)
    print(result)




