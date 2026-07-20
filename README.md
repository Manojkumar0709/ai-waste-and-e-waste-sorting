<div align="center">

# ♻️ Computer Vision for Automated Waste & E-Waste Sorting

**Teaching a computer to recognize trash — so recycling gets a little smarter.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
![Hardware](https://img.shields.io/badge/Runs%20on-CPU%20Only-blue?style=flat-square)
![Made with](https://img.shields.io/badge/Made%20with-Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

</div>

---

## 👋 What Is This Project?

Picture a conveyor belt piled with mixed waste — plastic bottles, old chargers, cardboard, glass. Instead of a person sorting every item by hand, this project uses **computer vision** to look at a photo and instantly say:

> 🔍 *"This is e-waste."* → 🚮 *"Send it to the electronics bin."*

It's a small, practical, CPU-friendly demo of how AI can support smarter recycling — built to be understandable even if you're new to machine learning.

> ⚠️ **Honesty note:** This model recognizes *visible* waste types (plastic, metal, e-waste, etc). It does **not** detect precious-metal content or chemical purity — that needs specialized sensors like XRF.

---

## ✨ How It Works

```text
📷 Photo of waste item
      │
      ▼
🧹 Resize & clean the image
      │
      ▼
🧠 Extract visual features
      │
      ▼
🏷️ Model predicts category + confidence
      │
      ▼
✅ High confidence  →  Correct sorting lane
❓ Low confidence   →  Flagged for manual review
```

---

## 🗂️ Categories the Model Learns

| Emoji | Category | Example Items |
|:---:|---|---|
| 📦 | `cardboard` | Boxes, packaging |
| 🍾 | `glass` | Bottles, jars |
| 📄 | `paper` | Newspaper, documents |
| 🧴 | `plastic` | Bottles, containers |
| 🥫 | `metal` | Cans, scrap metal |
| 🔌 | `cable` | Wires, electrical cables |
| 💻 | `e_waste` | Circuit boards, chargers, electronics |
| 🗑️ | `other_waste` | Anything that doesn't fit above |

---

## 📊 Datasets Used

| Dataset | What It Adds |
|---|---|
| 🌿 [TrashNet](https://github.com/garythung/trashnet) | 6 core waste categories |
| ♻️ Kaggle "New Trash Classification Dataset" | Adds `cable` and `e_waste` |

> 📁 Datasets aren't included in this repo (size + licensing). See [Setup](#-setup-instructions) below to grab them yourself.

---

## 🧠 The Model (No GPU Needed!)

This project is built to run on a normal laptop — **no expensive graphics card required**:

- 🪶 Lightweight pretrained image features (MobileNet)
- 🌳 Fast CPU-friendly classifiers (Random Forest / SVM / Logistic Regression)

---

## 📁 Project Structure

```text
ai-waste-and-e-waste-sorting/
├── data/
│   ├── raw/              🚫 not committed (too large)
│   └── processed/        🧼 cleaned & labeled images
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation.ipynb
├── models/                🚫 not committed
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone this repository

```bash
git clone https://github.com/Manojkumar0709/ai-waste-and-e-waste-sorting.git
cd ai-waste-and-e-waste-sorting
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3️⃣ Install requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Download the datasets

Search on Kaggle for:
- **"TrashNet"**
- **"New Trash Classification Dataset"**

Place them here:

```text
data/raw/trashnet/
data/raw/kaggle_waste/
```

### 5️⃣ Launch Jupyter and run the notebooks

```bash
jupyter notebook
```

Open `notebooks/01_data_preparation.ipynb` and run cells top to bottom. 🎉

---

## 📦 Requirements

```text
pandas
numpy
matplotlib
seaborn
pillow
scikit-learn
tqdm
jupyter
```

---

## 📈 Results (Updated as We Go)

| Metric | Value |
|---|---|
| Model used | *coming soon* |
| Test accuracy | *coming soon* |
| Number of classes | 8 |
| Hardware used | 💻 CPU only |

---

## ⚠️ Limitations

- 🔍 Recognizes visual categories only — not material purity
- 📉 Small dataset → may not generalize to all real-world waste
- 💡 Lighting, angle, and background can affect predictions
- 🏭 Not production-ready without further testing

---

## 🔮 Future Improvements

- [ ] Add more training images per category
- [ ] Try deep learning (fine-tuned MobileNet/ResNet) via free cloud GPUs
- [ ] Build an interactive Streamlit demo
- [ ] Add object detection for multi-item photos

---

## 📄 License

Licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- [TrashNet Dataset](https://github.com/garythung/trashnet) — Gary Thung & Mindy Yang
- Kaggle community for the additional waste dataset

---

<div align="center">

**Made with 🐍 Python, ☕ patience, and a laptop with no GPU**

</div>
