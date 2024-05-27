# -*- coding: utf-8 -*-
"""
Created on Mon 27 May 2024

Author: YIJU WU (gn02129251)

File: gamma.py

Topic: A module developed for image gamma processing

"""
# -*- coding: utf-8 -*-
"""
Created on Sun 26 May 2024

Author: YIJU WU (gn02129251)

File: gamma.py

Topic:

"""
# Import required modules
import cv2
import numpy as np
from cv2.typing import MatLike


def gamma_correction(image: MatLike, gamma_value: float) -> MatLike:
    """
    Apply gamma correction to an image.

    Args:
        image (MatLike): The input image.
        gamma_value (float): The gamma value for correction.

    Returns:
        MatLike: The gamma-corrected image.
    """
    # Create a lookup table for gamma correction
    table = (np.arange(0, 256) / 255.0) ** gamma_value
    table = (table * 255).astype(np.uint8)

    # Apply gamma correction using the lookup table
    gamma_corrected_img = cv2.LUT(image, table)

    return gamma_corrected_img


def main(*args):
    return 0


if __name__ == "__main__":
    main()
