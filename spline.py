#!/usr/bin/env python3
"""
Greg Marcil
CS280 UC Berkeley
Practice implementation of Burt and Adelson's "A Multiresolution Spline With
Application to Image Mosaics
"""

import numpy as np
import cv2

apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.jpg")
