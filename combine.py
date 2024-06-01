import numpy as np
from PIL import Image


def combine_image_channels(red, green, blue):
    """
    Combine image channels from three images into a new image.
    Returns: A NumPy array representing the new image with combined channels.
    """
    image1 = Image.open(red)
    image2 = Image.open(green)
    image3 = Image.open(blue)

    image1 = np.asarray(image1)
    image2 = np.asarray(image2)
    image3 = np.asarray(image3)

    if not (image1.shape == image2.shape == image3.shape):
        raise ValueError("Images must have the same shape")

    if image1.ndim == 3 and image1.shape[2] == 3:
        new_image = np.zeros_like(image1)
        new_image[..., 0] = image1[..., 0]  # Red channel from image 1
        new_image[..., 1] = image2[..., 1]  # Green channel from image 2
        new_image[..., 2] = image3[..., 2]  # Blue channel from image 3
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    else:
        height, width = image1.shape[:2]
        new_image = np.zeros((height, width, 3))
        new_image[..., 0] = image1  # Red channel from image 1
        new_image[..., 1] = image2  # Green channel from image 2
        new_image[..., 2] = image3  # Blue channel from image 3
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
