# Multi-modal Image Fusion

This project is for personal study and under development, please click 'watch' or 'star' my repo and check back later if you are interested in it.

> **2023.2.26 Update:**
> This project was initially set up for polarization image fusion, and now it has been extended to infrared image fusion. Thus, it was renamed as multi-modal image fusion.

## 0 使用方法

- 配置：`pip install -r requirements.txt`

- 训练：`python train.py --data roadscene`

- 测试：`python test.py --data tno --ckpt 2023-02-26_23-15`

- 评估：`python eval.py --data tno --ckpt 2023-02-26_23-15`

## 1 任务简述

主要任务：实现多模态图像融合，包括偏振与强度图像融合，以及红外与可见光图像融合。

## 2 模型

本项目最初基于无监督的 PFNet 算法构建模型。

- 论文：https://doi.org/10.1364/ol.384189

- 代码：https://github.com/Junchao2018/Polarization-image-fusion

另外，还包括以下算法模型：

- 红外：DeepFuse, DenseFuse, VIFNet, DBNet (Dual-Branch), SEDRFuse, NestFuse, RFN-Nest, UNFusion, Res2Fusion, MAFusion

- 通用：IFCNN, DIFNet, PMGI

### 2.1 网络架构


### 2.2 损失函数

- 总损失

    ![](http://latex.codecogs.com/svg.latex?L_{total}(I_1,I_2,I_f)=L_{ssim}(I_1,I_2,I_f)+\alpha\cdot%20L_{pixel}(I_1,I_2,I_f)+\beta\cdot%20L_{grad}(I_1,I_2,I_f))

- 结构损失：SSIM loss

    ![](http://latex.codecogs.com/svg.latex?L_{SSIM}(I_1,I_2,I_f)=1-\frac{1}{N}\cdot\sum_{x,y}[\lambda\cdot%20SSIM(I_1,I_f)+(1-\lambda)\cdot%20SSIM(I_2,I_f)])

- 像素损失：Pixel loss

    ![](http://latex.codecogs.com/svg.latex?L_{pixel}(I_1,I_2,I_f)=\frac{1}{N}\cdot\sum_{x,y}\|\|I_f-max(I_1,I_2)\|\|_1)

- 梯度损失：Grad loss

    ![](http://latex.codecogs.com/svg.latex?L_{grad}(I_1,I_2,I_f)=\frac{1}{N}\cdot\sum_{x,y}\|\|\nabla%20I_f-max(\nabla%20I_1,\nabla%20I_2)\|\|_1)

## 3 数据集

本项目基于自建数据集训练偏振融合模型。

偏振数据集：

- 训练集图片数：200 对

- 测试集图片数：32 对

- 图片分辨率：1224x1024

- 图片宽高比：1.2:1

另外，使用 RoadScene 数据集训练红外融合模型。

红外数据集：

- 训练集图片数：200 对

- 测试集图片数：21 对

## 4 评价指标

本项目基于定性和定量评价算法性能。

### 4.1 主观评价


### 4.2 客观评价

- 统计量：标准差（SD）、平均梯度（AG）、空间频率（SF）、均方误差（MSE）、峰值信噪比（PSNR）、相关系数（CC）、差异相关性总和（SCD）

- 信息量：信息熵（EN）、交叉熵（CE）、互信息（MI）

- 视觉感知：融合性能（Qabf）、融合伪影（Nabf）、融合损失（Labf）、结构相似度（SSIM）、多尺度结构相似度（MS-SSIM）、融合视觉信息保真度（VIFF）

## 5 文件夹说明

```

.
|-- Multi-Modal-Image-Fusion
|   |-- README.md
|   |-- common.py
|   |-- core
|   |   |-- block.py
|   |   |-- fusion.py
|   |   |-- loss.py
|   |   |-- metric.py
|   |   `-- model.py
|   |-- data
|   |   |-- dataset.py
|   |   |-- patches.py
|   |   |-- samples
|   |   |   |-- infrared
|   |   |   |   `-- test
|   |   |   |       |-- ir
|   |   |   |       |   |-- 00537D.png
|   |   |   |       |   |-- 00556D.png
|   |   |   |       `-- vis
|   |   |   |           |-- 00537D.png
|   |   |   |           `-- 36.png
|   |   |   `-- polar
|   |   |       `-- test
|   |   |           |-- po
|   |   |           |   |-- 1.jpg
|   |   |           |   |-- 2.jpg
|   |   |           |   |-- 3.jpg
|   |   |           |   |-- 4.jpg
|   |   |           |   `-- 5.jpg
|   |   |           `-- vis
|   |   |               |-- 1.jpg
|   |   |               |-- 2.jpg
|   |   |               |-- 3.jpg
|   |   |               |-- 4.jpg
|   |   |               `-- 5.jpg
|   |   `-- transform.py
|   |-- eval.py
|   |-- requirements.txt
|   |-- test.py
|   `-- train.py
|-- checkpoints
|   |-- 2024-10-21_10-57
|   |   `-- train.log
|   |-- 2024-10-21_11-06
|   |   |-- events.out.tfevents.1729480004.autodl-container-bc584abc13-b43e5644.1544.0
|   |   |-- train
|   |   |-- train.log
|   |   `-- valid
|   `-- 2024-10-21_11-08
|       |-- events.out.tfevents.1729480091.autodl-container-bc584abc13-b43e5644.1571.0
|       |-- train
|       |-- train.log
|       `-- valid
`-- datasets
    `-- roadscene








```




