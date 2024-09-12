from deepface import DeepFace

def match(inputed_image):
    dfs = DeepFace.find(
        img_path = inputed_image,
        db_path = 'images',
        model_name = 'Facenet512'
    )
