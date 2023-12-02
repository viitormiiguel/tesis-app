
# Step 1: Import the all necessary libraries and SDK commands.
import os
import boto3
from botocore.client import Config
import cv2
from urllib.request import urlopen
import numpy as np
from boto3.s3.transfer import S3Transfer

## Digital token
# dop_v1_58d842b32c192e6294ace82e6edaca2cc954b9071bee5b03062a9897e11c13c3

# Secret key
# gm6x1gX/WwtZJ/nwKrZkyv4g4o8xtoP1qGCrQNUGwss

def readFiles():

    response = client.list_objects(Bucket='faces-app')
    # print(response)
    for obj in response['Contents']:
        print(obj)    
        
def viewFile(path):
        
    imagem = "https://" + bucketname + ".nyc3.digitaloceanspaces.com/" + path
    
    resp = urlopen(imagem)
    
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR) # The image object

    # Optional: For testing & viewing the image
    cv2.imshow('image',image)
        
    # Show the image
    cv2.waitKey(0)
        
    return ''
        
def uploadFiles():    
    
    transfer = S3Transfer(client)
    
    # Uploads a file called 'name-of-file' to your Space called 'name-of-space'
    # Creates a new-folder and the file's final name is defined as 'name-of-file' 
    transfer.upload_file('E:/PythonProjects/tesis-app/test/footage/id2/footage1.jpg', bucketname, 'input/id2'+"/"+'footage1.jpg')

    #This makes the file you are have specifically uploaded public by default. 
    response = client.put_object_acl(ACL='public-read', Bucket=bucketname, Key="%s/%s" % ('input/id2', 'footage1.jpg'))

    
    return ''

if __name__ == '__main__':
    
    bucketname = 'faces-app'
    endpoint = 'https://nyc3.digitaloceanspaces.com'
    accesskeyId = 'DO00TNG3HW3H4C8JFAFF'
    secretKey = 'gm6x1gX/WwtZJ/nwKrZkyv4g4o8xtoP1qGCrQNUGwss'
    
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='nyc3',
                            endpoint_url=endpoint,
                            aws_access_key_id=accesskeyId,
                            aws_secret_access_key=secretKey)
    
    # readFiles()
    
    # viewFile('input/id1/footage1.jpg')
    
    uploadFiles()