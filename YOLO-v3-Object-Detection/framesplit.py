from yolo_detection_images import detectObjects
import cv2
def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    success = 1
    num_frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = vidObj.get(cv2.CAP_PROP_FPS)

    for i in range(num_frames):
        success, image = vidObj.read()

        #detect objects in image

    
        try:
            cv2.imwrite("frames/frame"+str(i+1)+".png", image)
            results = detectObjects("frames/frame"+str(i+1)+".png")
            print(results)
            x = results['detections']['labels'][0]['X']
            y = results['detections']['labels'][0]['Y']
            w = results['detections']['labels'][0]['Width']
            h = results['detections']['labels'][0]['Height']


            label = results['detections']['labels'][0]['Label']
            confidence = results['detections']['labels'][0]['Confidence']
            # draw the bounding box of the detected person on the image
            cv2.rectangle(imag, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # encode the image as a jpeg
            ret, jpeg = cv2.imencode('.jpg', imag)
            #save the image to a file
            cv2.imwrite('assets\\image'+str(i+1), imag)

        except:
            #print("error")
            print("No object detected")



    
        
  