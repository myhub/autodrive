import numpy as np
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

imgs = np.load("dataset/000000000_imgs.npy")
ain = np.load("dataset/000000000_ain.npy")
aout = np.load("dataset/000000000_aout.npy")

print("imgs", imgs.shape, imgs.dtype)
print("ain", ain.shape, ain.dtype)
print("aout", aout.shape, aout.dtype)

idx = 0

itos = ["S0", "S+", "S-", "L+", "L-", "R+", "R-"]

print("上一次执行的动作", itos[ain[idx][0]])
print("当前状态下该执行的动作", itos[aout[idx][0]])

img = np.transpose(imgs[idx], [1,2,0])

import PIL.Image
PIL.Image.fromarray(img*255).show()
