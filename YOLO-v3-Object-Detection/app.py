from flask import Flask,jsonify,request,render_template,redirect
import cv2
from yolo_detection_images import detectObjects
app = Flask(__name__)

@app.route('/',methods=["POST", "GET"])
def hello():
    if request.method=="POST":
        return redirect("/myapp/detectObjects")
    
    return render_template("index.html")

@app.route('/myapp/detectObjects', methods=["POST", "GET"])
def detect():
    img = request.args['image']
    img_path = 'static/'+img
    results = detectObjects(img_path)

    imag = cv2.imread(img_path)

    print(results)
    print(jsonify(results))
    # from results extract the X and Y coordinates of the bounding boxes
    # and their corresponding class namespace
    x = results['detections']['labels'][0]['X']
    y = results['detections']['labels'][0]['Y']
    w = results['detections']['labels'][0]['Width']
    h = results['detections']['labels'][0]['Height']


    label = results['detections']['labels'][0]['Label']
    confidence = results['detections']['labels'][0]['Confidence']
    # draw the bounding box of the detected person on the image
    cv2.rectangle(imag, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(imag, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(imag, str(confidence), (x, y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # encode the image as a jpeg
    ret, jpeg = cv2.imencode('.jpg', imag)
    #save the image to a file
    cv2.imwrite('assets\\'+img, imag)






    # # save img_path to assets/images/
    # cv2.imwrite('assets/'+img, img)



    return jsonify(results)
if __name__ == "__main__":
    app.run()
