import cv2

class CameraManager:
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
        self.config = {}

    def capture_frame(self):
        ret, frame = self.webcam.read()
        if ret:
            # rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            return frame
        return None

    def release_camera(self):
        self.webcam.release()

    def setConfig(self, key, value):
        self.config[key] = value
        # Apply the configuration changes to the camera
        # You can add the necessary code here based on your camera library
        print(f"Setting config: {key} = {value}")