import cv2

# Load images
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")
image3 = cv2.imread("image3.jpg")

# Convert images to grayscale (optional, for feature detection)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

# Extract locations of matched keypoints
src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Compute homography matrix
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Warp image2 to align with image1
height, width, channels = image1.shape
warped_image2 = cv2.warpPerspective(image2, H, (width * 2, height))

# Place image1 on the canvas
panorama = np.zeros_like(warped_image2)
panorama[0:height, 0:width] = image1

# Combine images
panorama = cv2.addWeighted(panorama, 1, warped_image2, 1, 0)
cv2.imshow("Panorama", panorama)
cv2.waitKey(0)
cv2.destroyAllWindows()

def stitch_images(images):
    stitched = images[0]
    for i in range(1, len(images)):
        # Detect and match features
        gray_stitched = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
        gray_next = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
        
        keypoints1, descriptors1 = sift.detectAndCompute(gray_stitched, None)
        keypoints2, descriptors2 = sift.detectAndCompute(gray_next, None)
        
        matches = bf.match(descriptors1, descriptors2)
        matches = sorted(matches, key=lambda x: x.distance)
        
        src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        
        H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        
        height, width, channels = stitched.shape
        warped_image = cv2.warpPerspective(images[i], H, (width * 2, height))
        
        panorama = np.zeros_like(warped_image)
        panorama[0:height, 0:width] = stitched
        stitched = cv2.addWeighted(panorama, 1, warped_image, 1, 0)
    return stitched

images = [cv2.imread("image1.jpg"), cv2.imread("image2.jpg"), cv2.imread("image3.jpg")]
panorama = stitch_images(images)
cv2.imwrite("panorama.jpg", panorama)
cv2.imshow("Final Panorama", panorama)
cv2.waitKey(0)
cv2.destroyAllWindows()
