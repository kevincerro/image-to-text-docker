from fastapi import FastAPI, UploadFile
from PIL import Image
import shutil
import tempfile
import pathlib
import pytesseract

UPLOAD_FOLDER = '/var/www/img'

app = FastAPI()

@app.post("/upload")
def upload_image(image: UploadFile):
    try:
        # Store uploaded image on filesystem
        originalExtension = pathlib.Path(image.filename).suffix
        fileName = tempfile.NamedTemporaryFile(dir='/opt/files', suffix=originalExtension).name
        with open(fileName, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        # Process uploaded image
        img = Image.open(image.file)
        text = pytesseract.image_to_string(img, 'spa')

        return {"status": "ok", "text": text}
    except Exception as e:
        return {"status": "ko", "error": str(e)}
    finally:
        image.close()
    