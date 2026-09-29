import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("FaceVideos/1.mp4")
pTime = 0
mpdraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpdraw.DrawingSpec(thickness=1, circle_radius=2)
while True:
    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpdraw.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_TESSELATION,
                                  landmark_drawing_spec=drawSpec)

            for id,lm in enumerate(faceLms.landmark):
                # print(lm)
                ih,iw,ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                print(id,x,y)

    cTime = time.time()
    fps = 1/ (cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS : {int(fps)}', (140, 180), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 15)
    img = cv2.resize(img, (854, 480))
    cv2.imshow("image", img)
    cv2.waitKey(1)