from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import  os

# Set API key.
subscription_key = '0c653ee317cd40bc9615e0b44f55ab8b'

# Set endpoint.
endpoint = 'https://visionclass.cognitiveservices.azure.com/'

# Call API
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

remote_image_url = "https://i.imgur.com/bWfDWm4.jpg"

# 指定圖檔
local_image_path = os.getcwd() + '/pic/test.jpg'

# 讀取圖片
local_image = open(local_image_path, "rb")

# '''
# Tag an Image - remote
# This example returns a tag (key word) for each thing in the image.
# '''
# print("===== Tag an image - remote =====")
# # Call API with remote image
# tags_result_remote = computervision_client.tag_image(remote_image_url)
#
# # Print results with confidence score
# print("Tags in the remote image: ")
# if (len(tags_result_remote.tags) == 0):
#     print("No tags detected.")
# else:
#     for tag in tags_result_remote.tags:
#         print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

'''
Tag an Image - local
This example returns a tag (key word) for each thing in the image.
'''
print("===== Tag an image - remote =====")
# Call API with local image
tags_result_local = computervision_client.tag_image_in_stream(local_image)


# Print results with confidence score
print("Tags in the local image: ")
if (len(tags_result_local.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_local.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))