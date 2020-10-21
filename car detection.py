import cv2

cap = cv2.VideoCapture('video.avi')

car_cascade = cv2.CascadeClassifier('cars.xml')


#width  = cap.get(3) # float width
#height = cap.get(4) # float height    
# Make a video writer to see if video being taken as input inflict any changes you make
#fourcc = cv2.VideoWriter_fourcc(*"MJPG")
#out_video = cv2.VideoWriter('result/output.avi', fourcc, 20.0, (int(width), int(height)), True)
# Then try this
while(cap.isOpened()):
        # Read each frame where ret is a return boollean value(True or False)
        ret, frame = cap.read()
        # if return is true continue because if it isn't then frame is of NoneType in that case you cant work on that frame
        if ret:
            # Any preprocessing you want to make on the frame goes here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # See if preprocessing is working on the frame it should

            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)


            cv2.imshow('frame', frame)
            # finally write your preprocessed frame into your output video
            #out_video.write(gray) # write the modifies frame into output video 
            # to forcefully stop the running loop and break out, if it doesnt work use ctlr+c
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
       # break out if frame has return NoneType this means that once script encounters such frame it breaks out 
       # You will get the error otherwise 
        else:
            break

#while True:
#    ret, frame = cap.read()

#    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    
#    for (x, y, w, h) in cars:
#        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

#cv.imshow('video2', frame)

#if cv.waitKey(33) == 27:
#    pass

cv2.destroyAllWindows()