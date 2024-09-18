import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def LSB_stego_sequential(cov, plaintext):
    h, w = cov.shape
    stg_img = cov.copy().flatten()
    cov = cov.flatten()
    
    lenx = plaintext.size
    for i in range(lenx):
        lsb = cov[i] % 2
        if plaintext[i]%2 == lsb:
            stg_img[i] = stg_img[i]
        elif lsb == 0:
            stg_img[i] = stg_img[i] + 1
        else:
            stg_img[i] = stg_img[i] - 1
    stg_img = stg_img.reshape(h,w)
    return stg_img

def LSB_extract_sequential(stg_img, h_p, w_p):
    # Ensure stg_img is a numpy array
    stg_img = np.array(stg_img)
    
    # Flatten the image to work with it sequentially
    flat_stg_img = stg_img.flatten()
    
    # Calculate the length based on the dimensions provided
    lenx = h_p * w_p
    plaintext = np.zeros(lenx, dtype=np.uint8)
    print(lenx)
    
    # Extract the least significant bit (LSB) for each pixel
    for i in range(lenx):
        plaintext[i] = flat_stg_img[i] % 2
    
    # Reshape the extracted data back into the original dimensions
    plaintext = plaintext.reshape(h_p, w_p)
    return plaintext





def LSB_extract_random(stg_img, stego_key, h_p, w_p):
    w,h = stg_img.size
    stg_img = np.array(stg_img)
    lenx = stego_key.shape[0]
    plaintext = np.zeros((h_p, w_p), dtype=np.uint8).flatten()
    for i in range(lenx):
        v = int(round(stego_key[i][0] * h))
        v = max(1, min(v, h))  # Ensure v is within bounds
        u = int(round(stego_key[i][1] * w))
        u = max(1, min(u, w))  # Ensure u is within bounds
        plaintext[i] = stg_img[v-1, u-1] % 2  # Adjust index for Python 0-based indexing
    return plaintext



def LSB_stego_random(cov, plaintext):
    h, w = cov.shape
    stg_img = cov.copy()
    
    lenx = plaintext.size
    # Old
    stego_key = np.random.rand(lenx, 2)
    # New random path without repeat. 
    norepeat_key = np.random.permutation(h*w)
    print(norepeat_key)
    norepeat_key = norepeat_key[0:lenx]
    for i in range(lenx):
        stego_key[i][0] = norepeat_key[i]//h/h
        stego_key[i][1] = norepeat_key[i]%h/w
    for i in range(lenx):
        v = int(round(stego_key[i][0] * h))
        v = max(1, min(v, h))  # Ensure v is within bounds
        u = int(round(stego_key[i][1] * w))
        u = max(1, min(u, w))  # Ensure u is within bounds
        lsb = cov[v-1, u-1] % 2  # Adjust index for Python 0-based indexing
        if plaintext[i]%2 == lsb:
            stg_img[v-1, u-1] = stg_img[v-1, u-1]
        elif lsb == 0 and stg_img[v-1, u-1]<255:
            stg_img[v-1, u-1] = stg_img[v-1, u-1] + 1
        else:
            stg_img[v-1, u-1] = stg_img[v-1, u-1] - 1
    return stg_img, stego_key




# 1. Basic Steganalysis
# Load images
cov = Image.open('Lena.bmp').convert('L')  # Convert to grayscale
#cov = Image.open('exposure.png').convert('L')  # Convert to grayscale
cov_array = np.array(cov)

plaintext = Image.open('plaintext.png').convert('L')
plaintext_array = np.array(plaintext).flatten()

# Sequential LSB Steganography
stg_img_seq = LSB_stego_sequential(cov_array, plaintext_array)
stg_img = Image.fromarray(stg_img_seq)
stg_img.save('stego_sequential.png')


fig, axs = plt.subplots(1, 4, figsize=(15, 5))
axs[0].imshow(cov_array, cmap='gray')
axs[0].set_title('Original')
axs[0].axis('off')
axs[1].imshow(cov_array%2, cmap='gray')
axs[1].set_title('Original LSB')
axs[1].axis('off')
axs[2].imshow(stg_img_seq, cmap='gray')
axs[2].set_title('Stego-Sequential')
axs[2].axis('off')
axs[3].imshow(stg_img_seq%2, cmap='gray')
axs[3].set_title('Stego-Sequential LSB')
axs[3].axis('off')

plt.show()

# 2. Basic Steganalysis not work for random path
# Extract the embedded bits
hp, wp = plaintext.size
res_plaintext_seq = LSB_extract_sequential(stg_img_seq, hp, wp)*255
res_plaintext_seq = Image.fromarray(res_plaintext_seq.reshape(hp, wp))
res_plaintext_seq.save('extracted_sequential.png')

# Random LSB Steganography
stg_array_rand, stego_key = LSB_stego_random(cov_array, plaintext_array)
stg_img_rand = Image.fromarray(stg_array_rand)
stg_img_rand.save('stego_random.png')

fig, axs = plt.subplots(1, 4, figsize=(15, 5))
axs[0].imshow(cov_array, cmap='gray')
axs[0].set_title('Original')
axs[0].axis('off')
axs[1].imshow(cov_array%2, cmap='gray')
axs[1].set_title('Original LSB')
axs[1].axis('off')
axs[2].imshow(stg_array_rand, cmap='gray')
axs[2].set_title('Stego-Sequential')
axs[2].axis('off')
axs[3].imshow(stg_array_rand%2, cmap='gray')
axs[3].set_title('Stego-Sequential Random Path')
axs[3].axis('off')

plt.show()
# Extract the embedded bits
res_plaintext_rand = LSB_extract_random(stg_img_rand, stego_key, hp, wp)*255
res_plaintext_rand = Image.fromarray(res_plaintext_rand.reshape(hp, wp))
res_plaintext_rand.save('extracted_random.png')


# 3. Histogram
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].hist(cov_array.ravel(), bins=256, range=(0,256), color='blue', alpha=0.5)
axs[0].set_title('Histogram of Cover Image')
axs[0].set_xlabel('Pixel Value')
axs[0].set_ylabel('Frequency')
axs[0].set_xlim([0, 256])

axs[1].hist(stg_array_rand.ravel(), bins=256, range=(0,256), color='red', alpha=0.5)
axs[1].set_title('Histogram of Stego Image')
axs[1].set_xlabel('Pixel Value')
axs[1].set_ylabel('Frequency')
axs[1].set_xlim([0, 256])

plt.tight_layout() 
plt.show()


# 4. Encrytion to cheat histogram
encry = np.random.choice(2, size=hp*wp)
encrytext_array = plaintext_array^encry
encry_stg_array_rand, encry_stego_key = LSB_stego_random(cov_array, encrytext_array)
encry_stg_img_rand = Image.fromarray(encry_stg_array_rand)
encry_stg_img_rand.save('encry_stego_random.png')

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].hist(cov_array.ravel(), bins=256, range=(0,256), color='blue', alpha=0.5)
axs[0].set_title('Histogram of Cover Image')
axs[0].set_xlabel('Pixel Value')
axs[0].set_ylabel('Frequency')
axs[0].set_xlim([0, 256])

axs[1].hist(encry_stg_array_rand.ravel(), bins=256, range=(0,256), color='red', alpha=0.5)
axs[1].set_title('Histogram of Encry Stego Image')
axs[1].set_xlabel('Pixel Value')
axs[1].set_ylabel('Frequency')
axs[1].set_xlim([0, 256])

plt.tight_layout()
plt.show()


# 5. Recover Encrytion




