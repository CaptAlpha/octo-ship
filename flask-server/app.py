from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import session as login_session

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #save the video
        video = request.files['video_file']
        #save the video to the static folder
        video.save('./static/' + video.filename)
        
        return redirect(url_for('index'))
    return render_template('index.html')


#main function
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run()