# import os
# import cv2
# import time
# import uuid

# IMAGE_PATH = "CollectedImages"

# labels = ["Hello",  "Yes", "No", "Thanks", "ILoveYou", "Please"]


# number_of_images = 5

# for label in labels:
#     img_path = os.path.join(IMAGE_PATH, label)
#     os.makedirs(img_path)
    
#     #open camera
#     cap = cv2.VideoCapture(0)
#     print(f"Collecting Images for {label}")
#     time.sleep(3)
    
#     for imgnum in range(number_of_images):
#         ret, frame = cap.read()
#         imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
#         cv2.imwrite(imagename, frame)
#         cv2.imshow("frame", frame)
#         time.sleep(5)
        
#         if cv2.waitKey(1) & 0xFF==ord("q"):
#             break
    
#     cap.release()
    
import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ["Hello",  "Yes", "No", "Thanks", "ILoveYou", "Please"]

number_of_images = 5

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)  # create folder if not exists
    
    # Open camera
    cap = cv2.VideoCapture(0)
    print(f"Collecting Images for {label}")
    time.sleep(3)
    
    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        imagename = os.path.join(img_path, f"{label}_{imgnum+1}.jpg")
        
        print(f"Capturing image {imgnum+1} for {label}")
        cv2.imwrite(imagename, frame)
        
        # Display captured image
        cv2.imshow("Captured Image", frame)
        cv2.waitKey(10000)  # Show captured image for 2 seconds
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    cap.release()
    cv2.destroyAllWindows()

