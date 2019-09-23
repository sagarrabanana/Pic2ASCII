import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #convert the image to B&W
    (thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Black white image', blackAndWhiteImage)
    
    resized=cv2.resize(blackAndWhiteImage, (213,160), interpolation = cv2.INTER_AREA)
    print(resized.shape)
    cv2.imshow('mini', resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        f = open('ASCII_pic.txt','w')
        for x in range(160):
            f.write('\n')
            
            for y in range(213):
                t=(resized[x, y])
                if t==0:
                    f.write('X')
                   
                else:
                    f.write(' ')
                    
        #f.write(str(pixel))
        f.close()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
