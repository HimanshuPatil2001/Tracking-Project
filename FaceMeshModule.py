import cv2
import mediapipe as mp
import time

class FaceMeshDetector():
    def __init__(self,staticMode = False, maxFaces = 2, minDetectionCond = 0.5, minTrackCond = 0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCond = minDetectionCond
        self.minTrackCond = minTrackCond

        self.mpdraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode,self.maxFaces,False,self.minDetectionCond,self.minTrackCond)
        self.drawSpec = self.mpdraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self,img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    face = []
                    self.mpdraw.draw_landmarks(img,faceLms,self.mpFaceMesh.FACEMESH_TESSELATION,
                                          landmark_drawing_spec=self.drawSpec)
                    for id,lm in enumerate(faceLms.landmark):
                        # print(lm)
                        ih,iw,ic = img.shape
                        x,y = int(lm.x*iw), int(lm.y*ih)
                        # print(id,x,y)
                        face.append([x,y])
            faces.append(face)
        return img, faces



def main():
    cap = cv2.VideoCapture("FaceVideos/1.mp4")
    pTime = 0
    detector = FaceMeshDetector()
    while True:
        sucess, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces)!= 0:
            print(faces[0])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS : {int(fps)}', (140, 180), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 15)
        img = cv2.resize(img, (854, 480))
        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()