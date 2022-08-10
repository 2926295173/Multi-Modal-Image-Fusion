# -*- coding: utf-8 -*-
"""
# @file name  : transform.py
# @author     : chenzhanpeng https://github.com/chenzpstar
# @date       : 2022-08-08
# @brief      : 图像变换
"""

import numpy as np


def norm(img, mode=None):
    if mode is None:
        return img

    elif mode == 'max-min':
        img_min = img.min()
        img_max = img.max()
        img = (img - img_min) / (img_max - img_min)

    elif mode == 'mean-std':
        img_mean = img.mean()
        img_std = img.std()
        img = (img - img_mean) / img_std.clip(1e-7)

    else:
        raise ValueError("only supported ['max-min', 'mean-var'] mode")

    return img


def denorm(img):
    img = img.detach().cpu().numpy()
    img = img.clip(0, 1) * 255.0
    img = img.transpose((1, 2, 0)).astype(np.uint8)

    return img


def transform(img, mode=0):
    if mode == 0:
        # original
        return img
    elif mode == 1:
        # rotate 180 degree
        img = np.rot90(img, k=2)
    elif mode == 2:
        # flip up and down
        img = np.flipud(img)
    elif mode == 3:
        # flip left and right
        img = np.fliplr(img)
    elif mode == 4:
        # rotate 90 degree
        img = np.rot90(img, k=1)
    elif mode == 5:
        # rotate 270 degree
        img = np.rot90(img, k=-1)
    elif mode == 6:
        # rotate 90 degree and flip up and down
        img = np.rot90(img, k=1)
        img = np.flipud(img)
    elif mode == 7:
        # rotate 270 degree and flip up and down
        img = np.rot90(img, k=-1)
        img = np.flipud(img)

    return img
