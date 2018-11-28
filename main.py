import picamera
import sys
print(sys.version)

from bottle import route, run, response
from camera import HTTPMJPEGStream


@route('/')
def index():
    return '''
        <html>
            <head></head>
            <body>
                <img src="/cam.mjpeg"/>
            </body>
        </html>
    '''


@route('/cam.mjpeg')
def mjpeg():
    try:
        boundary = '--jpgboundary'
        response.set_header('Content-type', 'multipart/x-mixed-replace; boundary=' + boundary)

        camera = picamera.PiCamera(resolution=(320, 240), framerate=20)
        return HTTPMJPEGStream(camera, content_type_header=False, boundary=boundary)

    except Exception as e:
        print(e)


run(host='alphabot.local', port=8080)