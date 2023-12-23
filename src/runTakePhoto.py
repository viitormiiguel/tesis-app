
import cv2
import os
from bson.objectid import ObjectId

def takePhoto():

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Take a Photo")

    img_counter = 0
    
    nome = str(ObjectId())
    
    ## Pasta no input
    if not os.path.exists('./input/' + nome + '_' + str(img_counter)):
        os.makedirs('./input/' + nome + '_' + str(img_counter))
        
    ## Pasta no output
    if not os.path.exists('./output/' + nome + '_' + str(img_counter)):
        os.makedirs('./output/' + nome + '_' + str(img_counter))

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Take a Photo", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            # print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = './input/' + nome + '_' + str(img_counter) + '/' + nome + "_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("Image " + "{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    
    return nome