import cv2
 
#print("Before URL")
cap = cv2.VideoCapture('rtsp://localhost:8888/cam1/mpeg4')
frame_index = 0
#cap = cv2.VideoCapture('rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa')
 
while True:
 
    #print('About to start the Read command')
    ret, frame = cap.read()
    print(frame.shape)
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    cv2.imwrite("/home/dell/Desktop/out_frame/frame_{}.jpg".format(frame_index), frame)
    frame_index += 1
    #print('Running..')
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()