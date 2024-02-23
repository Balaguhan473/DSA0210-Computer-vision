import cv2
path =r"C:\Users\kbala\Pictures\WhatsApp Image 2023-12-17 at 15.54.51_a6768a73.jpg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
img = cv2.resize(image,(600,600))
cv2.imshow(window_name, img)
cv2.waitKey(0)
