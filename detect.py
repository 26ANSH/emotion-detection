import io, cv2
from google.cloud import vision

def detect_faces(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    deteted = ['UNKNOWN', 'NOO', 'NO', 'Maybe','YES', 'YESS']
    if len(faces) == 0:
        print(deteted[0])
        return deteted[0]
    else:
        face = faces[0]
        print(face)
        return f"\nAnger : {deteted[face.anger_likelihood]} \n Joy : {deteted[face.joy_likelihood]} \n Sorrow : {deteted[face.sorrow_likelihood]}  \n Shock : {deteted[face.surprise_likelihood]} \n"

# # ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
# detect_faces('images/happy.png')

def capture_image(name):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    path = 'static/images/{}.png'.format(name)
    cv2.imwrite(path, frame)
    cap.release()
    cv2.destroyAllWindows()
    return path