# AI Security - FaceSwap

Please try https://github.com/neuralchen/SimSwap 

I suggest to run on our own 3090 machines. Before you test the model, please ensure the environment. 

```bash
conda create -n simswap python=3.12
conda activate simswap
conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 cudatoolkit=12.2 -c pytorch
pip install --ignore-installed imageio
pip install --prefer-binary insightface onnx==1.17.0 onnxruntime==1.19.2 moviepy==1.0.3 
```

# Download Trained Model. 
We could skip the training data. I think their googledrive link is blocked due to too much downloads.
```bash
wget -P ./arcface_model https://github.com/neuralchen/SimSwap/releases/download/1.0/arcface_checkpoint.tar
wget https://github.com/neuralchen/SimSwap/releases/download/1.0/checkpoints.zip
unzip ./checkpoints.zip  -d ./checkpoints
wget -P ./parsing_model/checkpoint https://github.com/neuralchen/SimSwap/releases/download/1.0/79999_iter.pth
wget https://github.com/neuralchen/SimSwap/releases/download/512_beta/512.zip
unzip ./512.zip -d ./checkpoints
```

![](https://github.com/neuralchen/SimSwap/raw/main/docs/img/multi_face_comparison.png)

# Test one image 
```bash
python test_wholeimage_swap_multispecific.py --crop_size 512 --use_mask  --name people --Arc_path arcface_model/arcface_checkpoint.tar --pic_b_path ./demo_file/multi_people.jpg --output_path ./output/ --multisepcific_dir ./demo_file/multispecific
```
Check more on https://github.com/neuralchen/SimSwap/blob/main/docs/guidance/usage.md 


# Test video
```bash
python test_video_swap_multispecific.py --crop_size 224 --use_mask  --name people --Arc_path arcface_model/arcface_checkpoint.tar --video_path ./demo_file/multi_people_1080p.mp4 --output_path ./output/multi_test_multispecific.mp4 --temp_path ./temp_results --multisepcific_dir ./demo_file/multispecific 
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
