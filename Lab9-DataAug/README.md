# Data Augmentation 

Our learned methods, such as watermarking and Steganography, also can be used in the data augmentation.

Today, we will examine several methods of data augmentation.
The essential point is that these methods do not alter the fundamental meaning of the image.
Specifically, people should still be able to recognize the objects within the image.

![](https://github.com/zhunzhong07/Random-Erasing/raw/master/all_examples-page-001.jpg)

Please check our baseline code at https://github.com/zhunzhong07/Random-Erasing.

## 1. Reproduce results

You can reproduce the results by `python cifar.py --dataset cifar10 --arch resnet --depth 20` for CIFAR10 with ResNet-20.

| |  CIFAR10 | CIFAR10| CIFAR100 | CIFAR100| Fashion-MNIST | Fashion-MNIST|
| -----   | -----  | ----  | -----  | ----  | -----  | ----  |
|Models |  Base. | +RE | Base. | +RE | Base. | +RE |
|ResNet-20 |  7.21 | 6.73 | 30.84 | 29.97 | 4.39 | 4.02 |
|ResNet-32 |  6.41 | 5.66 | 28.50 | 27.18 | 4.16 | 3.80 |
|ResNet-44 |  5.53 | 5.13 | 25.27 | 24.29 | 4.41 | 4.01 |
|ResNet-56 |  5.31 | 4.89| 24.82 | 23.69 | 4.39 | 4.13 |
|ResNet-110 |  5.10 | 4.61 | 23.73 | 22.10 | 4.40 | 4.01 |
|WRN-28-10 |  3.80 | 3.08 | 18.49 | 17.73 | 4.01 | 3.65 |


## 2. Try deeper and wider network.

`python cifar.py --dataset cifar10 --arch wrn --depth 28 --widen-factor 10`

## 3. Try data augmentation.
Please check random erasing by simply adding `--p 0.5`

The running command will be `python cifar.py --dataset cifar10 --arch resnet --depth 20 --p 0.5`


## 4. Challenge. Try to adding more data augmentation.

![](https://raw.githubusercontent.com/aleju/imgaug-doc/master/readme_images/examples_grid.jpg?raw=true)

https://github.com/aleju/imgaug

Add the data augmentation to the training part at this line https://github.com/zhunzhong07/Random-Erasing/blob/master/cifar.py#L107 . 

## 5. Thinking.
1. Why most data augmentation will compromise the performance?
2. Do you still remember the bar chart in steganalysis? Think about the data distribution after any data augmentation.
3. What is (0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010) in https://github.com/zhunzhong07/Random-Erasing/blob/master/cifar.py#L110? Try to search these numbers.

