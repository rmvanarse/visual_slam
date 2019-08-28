import numpy as np
import cv2

class Image:
	def __init__(self, np_matrix):
		self.img = np_matrix

	def replace(self, new_img):
		self.img = new_img

	def gaussian_blur(self):
		pass