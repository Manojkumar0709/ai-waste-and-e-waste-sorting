♻️ AI-Powered E‑Waste Image Classification
Teaching a computer to recognize electronic waste — one image at a time.

</div>

👋 What Is This Project?
Imagine a bin full of discarded electronics: batteries, keyboards, remotes, phones, microwaves.
Instead of a person visually checking each item, this project uses computer vision to look at an image and say:

🔍 “This is a keyboard.” → ⚙️ “Route it to the electronics recycling line.”

This repo is a CPU-friendly prototype of an e‑waste classification module:

A classical baseline (LinearSVC on grayscale images)

A Convolutional Neural Network (CNN) on RGB images

A simple prediction script to test the trained model on new images

⚠️ Honesty note:
This prototype only classifies visible device types (battery, keyboard, etc.).
It does not detect precious-metal content or chemical composition — that would require additional sensors (e.g. spectral data) like in industrial scrap-sorting systems.

✨ How It Works
text
📷 E‑waste image (e.g. battery, keyboard, TV)
      │
      ▼
🧹 Preprocess (resize, RGB, normalize)
      │
      ▼
🧠 Model predicts device class (10 categories)
      │
      ▼
🔁 Used as a building block for automated sorting decisions
There are two main model paths:

Baseline: Grayscale + LinearSVC → fast, simple reference

CNN: RGB + small ConvNet → better at visual details and color

🗂️ Classes the Model Learns
All images are mapped into these 10 classes:

Class	Example Items
battery	AA/AAA cells, rechargeable packs
keyboard	PC keyboards
microwave	Microwave ovens
mobile	Mobile phones / smartphones
mouse	Computer mice
pcb	Printed circuit boards
player	Media players, small consumer devices
printer	Desktop printers
television	TVs, monitors
washing_machine	Washing machines
These categories come from a modified Kaggle e‑waste dataset with balanced classes.

📊 Dataset & Splits
Source: Local copy of a Kaggle e‑waste dataset (10 balanced classes)

Approx. 300 images per class

Splits:

Train: 2400 images

Validation: 300 images

Test: 300 images

Images are indexed into a kaggle_images.csv file with:

split (train / val / test)

orig_class (original folder name)

class (normalized class name)

path (absolute or relative image path)

This makes the pipeline reproducible and notebook‑friendly, as recommended in many image classification projects.

🧠 Models
1️⃣ Baseline: LinearSVC (CPU-Only)
Input: 64×64 grayscale images

Flattened to 4,096 features per image

Model: LinearSVC (scikit‑learn)

Use case: quick, CPU‑friendly baseline

Observations:

Good at large, distinctive items (washing_machine, television)

Struggles with visually similar small devices (mouse, keyboard, mobile, printer)

Expected limitations:

No color information

No spatial structure (flattening loses local patterns)

This baseline is a “sanity check” model to compare against the CNN, similar to classical baselines reported in waste‑classification literature.

2️⃣ CNN: Keras / TensorFlow
Input: 64×64 RGB images (values normalised to )

Architecture (simple ConvNet):

Conv2D(32, 3×3, ReLU) → MaxPooling2D

Conv2D(64, 3×3, ReLU) → MaxPooling2D

Conv2D(128, 3×3, ReLU) → MaxPooling2D

Flatten

Dense(128, ReLU)

Dropout(0.5)

Dense(10, Softmax)

Training:

Loss: sparse_categorical_crossentropy

Optimizer: Adam

Epochs: 15

Batch size: 32

Example performance (test set):

Accuracy: ~63–69%

Macro F1: ~0.63–0.69

Stronger classes:

keyboard, microwave, pcb, washing_machine, television

Still challenging:

mobile, mouse, player, printer (small, similar items)

These values are typical for simple CNNs on small waste datasets and can be improved with larger models, more data, or transfer learning.

The trained CNN is saved as:

text
models/cnn_e_waste.h5
📁 Project Structure
text
ai-e-waste-classification/
├── data/
│   ├── raw/                # Original datasets (not committed)
│   └── processed/          # Optional processed arrays
├── notebook/
│   ├── 01_data_preparation.ipynb
│   ├── 02_baseline_linearSVC.ipynb
│   ├── 03_cnn_training.ipynb
│   ├── kaggle_images.csv   # Index of all images
│   └── predict.py          # CLI prediction script
├── models/
│   └── cnn_e_waste.h5      # Saved CNN model (ignored in Git, stored locally)
├── requirements.txt
├── .gitignore
└── README.md
🚀 Setup Instructions
1️⃣ Clone the repository
bash
git clone https://github.com/your-username/ai-e-waste-classification.git
cd ai-e-waste-classification
2️⃣ Create and activate a virtual environment
bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
3️⃣ Install dependencies
bash
pip install -r requirements.txt
Typical libraries include TensorFlow/Keras, scikit‑learn, NumPy, Pandas, Pillow, Matplotlib, Seaborn, tqdm.

4️⃣ Prepare the dataset
Download your e‑waste dataset (e.g. Kaggle)

Arrange it in:

text
data/raw/modified-dataset/
    train/<class_name>/*.png
    val/<class_name>/*.png
    test/<class_name>/*.png
Run 01_data_preparation.ipynb to:

Count images per class and split

Build kaggle_images.csv

5️⃣ Train the CNN (optional if you already have cnn_e_waste.h5)
Run 03_cnn_training.ipynb to:

Load kaggle_images.csv

Build X_train, y_train, X_val, y_val, X_test, y_test

Train the CNN

Save models/cnn_e_waste.h5

🔁 Prediction: Test the Model on New Images
Once cnn_e_waste.h5 exists, you can classify new images via the CLI script.

From the notebook/ folder:

bash
cd notebook
python predict.py "C:\path\to\your_image.png"
The script will:

Load the saved CNN model

Preprocess the image (RGB, 64×64, normalised)

Print:

Image path

Predicted class name

Confidence score

This is similar to prediction scripts used in other image‑classification projects.

⚠️ Limitations
Trained on a moderate-sized dataset → may not generalize to all real‑world e‑waste

Uses only RGB images:

No spectral data

No depth / 3D information

No integration yet with:

Conveyor belts

PLC/SCADA

Real-time plant monitoring

This is intentionally a prototype, designed to be a realistic building block rather than a complete industrial solution.

🔮 Future Directions
Possible next steps:

📈 Improve accuracy:

Transfer learning (e.g. MobileNetV2, ResNet)

Data augmentation tuned per class

🧪 Multi‑modal fusion:

Combine image features with spectral data (e.g. NIR, XRF)

🏭 Integration:

Simple sorting logic (class → route)

Logging predictions for analysis

Simple GUI (Tkinter / Streamlit) for operator use

📄 License
Licensed under the MIT License.
You’re free to study, adapt, and extend this prototype.

<div align="center">

Built with 🐍 Python, 🧠 CNNs, and a focus on practical, CPU-first ML.

</div>
