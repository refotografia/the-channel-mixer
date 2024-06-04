import numpy as np
from PIL import Image


def remix_image_channels(image, mode):
    """
    Remix image channels from RGB image into a new image.
    Modes: RBG, BRG, BGR, GRB, GBR, BW-R, BW-G, BW-B
    Returns: A NumPy array representing the new image with combined channels.
    """
    src = Image.open(image)
    image_src = np.asarray(src)

    if not image_src.shape[2] == 3:
        raise ValueError("Images must have 3 channels")

    if mode == "RBG":
        new_image = np.zeros_like(image_src)
        new_image[..., 0] = image_src[..., 0]
        new_image[..., 1] = image_src[..., 2]
        new_image[..., 2] = image_src[..., 1]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    if mode == "BRG":
        new_image = np.zeros_like(image_src)
        new_image[..., 0] = image_src[..., 2]
        new_image[..., 1] = image_src[..., 0]
        new_image[..., 2] = image_src[..., 1]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    if mode == "BGR":
        new_image = np.zeros_like(image_src)
        new_image[..., 0] = image_src[..., 2]
        new_image[..., 1] = image_src[..., 1]
        new_image[..., 2] = image_src[..., 0]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    if mode == "GRB":
        new_image = np.zeros_like(image_src)
        new_image[..., 0] = image_src[..., 1]
        new_image[..., 1] = image_src[..., 0]
        new_image[..., 2] = image_src[..., 2]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    if mode == "GBR":
        new_image = np.zeros_like(image_src)
        new_image[..., 0] = image_src[..., 1]
        new_image[..., 1] = image_src[..., 2]
        new_image[..., 2] = image_src[..., 0]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    if mode == "BW-R":
        height, width = image_src.shape[:2]
        new_image = np.zeros((height, width))
        new_image = image_src[..., 0]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    if mode == "BW-G":
        height, width = image_src.shape[:2]
        new_image = np.zeros((height, width))
        new_image = image_src[..., 1]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out
    if mode == "BW-R":
        height, width = image_src.shape[:2]
        new_image = np.zeros((height, width))
        new_image = image_src[..., 2]
        out = Image.fromarray(new_image)  # Convert NumPy array to PIL image
        return out

