import io, cv2
from google.cloud import vision

def detect_faces(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    deteted = ('UNKNOWN', 'NOO', 'NO', 'Maybe','YES', 'YESS')
    if len(faces) == 0:
        return path, deteted[0]
    else:
        faces = faces[0]
        return path, deteted[face.anger_likelihood], deteted[face.joy_likelihood], deteted[face.sorrow_likelihood], deteted[face.surprise_likelihood]

# # ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
# detect_faces('images/happy.png')

def capture_image(name):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    path = 'static/images/{}.png'.format(name)
    cv2.imwrite(path, frame)
    cap.release()
    cv2.destroyAllWindows()
    return path