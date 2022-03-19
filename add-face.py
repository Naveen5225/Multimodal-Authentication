from aws.rekognition.faces import index_face
from aws.dynamoDB.items import put_item

if __name__ == '__main__':
    image_path = 'images/naveen.jpg'
    person_name = 'Naveen'
    collection_id = 'My-Collection'
    face_id = index_face(collection_id, image_path)
    table_name = 'Faces'
    item = {
        'face-id' : face_id,
        'person-id' : person_name
    }
    put_item(table_name, item)
