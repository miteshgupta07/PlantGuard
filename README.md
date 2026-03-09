# PlantGuard: A Plant Disease Detection System 🌱

## Overview
PlantGuard is an intelligent deep learning-based plant disease detection system designed to help farmers and gardeners identify and manage crop diseases effectively. Using convolutional neural networks (CNNs), the system classifies images of plant leaves into different disease categories across 9 different plant types, enabling early detection and timely intervention.

**Deployed Version:** Access the live application on the Streamlit platform [here](https://plant-guard.streamlit.app/).

## Supported Plants & Diseases

The system can detect **26+ different conditions** across **9 plant types**:

### 🍎 Apple
- Apple Scab
- Black Rot
- Cedar Apple Rust
- Healthy

### 🍒 Cherry
- Powdery Mildew
- Healthy

### 🌽 Corn
- Common Rust
- Gray Leaf Spot
- Northern Leaf Blight
- Healthy

### 🍇 Grape
- Black Rot
- Esca (Black Measles)
- Leaf Blight
- Healthy

### 🍑 Peach
- Bacterial Spot
- Healthy

### 🌶️ Pepper
- Bacterial Spot
- Healthy

### 🥔 Potato
- Early Blight
- Late Blight
- Healthy

### 🍓 Strawberry
- Leaf Scorch
- Healthy

### 🍅 Tomato
- Bacterial Spot
- Early Blight
- Late Blight
- Healthy

## Methodology
The project employs **DenseNet**, a state-of-the-art deep learning architecture known for its dense connectivity pattern, which enhances feature propagation and encourages feature reuse. Each plant type has a dedicated fine-tuned model trained on the PlantVillage dataset, ensuring specialized and accurate disease classification.

**Model Architecture:**
- Base: DenseNet (pre-trained on ImageNet)
- Input Size: 256x256 pixels
- Output: Multi-class classification (plant-specific diseases)
- Total Models: 9 specialized models (one per plant type)

## Features
✅ Detection of 26+ plant diseases across 9 crop types  
✅ User-friendly web interface with real-time predictions  
✅ Comprehensive disease information including:
  - Detailed descriptions
  - Symptoms identification
  - Treatment recommendations
  - Preventive measures  
✅ Plant type selection for targeted disease detection  
✅ Image upload support (JPEG, PNG, JPG)  
✅ Visual feedback with prediction confidence  
✅ Dockerized deployment for easy setup  

## Technologies Used
- **Python 3.9+**
- **TensorFlow 2.15.0** - Deep learning framework
- **Keras** - Neural network API
- **Streamlit 1.30.0** - Web application framework
- **NumPy 1.24.4** - Numerical computing
- **Pandas 2.2.0** - Data manipulation
- **Matplotlib 3.8.4** - Visualization
- **Docker** - Containerization

## Project Structure
```
PlantGuard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── LICENSE.txt                     # License information
├── README.md                       # Project documentation
├── Dataset/
│   ├── train/                      # Training images (organized by plant/disease)
│   ├── valid/                      # Validation images
│   └── test/                       # Test images
├── models/
│   ├── apple_model.h5             # Apple disease detection model
│   ├── cherry_model.h5            # Cherry disease detection model
│   ├── corn_model.h5              # Corn disease detection model
│   ├── grape_model.h5             # Grape disease detection model
│   ├── peach_model.h5             # Peach disease detection model
│   ├── pepper_model.h5            # Pepper disease detection model
│   ├── potato_model.h5            # Potato disease detection model
│   ├── strawberry_model.h5        # Strawberry disease detection model
│   └── tomato_model.h5            # Tomato disease detection model
├── src/
│   └── disease_information.py     # Disease descriptions and treatments
├── notebooks/
│   └── *.ipynb                    # Model training notebooks
└── test/
    └── Model Testing.ipynb        # Model evaluation notebook
```

## Dataset
The project uses the **PlantVillage Dataset** with the following structure:
- **Training Set**: Images organized by plant type and disease category
- **Validation Set**: Separate validation images for model tuning
- **Test Set**: Hold-out test set for final evaluation

Images are RGB, resized to 256x256 pixels for model input.

## Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Docker (optional, for containerized deployment)

## Getting Started

### Local Installation

1. **Clone the repository:**
```bash
git clone https://github.com/miteshgupta07/PlantGuard.git
cd PlantGuard
```

2. **Create and activate a virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit application:**
```bash
streamlit run app.py
```

5. **Access the application:**
   - Open your browser and navigate to `http://localhost:8501`

### Docker Deployment

1. **Build the Docker image:**
```bash
docker build -t plantguard:latest .
```

2. **Run the container:**
```bash
docker run -p 8501:8501 plantguard:latest
```

3. **Access the application:**
   - Open your browser and navigate to `http://localhost:8501`

## Usage
1. Select the plant type from the dropdown menu (Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, or Tomato)
2. Upload an image of a plant leaf (supported formats: JPEG, PNG, JPG)
3. Click the "Predict Disease" button
4. View the prediction results with:
   - Disease name or healthy status
   - Disease description
   - Symptoms to look for
   - Treatment recommendations

## Model Training
Individual Jupyter notebooks for each plant type are available in the `notebooks/` directory. These notebooks contain:
- Data preprocessing steps
- Model architecture definition
- Training and validation procedures
- Performance evaluation metrics

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For bug reports or feature requests, please open an issue with detailed information.

## License
This project is licensed under the terms specified in the LICENSE.txt file.

## Acknowledgements
- **Dataset**: PlantVillage Dataset from Kaggle
- **Framework**: TensorFlow and Keras teams
- **Inspiration**: Agricultural technology and deep learning research community
- **Special Thanks**: To all contributors and users of this project

## Future Enhancements
- [ ] Add more plant species and disease types
- [ ] Implement mobile application
- [ ] Include severity assessment for detected diseases
- [ ] Multi-language support for global accessibility
- [ ] Integration with weather data for preventive alerts
- [ ] Batch processing for multiple images

## Contact
For inquiries, collaborations, or support:
- **Email**: miteshgupta2711@gmail.com

---
*Made with ❤️ for farmers and gardeners worldwide*
