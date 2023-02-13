import cv2

from projects.gradio_apps.refaktor.yuzbib import (
    model_yuklash, aniqlash, vector_taq
)

aniqlagich_model = model_yuklash(turi="aniqlagich")
embedding_model = model_yuklash(turi="embedding")


video_joy = "/home/nuriddin/ochiqai/python/projects/gradio_apps/video/as.mp4"
cap = cv2.VideoCapture(video_joy)

embedding_baza = {}
yaqinliklar = []
s = 2
while (True):
    # Capture image frame-by-frame
    ret, frame = cap.read()
    if ret:
        kordinata = aniqlash(aniqlagich_model, frame)
        embedding = embedding_model.get(frame, kordinata)
        embedding.tolist()
        if len(embedding_baza) == 0:
            embedding_baza['1'] = embedding
        else:
            for key in embedding_baza:
                yaqinlik = vector_taq(embedding_baza[key], embedding)
                if yaqinlik < 0.15:
                    embedding_baza['s'] = embedding
                    s = s + 1

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

print(len(embedding_baza))
