# 3D Generation (about 10~30-minute training on Nvidia 3090)

Code: https://github.com/Texaser/MTN

Video: https://www.youtube.com/watch?v=LH6-wKg30FQ

### Note

If the memory is not enough, you could resize 64 to 48.
Or try different stable diffusion version. 


### Task 1

Generate a 3D video by using your command like `a tiger dressed as a doctor`.

### Task 2

Check the memory usage by 
```bash
pip install gpustat
gpustat
```

### Task3 

Try to find some common failure. 

### Task 4

Try to understand every hyper-parameters. 
https://github.com/Texaser/MTN/blob/main/main.py#L22-L173 

Change one hyper-parameter to see the effect.
