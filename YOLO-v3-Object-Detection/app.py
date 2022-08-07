from flask import Flask,jsonify,request,render_template,redirect
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
    img_path = 'images/'+img
    results = detectObjects(img_path)

    print(results)

    return jsonify(results)
if __name__ == "__main__":
    app.run()
