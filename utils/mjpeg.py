import io
import picamera


class MJPEGStream(object):
    def __init__(self):
        self._last_frame = None
        self._current_frame = None

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self._last_frame = self._current_frame
            self._current_frame = io.BytesIO()
        self._current_frame.write(buf)

    def __iter__(self):
        while True:
            if self._last_frame:
                yield self._last_frame.getvalue()


class HTTPMJPEGStream(object):

    def __init__(self, camera=None, stream=None, content_type_header=True, boundary='--jpgboundary', close_camera_on_exit=True):
        self._camera = camera if camera else picamera.PiCamera()
        self._stream = stream if stream else MJPEGStream()
        self._content_type_header = content_type_header
        self._boundary = boundary
        self._close_camera_on_exit = close_camera_on_exit

    def __iter__(self):
        crlf = '\r\n'

        if not self._camera.recording:
            self._camera.start_recording(self._stream, format='mjpeg', quality=23)

        if self._content_type_header:
            yield 'Content-type: multipart/x-mixed-replace; boundary=' + self._boundary + crlf
            yield crlf

        for b in self._stream:
            yield self._boundary + crlf
            yield 'Content-type: image/jpeg' + crlf
            yield 'Content-length: ' + str(len(b)) + crlf
            yield crlf
            yield b
            yield crlf
            yield crlf

    def __del__(self):
        if self._close_camera_on_exit:
            self._camera.stop_recording()
            self._camera.close()
