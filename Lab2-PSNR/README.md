# CISC3021 Multimedia Forensics and Security - Lab2

We'll primarily use the `numpy` library for numerical operations, `matplotlib` for plotting, and `PIL` (Pillow) for image handling. Additionally, we'll use the `spicy` and `imageio` libraries for specific functionalities.

# Preparation
First, ensure you have the necessary packages installed:
```bash
pip install numpy matplotlib pillow scipy imageio
```

# See Channels
```python
# Load a true-color RGB image
image_path = 'path/to/your/image.jpg'  # Change this to the actual path
img = Image.open(image_path)

# Show the loaded image
plt.imshow(img)
plt.axis('off')
plt.show()

# Get the R, G, and B channels out of this image
r, g, b = img.split()

# Show the R, G, and B channels as grayscale images
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(np.array(r), cmap='gray')
axs[0].set_title('R Channel')
axs[0].axis('off')
axs[1].imshow(np.array(g), cmap='gray')
axs[1].set_title('G Channel')
axs[1].axis('off')
axs[2].imshow(np.array(b), cmap='gray')
axs[2].set_title('B Channel')
axs[2].axis('off')
plt.show()

# Show the R, G, and B channels as red, green, and blue images
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(np.array(r))
axs[0].set_title('Red Channel')
axs[0].axis('off')
axs[1].imshow(np.array(g))
axs[1].set_title('Green Channel')
axs[1].axis('off')
axs[2].imshow(np.array(b))
axs[2].set_title('Blue Channel')
axs[2].axis('off')
plt.show()

# Convert the RGB image into a grayscale image
img_gray = img.convert('L')

# Show the generated grayscale image
plt.imshow(np.array(img_gray), cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

# Image Manipulation
```python
# Reverse the colors of all pixel values inside the (both horizontally and vertically) 50% center part of the true-color image
width, height = img.size
center_width = int(width * 0.5)
center_height = int(height * 0.5)

# Crop the center part
img_center = img.crop(((width - center_width) // 2, (height - center_height) // 2,
                       (width + center_width) // 2, (height + center_height) // 2))

# Reverse the colors
r_center, g_center, b_center = img_center.split()
r_center = 255 - np.array(r_center)
g_center = 255 - np.array(g_center)
b_center = 255 - np.array(b_center)

# Merge the reversed colors back into the center part
img_center = Image.merge('RGB', (Image.fromarray(r_center), Image.fromarray(g_center), Image.fromarray(b_center)))

# Paste the modified center part back into the original image
img.paste(img_center, ((width - center_width) // 2, (height - center_height) // 2))

# Show the manipulated image
plt.imshow(img)
plt.title('Manipulated Image')
plt.axis('off')
plt.show()
```

# Image Analysis: Histograms
```python
# Calculate the histograms of the R, G, and B channels of both images
hist_r = np.histogram(np.array(r), bins=256, range=(0, 255))[0]
hist_g = np.histogram(np.array(g), bins=256, range=(0, 255))[0]
hist_b = np.histogram(np.array(b), bins=256, range=(0, 255))[0]

# Plot the histograms
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].plot(hist_r, color='red')
axs[0].set_title('Histogram of R Channel')
axs[1].plot(hist_g, color='green')
axs[1].set_title('Histogram of G Channel')
axs[2].plot(hist_b, color='blue')
axs[2].set_title('Histogram of B Channel')
plt.show()
```

# Image Analysis: Spatial Correlation
```python
# Draw a scatter diagram about pairs of neighboring pixel values (horizontal or vertical)
pixels = np.array(img)
scatter_horizontal = pixels[:, :-1].flatten(), pixels[:, 1:].flatten()
scatter_vertical = pixels[:-1, :].flatten(), pixels[1:, :].flatten()

# Plot the scatter diagrams
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].scatter(*scatter_horizontal, s=1, alpha=0.5)
axs[0].set_title('Horizontal Neighbors Scatter Diagram')
axs[1].scatter(*scatter_vertical, s=1, alpha=0.5)
axs[1].set_title('Vertical Neighbors Scatter Diagram')
plt.show()
```


## Image I/O and Image Compression
```python
# Save the manipulated image as a PNG file and a JPG file
iio.imwrite('manipulated_image.png', np.array(img))
iio.imwrite('manipulated_image.jpg', np.array(img))

# Compare the sizes of the PNG and JPG files with the original size of the image
original_size = os.path.getsize(image_path)
png_size = os.path.getsize('manipulated_image.png')
jpg_size = os.path.getsize('manipulated_image.jpg')

print(f"Original Image Size: {original_size} bytes")
print(f"PNG File Size: {png_size} bytes")
print(f"JPG File Size: {jpg_size} bytes")

# Load these two files and show them in the same figure as two sub-figures
img_png = Image.open('manipulated_image.png')
img_jpg = Image.open('manipulated_image.jpg')

# Show the images
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img_png)
axs[0].set_title('PNG Image')
axs[0].axis('off')
axs[1].imshow(img_jpg)
axs[1].set_title('JPG Image')
axs[1].axis('off')
plt.show()

# Show their difference as a single image
difference = np.array(img_png) - np.array(img_jpg)
plt.imshow(difference)
plt.title('Difference Image')
plt.axis('off')
plt.show()
```

# Color Space Conversion and Chroma Subsampling
```python
# Convert the original true-color image from RGB color space to YCbCr color space
# Note: PIL does not support YCbCr conversion directly, so we'll use OpenCV for this step.
import cv2

img_rgb = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2YCrCb)
y, cb, cr = cv2.split(img_rgb)

