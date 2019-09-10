"""
Created by: Rishikesh Vanarse

27/08/2019
"""

import numpy as np
import cv2

"""
To be imported in driver
"""

GAUSS_KERNEL_SIZE = 5

HARRIS_BLOCK_SIZE = 2
HARRIS_KSIZE = 5 #Aperture for sobel operator
HARRIS_K = 0.07
HARRIS_THRESHOLD = 0.01



class Image:

	"""
	Wrapper class for images in cv2 for required functions
	
	"""

	def __init__(self, np_matrix):
		self.img = np_matrix

	def display(self, name="Output", image = self.img):

		""" Display Image """
		
		cv2.imShow(name, image)

		#Temporary part - waitkey:
		if cv2.waitKey(0):
			cv2.destroyAllWindows()


	def replace(self, new_img):
		self.img = new_img

	
	def gaussian_blur(self, kernel_size=GAUSS_KERNEL_SIZE):
		ret_img = cv2.blur(self.img, (kernel_size, kernel_size))
		return ret_img

	
	def gaussian_diff(self, kernel_size=5):
		return self.img - self.gaussian_blur(kernel_size)

	
	def harris_corners(self):
		temp_img = np.float32(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY))
		ret_img = cv2.cornerHarris(temp_img, blockSize = HARRIS_BLOCK_SIZE, HARRIS_KSIZE, HARRIS_K)
		ret_img = cv2.dilate(ret_img, None)

		#Currently returning original image with highlighted corners
		#May need to be changed for returning only greyscale with threhold

		modified_img = self.img
		modified_img[ret_img > HARRIS_THRESHOLD*ret_img.max()] = [0,0,255]

		return modified_img

	"""
	SIFT
	"""
	def sift_direct(self):
		greyscale_img = cv2.cvtColor(self.img, COLOR_BGR2GRAY)

		sift = cv2.SIFT()
		keyPoints  = sift.detect(gray, None)

		sift_keypoints_img = cv2.drawKeypoints(gray, keyPoints)

		return sift_keypoints_img