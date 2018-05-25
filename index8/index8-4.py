# coding:utf8
import os, cv2, time, struct, threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import TCPServer, ThreadingTCPServer
from threading import Thread, RLock
from select import select

# 如何使用线程本地数据
''''''

'''
实际案例:
我们实现了一个web视频监控服务器,服务器采集摄像头数据,客户端使用
浏览器通过http请求接收数据,服务器使用推送的方式(multipart/x-
mixed-replace)一直使用一个tcp连接向客户端传递数据,这种方式
将持续占用一个线程,导致单线程服务器无法处理多客户端请求

改写程序,在每个线程中处理一个客户端请求,支持多客户端访问
'''


class JpegStreamer(Thread):
    def __init__(self, camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self):
        self.lock.acquire()
        self.pipes.pop(pr)
        self.lock.release()
        pr.close()
        pw.close()

    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ret, data = cv2.imencode('.jpg',frame,(cv2.IMWRITE_JPEG_QUALITY,40))
                yield data.tostring()

    def send(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.itervalues(),[], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send(frame)


class JpegRetriever(object):
    def __init__(self, streamer):
        self.streamer = streamer
        self.pipe = streamer.register()

    def retrieve(self):
        while True:
            ns = os.read(self.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.pipe, n)
            yield data

    def cleanup(self):
        self.streamer.unregister()


class Handler(BaseHTTPRequestHandler):
    retriever = None

    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever

    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')

        if self.path != '/':
            return

        self.send_response(200)
        self.send_header('Content Type', 'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()

        for frame in self.retriever.retriever():
            self.send_frame(frame)

    def send_frame(self, frame):
        self.wfile.write('--abcde\r\n')
        self.wfile.write('Content Type: image/jpeg\r\n')
        self.wfile.write('Content Length: %d\r\n\r\n' % len(frame))


if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()










