import numpy as np


def combine_image_channels(image1, image2, image3):
  """
  Combine image channels from three images into a new image.

  Args:
      image1: A NumPy array representing the first image.
      image2: A NumPy array representing the second image.
      image3: A NumPy array representing the third image.

  Returns:
      A NumPy array representing the new image with combined channels.
  """

  if not (image1.shape == image2.shape == image3.shape):
    raise ValueError("Images must have the same shape")

  # Assuming images have RGB channels
  if image1.ndim == 3 and image1.shape[2] == 3:
    new_image = np.zeros_like(image1)
    new_image[..., 0] = image1[..., 0]  # Red channel from image 1
    new_image[..., 1] = image2[..., 1]  # Green channel from image 2
    new_image[..., 2] = image3[..., 2]  # Blue channel from image 3
    return new_image
  else:
    raise ValueError("Images must have 3 channels (RGB)")


