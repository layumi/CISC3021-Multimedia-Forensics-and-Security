# LSB-stego

Check the steps on Slide 34 of Lecture 2, and implement the LSB substitution based steganography (both sequential path and random path). You can choose any cover image and the information you would like to embed.  

```bash
pip install numpy pillow
```

```python
import numpy as np
from PIL import Image

def LSB_stego_sequential(cov, plaintext):
    h, w = cov.shape
    stg_img = cov.copy()
    
    len = plaintext.size
    for i in range(len):
        lsb = cov[i] % 2
        if plaintext[i] == lsb:
            stg_img[i] = stg_img[i]
        elif lsb == 0:
            stg_img[i] = stg_img[i] + 1
        else:
            stg_img[i] = stg_img[i] - 1
    return stg_img

def LSB_extract_sequential(stg_img, h_p, w_p):
    # Ensure stg_img is a numpy array
    stg_img = np.array(stg_img)
    
    # Flatten the image to work with it sequentially
    flat_stg_img = stg_img.flatten()
    
    # Calculate the length based on the dimensions provided
    len = h_p * w_p
    plaintext = np.zeros(len, dtype=np.uint8)
    
    # Extract the least significant bit (LSB) for each pixel
    for i in range(len):
        plaintext[i] = flat_stg_img[i] % 2
    
    # Reshape the extracted data back into the original dimensions
    plaintext = plaintext.reshape(h_p, w_p)
    return plaintext

def LSB_extract_random(stg_img, stego_key, h_p, w_p):
    h, w = stg_img.shape
    
    len = stego_key.shape[0]
    plaintext = np.zeros((h_p, w_p))
    for i in range(len):
        v = int(round(stego_key[i][0] * h))
        v = max(1, min(v, h))  # Ensure v is within bounds
        u = int(round(stego_key[i][1] * w))
        u = max(1, min(u, w))  # Ensure u is within bounds
        plaintext[i] = stg_img[v-1, u-1] % 2  # Adjust index for Python 0-based indexing
    return plaintext

def LSB_stego_random(cov, plaintext):
    h, w = cov.shape
    stg_img = cov.copy()
    
    len = plaintext.size
    stego_key = np.random.rand(len, 2)
    for i in range(len):
        v = int(round(stego_key[i][0] * h))
        v = max(1, min(v, h))  # Ensure v is within bounds
        u = int(round(stego_key[i][1] * w))
        u = max(1, min(u, w))  # Ensure u is within bounds
        
        lsb = cov[v-1, u-1] % 2  # Adjust index for Python 0-based indexing
        if plaintext[i] == lsb:
            stg_img[v-1, u-1] = stg_img[v-1, u-1]
        elif lsb == 0:
            stg_img[v-1, u-1] = stg_img[v-1, u-1] + 1
        else:
            stg_img[v-1, u-1] = stg_img[v-1, u-1] - 1
    return stg_img, stego_key

# Example usage:
# Load images
cov = Image.open('parrots.jpg').convert('L')  # Convert to grayscale
cov_array = np.array(cov)

plaintext = Image.open('plaintext.png').convert('L')
plaintext_array = np.array(plaintext).flatten()

# Sequential LSB Steganography
stg_img_seq = LSB_stego_sequential(cov_array, plaintext_array)
stg_img_seq = Image.fromarray(stg_img_seq)
stg_img_seq.save('stego_sequential.png')

# Extract the embedded bits
hp, wp = plaintext.shape
res_plaintext_seq = LSB_extract_sequential(stg_img_seq, hp, wp)
res_plaintext_seq = Image.fromarray(res_plaintext_seq.reshape(hp, wp)).convert('L')
res_plaintext_seq.save('extracted_sequential.png')

# Random LSB Steganography
stg_img_rand, stego_key = LSB_stego_random(cov_array, plaintext_array)
stg_img_rand = Image.fromarray(stg_img_rand)
stg_img_rand.save('stego_random.png')

# Extract the embedded bits
res_plaintext_rand = LSB_extract_random(stg_img_rand, stego_key, hp, wp)
res_plaintext_rand = Image.fromarray(res_plaintext_rand.reshape(hp, wp)).convert('L')
res_plaintext_rand.save('extracted_random.png')
```

