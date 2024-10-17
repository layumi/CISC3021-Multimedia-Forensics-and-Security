# AI Security - FaceSwap

Please try https://github.com/neuralchen/SimSwap 
Follow the setting in Colab. 

I suggest to run on our own 3090 machines. 
```bash
conda create -n simswap python=3.6
conda activate simswap
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=10.2 -c pytorch
pip install --ignore-installed imageio
pip install insightface==0.2.1 onnxruntime moviepy
pip install onnxruntime-gpu  (If you want to reduce the inference time)(It will be diffcult to install onnxruntime-gpu , the specify version of onnxruntime-gpu may depends on your machine and cuda version.)
```


# See their paper. 
https://dl.acm.org/doi/10.1145/3394171.3413630 

# Understand the code.
1. Try the pretrained model.
2. Try using your own selfie or other celebrity selfie to swap the face.
3. Check about the outliers, such as strong illumination, occluded, or side face.

# Think more.
4. Design and implement a simple detection system that can identify whether an image has been manipulated using SimSwap. 
5. Discuss the ethical and legal implications of using face swapping technology. How can we ensure responsible use and prevent misuse?
