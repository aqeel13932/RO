#https://github.com/log0/video_streaming_with_flask_example
from flask import *
from camera import VideoCamera
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('video.html')


def gen(camera):
    while True:
        time.sleep(0.05)
        frame = camera.get_frame()
        if frame is None:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(host='0.0.0.0')
