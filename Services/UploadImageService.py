

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import io
import os
from typing import List

class ImageUploadService:
    """
    A service class for handling image uploads with FastAPI.
    """
    def __init__(self, upload_folder="uploads", allowed_extensions=None, max_file_size=10 * 1024 * 1024):
        """
        Initializes the ImageUploadService.

        Args:
            upload_folder (str): The folder to save uploaded images.
            allowed_extensions (List[str], optional): A list of allowed image file extensions (e.g., ['.jpg', '.jpeg', '.png']).
                                                     Defaults to allowing all common image types if None.
            max_file_size (int): The maximum allowed file size in bytes (default: 10MB).
        """
        self.upload_folder = upload_folder
        if allowed_extensions is None:
            self.allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
        else:
            self.allowed_extensions = [ext.lower() for ext in allowed_extensions]
        self.max_file_size = max_file_size
        os.makedirs(self.upload_folder, exist_ok=True)

    async def upload_image(self, file: UploadFile):
        """
        Handles the upload of a single image file.

        Args:
            file (UploadFile): The uploaded file object from FastAPI.

        Returns:
            JSONResponse: A JSON response indicating the status and filename.

        Raises:
            HTTPException: If the file is invalid (size, extension, or content).
        """
        if file.size > self.max_file_size:
            raise HTTPException(status_code=400, detail=f"File size exceeds the limit of {self.max_file_size / (1024 * 1024):.2f} MB.")

        file_extension = os.path.splitext(file.filename)[1].lower()
        if self.allowed_extensions and file_extension not in self.allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file extension. Allowed extensions are: {', '.join(self.allowed_extensions)}",
            )

        try:
            img = Image.open(io.BytesIO(await file.read()))
            filename = f"{os.urandom(16).hex()}{file_extension}"
            file_path = os.path.join(self.upload_folder, filename)
            img.save(file_path)
            return JSONResponse(status_code=200, content={"message": "Image uploaded successfully", "filename": filename})
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image file: {e}")

    async def upload_multiple_images(self, files: List[UploadFile]):
        """
        Handles the upload of multiple image files.

        Args:
            files (List[UploadFile]): A list of uploaded file objects from FastAPI.

        Returns:
            JSONResponse: A JSON response indicating the status and a list of filenames.

        Raises:
            HTTPException: If any of the files are invalid.
        """
        filenames = []
        for file in files:
            if file.size > self.max_file_size:
                raise HTTPException(
                    status_code=400,
                    detail=f"File '{file.filename}' exceeds the limit of {self.max_file_size / (1024 * 1024):.2f} MB.",
                )

            file_extension = os.path.splitext(file.filename)[1].lower()
            if self.allowed_extensions and file_extension not in self.allowed_extensions:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid file extension for '{file.filename}'. Allowed extensions are: {', '.join(self.allowed_extensions)}",
                )

            try:
                img = Image.open(io.BytesIO(await file.read()))
                filename = f"{os.urandom(16).hex()}{file_extension}"
                file_path = os.path.join(self.upload_folder, filename)
                img.save(file_path)
                filenames.append(filename)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Invalid image file '{file.filename}': {e}")

        return JSONResponse(status_code=200, content={"message": "Images uploaded successfully", "filenames": filenames})