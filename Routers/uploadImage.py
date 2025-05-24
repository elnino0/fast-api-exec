from fastapi import APIRouter, UploadFile 
app = APIRouter()
from Services.UploadImageService import ImageUploadService
from typing import List

image_service = ImageUploadService()

@app.post("/upload/image")
async def upload_single_image(file: UploadFile):
    """
    Endpoint for uploading a single image.
    """
    return await image_service.upload_image(file)

@app.post("/upload/images")
async def upload_multiple_images_endpoint(files: List[UploadFile]):
    """
    Endpoint for uploading multiple images.
    """
    return await image_service.upload_multiple_images(files)