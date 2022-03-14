from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

# Set API key.
subscription_key = '0c653ee317cd40bc9615e0b44f55ab8b'

# Set endpoint.
endpoint = 'https://visionclass.cognitiveservices.azure.com/'
# Call API
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# 指定圖檔
local_image_path = os.getcwd() + '/pic/yuping.png'

# 讀取圖片
local_image = open(local_image_path, "rb")
'''
Detect Faces - remote
This example detects faces in a remote image, gets their gender and age, 
and marks them with a bounding box.
'''
print("===== Detect Faces - remote =====")
# Get an image with faces
remote_image_url_faces = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/faces.jpg"
# Select the visual feature(s) you want.
remote_image_features = ["faces"]
# Call the API with remote URL and features
#detect_faces_results_remote = computervision_client.analyze_image(remote_image_url_faces, remote_image_features)
detect_faces_results_remote = computervision_client.analyze_image_in_stream(local_image, remote_image_features)

# Print the results with gender, age, and bounding box
print("Faces in the remote image: ")
if (len(detect_faces_results_remote.faces) == 0):
    print("No faces detected.")
else:
    for face in detect_faces_results_remote.faces:
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))