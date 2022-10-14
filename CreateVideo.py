import os
import cv2

path = 'Images/'
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path_name = path + name + ext
        print(path_name)
        images.append(path_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])

height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('friends.mp4' ,0x7634706d, 30, size)

for i in range(count - 1, 0, -1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print('complete')
