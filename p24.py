import cv2
import numpy as np
resized_img=cv2.imread("E:\pictures\p7.jpeg")
h_img, w_img, _ = resized_img.shape
center_y = int(h_img / 2)
center_x = int(w_img / 2)
resized_wm=cv2.imread("E:\pictures\p7.jpeg")
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
roi = resized_img[top_y:bottom_y, left_x:right_x]
sharpening_kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
sharpened_roi = cv2.filter2D(roi, -1, sharpening_kernel)
resized_img[top_y:bottom_y, left_x:right_x] = sharpened_roi
filename ="E:\pictures\p7.jpeg"
cv2.imwrite(filename, resized_img)
cv2.imshow("Resized Input Image with Sharpened ROI",sharpened_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