# Subsample the Cb and Cr channels (i.e., halve both horizontal and vertical resolutions)
cb_subsampled = zoom(cb, (0.5, 0.5))
cr_subsampled = zoom(cr, (0.5, 0.5))

# Upsample to get the original size back
cb_upsampled = zoom(cb_subsampled, (2, 2))
cr_upsampled = zoom(cr_subsampled, (2, 2))

# Merge the Y, Cb, and Cr channels back together
img_ycbcr = cv2.merge([y, cb_upsampled, cr_upsampled])

# Convert the image from YCbCr color space back to RGB space
img_recovered = cv2.cvtColor(img_ycbcr, cv2.COLOR_YCrCb2BGR)

# Show the original image and the recovered image and their difference
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(np.array(img))
axs[0].set_title('Original Image')
axs[0].axis('off')
axs[1].imshow(cv2.cvtColor(img_recovered, cv2.COLOR_BGR2RGB))
axs[1].set_title('Recovered Image')
axs[1].axis('off')
axs[2].imshow(np.array(img) - cv2.cvtColor(img_recovered, cv2.COLOR_BGR2RGB))
axs[2].set_title('Difference Image')
axs[2].axis('off')
plt.show()
```


# PSNR
```python
def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Load a losslessly compressed test image and save it as a PNG and a JPG file
test_img = Image.open('path/to/your/test/image.png')  # Change this to the actual path
test_img.save('test_image.png')
test_img.save('test_image.jpg')

# Calculate the PSNR values of the PNG and the JPG files compared with the original image
psnr_png = psnr(np.array(test_img), iio.imread('test_image.png'))
psnr_jpg = psnr(np.array(test_img), iio.imread('test_image.jpg'))

print(f"PSNR of PNG: {psnr_png}")
print(f"PSNR of JPG: {psnr_jpg}")

# For the original image, do the RGB to YCbCr color space conversion and calculate the visual quality of the image recovered
# We already did the conversion and recovery steps above.
psnr_recovered = psnr(np.array(img), cv2.cvtColor(img_recovered, cv2.COLOR_BGR2RGB))

print(f"PSNR of Recovered Image: {psnr_recovered}")
```
