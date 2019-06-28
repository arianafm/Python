import json
from ibm_watson import VisualRecognitionV3

#Fecha de la versión:
visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey= '_qMfGOYADh9XYx4qCXHeu4feTcvuPRR564s41W7U1g_H')

with open('./arianafm.jpg','rb') as image_file:
	faces = visual_recognition.detect_faces(image_file).get_result()

print(json.dumps(faces, indent = 2))

#Watson tiene algoritmos por detras que son capaces de hacer esto...

"""
Nos devuelve un json:
{
  "images": [
    {
      "faces": [
        {
          "age": {
            "min": 19, #Te da un apróx de su edad 
            "max": 22,
            "score": 0.96091753 #Qué tan acertado fue su pronostico.
          },
          "face_location": {
            "height": 114,
            "width": 97,
            "left": 44,
            "top": 41
          },
          "gender": {
            "gender": "FEMALE", #Te da su género
            "gender_label": "female",
            "score": 0.99999464
          }
        }
      ],
      "image": "ariana.jpg"
    }
  ],
  "images_processed": 1
}
"""