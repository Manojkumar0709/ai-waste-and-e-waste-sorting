# predict.py
import argparse
from pathlib import Path

from pathlib import Path

# Go one directory up from the notebook folder
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "cnn_e_waste.h5"
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Same classes and order as during training:
classes = [
    "battery", "keyboard", "microwave", "mobile", "mouse",
    "pcb", "player", "printer", "television", "washing_machine"
]

def preprocess_image(image_path, image_size=(64, 64)):
    img = Image.open(image_path).convert("RGB")
    img = img.resize(image_size)
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)  # (1, H, W, 3)
    return arr

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=str, help="Path to image file")
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Image not found: {image_path}")
        return

    model_path = Path("models") / "cnn_e_waste.h5"
    if not model_path.exists():
        print(f"Model file not found: {model_path}")
        return

    print(f"Loading model from: {model_path}")
    model = load_model(model_path)

    arr = preprocess_image(image_path, image_size=(64, 64))
    preds = model.predict(arr)
    idx = np.argmax(preds, axis=1)[0]
    class_name = classes[idx]
    confidence = preds[0][idx]

    print(f"Prediction: {class_name} (confidence {confidence:.2f})")

if __name__ == "__main__":
    main()