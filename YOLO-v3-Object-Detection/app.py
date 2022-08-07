from flask import Flask,jsonify,request,render_template,redirect
import cv2
from framesplit import FrameCapture
from yolo_detection_video import detectObj
from yolo_detection_images import detectObjects
app = Flask(__name__)

@app.route('/',methods=["POST", "GET"])
def index():
    if request.method=="POST":
        return redirect("upload")
    
    return render_template("index.html")

@app.route('/upload',methods=["POST", "GET"])
def upload():
    if request.method=="POST":
        f = request.files['file']
        f.save("video/vid.mp4")

        detectObj("video/vid.mp4")
        import moviepy.editor as moviepy
        clip = moviepy.VideoFileClip("static/chase_output.avi")
        clip.write_videofile("static/chase_output.mp4")
        return redirect("/myapp/detectObjects")
    return render_template("upload.html")

@app.route('/myapp/detectObjects', methods=["POST", "GET"])
def detect():
    return render_template("render.html")
if __name__ == "__main__":
    app.run()
