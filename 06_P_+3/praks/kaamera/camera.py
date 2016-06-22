import cv2
import datetime
import imutils
import numpy as np
from math import log
from math import log10
def log_tranformation(image):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values

    table = np.array([(log10((i+1) / 255.0)) * 255
		for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)
def laplacianSharpening(img):
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    #showimg(img-laplacian)
    return (img-laplacian)
class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        self.firstFrame = None
        self.contourMinArea = 500
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()


    def get_frame(self):
        text = "Unoccupied"
        success, image = self.video.read()
        # if the frame could not be grabbed, then we have reached the end
        # of the video
        if not success:
            return

        # resize the frame, convert it to grayscale, and blur it
        #frame = imutils.resize(image, width=500)
        frame = image

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        '''
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # if the first frame is None, initialize it
        if self.firstFrame is None:
            self.firstFrame = gray
            return

        # compute the absolute difference between the current frame and
        # first frame
        frameDelta = cv2.absdiff(self.firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts= cv2.findContours(thresh.copy(), cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)[0]

        # loop over the contours
        for c in cnts:
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < self.contourMinArea:
                continue

            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Occupied"

        # draw the text and timestamp on the frame
        cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A, %d %B %Y %H:%M:%S"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        '''
       # frame = laplacianSharpening(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tostring()
