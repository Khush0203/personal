import cv2
cam = cv2.VideoCapture(0)
cam.set(10,120)
while cam.isOpened():
    ret , frame = cam.read()
    # flipped = cv2.flip(frame,0)
    flip = cv2.flip(frame,1)

    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('CCTV',flip)


# # import cv2

# # file = cv2.VideoCapture(r"C:\Users\Suneetha\Desktop\pics res\New folder\WhatsApp Video 2021-07-31 at 5.45.34 PM.mp4")
# # #giving location of file 

# # while True:
# #     succeess, vid = file.read()
# # #read the file
# #     cv2.imshow("Khush",vid)
# # #show the file
# #     if cv2.waitKey(10) & 0xFF == ord("q"): 
# # #if q is entered on keyboard then break
# #         break
        
# # #it breaks if q is entered

# import cv2

# file = cv2.VideoCapture(0)
# #open camera
# file.set(3,480)
# #height
# file.set(4,480)
# #width
# file.set(10,100)
# #brightness

# while True:
#     succeess, vid = file.read()
# #read the cam
#     cv2.imshow("Khush",vid)
# #show the cam
#     if cv2.waitKey(10) & 0xFF == ord("q"): 
# #if q is entered on keyboard then break
#         break
        
# #it breaks if q is entered