"""
Created by: Rishikesh Vanarse

27/08/2019
"""

import numpy as np
import cv2

"""
To be imported in driver
"""

class Image:

	"""
	Wrapper class for images in cv2 for required functions
	
	"""

	def __init__(self, np_matrix):
		self.img = np_matrix

	def replace(self, new_img):
		self.img = new_img

	def gaussian_blur(self, kernel_size=5):
		ret_img = cv2.blur(self.img, (kernel_size, kernel_size))
		return ret_img

	def gaussian_diff(self, kernel_size=5):
		return img - self.gaussian_blur(kernel_size)

	def harrison_corners(self):
		pass