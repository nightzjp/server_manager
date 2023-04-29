import cv2

from func_timeout import func_set_timeout, exceptions


def check_rtsp_stream(url):
    @func_set_timeout(2)
    def parse_rtsp_stream(rtsp_address):
        try:
            cap = cv2.VideoCapture(rtsp_address)
            cap.set(cv2.CAP_PROP_FPS, 1)
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
            cap.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
            cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"H264"))
            cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)
            cap.set(cv2.CAP_PROP_BRIGHTNESS, 50)
            cap.set(cv2.CAP_PROP_CONTRAST, 50)
            cap.set(cv2.CAP_PROP_SATURATION, 50)
            cap.set(cv2.CAP_PROP_HUE, 50)
            cap.set(cv2.CAP_PROP_GAIN, 50)
            cap.set(cv2.CAP_PROP_EXPOSURE, 50)
            cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
            if cap.isOpened():
                cap.release()
                return True
            else:
                return False
        except cv2.error as e:
            return False

    try:
        return parse_rtsp_stream(url)
    except exceptions.FunctionTimedOut:
        return False
