from flask import Flask,jsonify,request,render_template,redirect
import cv2
from yolo_detection_video import detectObj
from yolo_detection_images import detectObjects
app = Flask(__name__)
key = ""
@app.route('/',methods=["POST", "GET"])
def index():
    if request.method=="POST":
        return redirect("upload")
    
    return render_template("index.html")

@app.route('/upload',methods=["POST", "GET"])
def upload():
    if request.method=="POST":
        key =""
        if request.files['image']:
            print("tt")
            f = request.files['image']
            f.save("frames/frame.jpg")
            detectObjects("frames/frame.jpg")
            key="image"
            return redirect("/myapp/detectObjectsimg")
        if request.files['file']:
            f = request.files['file']
            f.save("video/vid.mp4")

            detectObj("video/vid.mp4")
            import moviepy.editor as moviepy
            clip = moviepy.VideoFileClip("static/chase_output.avi")
            clip.write_videofile("static/chase_output.mp4")
            key="video"
            return redirect("/myapp/detectObjectsvid")
        
        




    return render_template("upload_new.html")

@app.route('/myapp/detectObjectsvid', methods=["POST", "GET"])
def detect():
    return render_template("render_video.html")
@app.route('/myapp/detectObjectsimg', methods=["POST", "GET"])
def detect_img():
    return render_template("render_image.html")
if __name__ == "__main__":
    app.run()
