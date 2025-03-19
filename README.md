# AI-Powered Endangered Species Tracker with Citizen Science Integration

## Overview

The **AI-Powered Endangered Species Tracker with Citizen Science Integration** is an innovative, real-time solution designed to protect endangered species through the power of Artificial Intelligence (AI) and crowdsourced data. Using advanced computer vision (YOLO, ResNet) and audio machine learning techniques (librosa, TensorFlow), this project aims to identify, track, and protect endangered animals (e.g., rhinos, pangolins) through camera traps or audio recordings. Additionally, the system integrates a citizen science platform where users can submit species sightings to train and refine the model further.

By leveraging real-time data and the collective efforts of a global community, this project helps in the identification of species, detection of poaching activities, and mapping of wildlife habitats. It collaborates with conservation NGOs to source real-world data and integrates geospatial AI (Google Earth Engine) to map habitats and predict potential poaching hotspots.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **AI-Driven Species Identification**
  - Uses YOLO and ResNet to identify endangered species from images and videos.
  - Utilizes TensorFlow and librosa for detecting animal calls in audio recordings.

- **Poaching Detection**
  - Flags suspicious activity around endangered species using AI-powered real-time data processing.

- **Crowdsourced Data Platform**
  - Allows users to upload sightings of endangered species to improve AI training and accuracy.

- **Geospatial AI for Habitat Mapping**
  - Uses Google Earth Engine to analyze and predict poaching hotspots.

- **Collaboration with NGOs**
  - Partners with conservation organizations to ensure real-world impact and credibility.

## Installation

### Prerequisites

- Python 3.x
- TensorFlow
- Flask/Django (for the crowdsourcing platform)
- Google Earth Engine account (for habitat mapping)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/endangered-species-tracker.git
   cd endangered-species-tracker
   ```

2. **Install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up the crowdsourcing platform** (Flask/Django):
   Follow instructions in the `crowdsourcing/README.md`.

4. **Google Earth Engine setup**:
   Sign up for Google Earth Engine and follow setup instructions [here](https://developers.google.com/earth-engine/guides/python_install).

5. **Train and Deploy the AI Model**:
   Follow instructions in `model_training/README.md`.

6. **Run the system**:
   ```bash
   python app.py
   ```

7. **Access the web platform**:
   Visit `http://localhost:5000`.

## Usage

### Endangered Species Identification

- Uses computer vision and audio ML to detect species in images, videos, and sound recordings.

### Crowdsourcing Sightings

- Users submit sightings via the web app, improving AI model training over time.
  
### Habitat Mapping & Poaching Detection

- Google Earth Engine maps wildlife habitats and predicts high-risk poaching zones.

## Technologies

- **Computer Vision**: YOLO, ResNet
- **Audio ML**: TensorFlow, librosa
- **Web Framework**: Flask/Django
- **Geospatial AI**: Google Earth Engine
- **ML Libraries**: TensorFlow, scikit-learn
- **Cloud Storage**: AWS S3, Google Cloud Storage

## Project Structure

```
/endangered-species-tracker
├── app.py                # Main application entry point
├── model_training        # Model training scripts
│   ├── train.py
│   ├── evaluate.py
│   ├── data_preprocessing.py
├── crowdsourcing         # Flask/Django app for citizen science
│   ├── app.py
│   ├── templates/
│   ├── static/
├── geospatial            # Google Earth Engine integration
│   ├── habitat_mapping.py
│   ├── poaching_prediction.py
└── requirements.txt      # Python dependencies
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Conservation NGOs**: Special thanks to our partners for providing invaluable data.
- **Google Earth Engine**: For geospatial analytics and habitat mapping.
- **YOLO and ResNet**: For cutting-edge computer vision models.
- **TensorFlow & librosa**: For enabling audio-based species detection.

