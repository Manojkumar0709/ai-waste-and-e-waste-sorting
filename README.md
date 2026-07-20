# ai-waste-and-e-waste-sorting
Build a CPU-friendly image-classification system that identifies waste material categories and provides a confidence-aware sorting recommendation.
Computer Vision for Automated Waste and E-Waste Sorting
A beginner-friendly, CPU-friendly machine learning project that automatically
classifies images of waste and e-waste into categories like plastic, glass,
metal, paper, cardboard, cable, and e-waste — helping identify the right
sorting or recycling stream for each item.

Note: This project classifies visible waste types from images.
It does not detect precious-metal composition or chemical purity —
that would require specialized sensors like X-ray fluorescence (XRF).

What Does This Project Do?
Imagine a conveyor belt full of mixed waste. Instead of a person manually
sorting every item by hand, this project uses a computer vision model to:

Look at a photo of a waste item

Predict which category it belongs to (e.g. "plastic" or "e-waste")

Give a confidence score for that prediction

Recommend a sorting lane, or flag it for manual review if the model is unsure

Why This Project Matters
Recycling and e-waste management are growing global challenges

Manual sorting is slow, costly, and inconsistent

Automated sorting can speed up recycling and reduce human error

This project is a small-scale, practical demonstration of how AI can help

Waste Categories Used
Category	Example items
cardboard	Boxes, packaging
glass	Bottles, jars
paper	Newspaper, documents
plastic	Bottles, containers
metal	Cans, metal scraps
cable	Wires, electrical cables
e_waste	Circuit boards, chargers, electronics
other_waste	Items that don't fit other categories
Datasets Used
This project combines two public datasets:

TrashNet — a well-known dataset with 6 waste categories
(cardboard, glass, paper, plastic, metal, trash)

Kaggle "New Trash Classification Dataset" — adds categories like
cable and e-waste

Both datasets contain real photographs of waste items collected for
research and educatio
