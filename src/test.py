import cv2
import numpy as np

# Kmeans color segmentation
# def kmeans_color_quantization(image, clusters=8, rounds=1):
#     h, w = image.shape[:2]
#     samples = np.zeros([h*w,3], dtype=np.float32)
#     count = 0

#     for x in range(h):
#         for y in range(w):
#             samples[count] = image[x][y]
#             count += 1

#     compactness, labels, centers = cv2.kmeans(samples,
#             clusters, 
#             None,
#             (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
#             rounds, 
#             cv2.KMEANS_RANDOM_CENTERS)

#     centers = np.uint8(centers)
#     res = centers[labels.flatten()]
#     return res.reshape((image.shape))

# # Load image and perform kmeans
# image = cv2.imread('./teste1.png')
# kmeans = kmeans_color_quantization(image, clusters=3)
# result = kmeans.copy()

# # Floodfill
# seed_point = (150, 50)
# cv2.floodFill(result, None, seedPoint=seed_point, newVal=(36, 255, 12), loDiff=(0, 0, 0, 0), upDiff=(0, 0, 0, 0))

# cv2.imshow('image', image)
# cv2.imshow('kmeans', kmeans)
# cv2.imshow('result', result)
# cv2.waitKey()   


flood = cv2.imread("./teste1.png");

seed = (180, 80)

cv2.floodFill(flood, None, seedPoint=seed, newVal=(0, 0, 255), loDiff=(5, 5, 5, 5), upDiff=(5, 5, 5, 5))
cv2.circle(flood, seed, 2, (0, 255, 0), cv2.FILLED, cv2.LINE_AA);

cv2.imshow('flood', flood)
cv2.waitKey(0)
cv2.destroyAllWindows()