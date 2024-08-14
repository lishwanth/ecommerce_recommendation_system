
# E-commerce Recommendation System

## Overview

This project is a modular recommendation system for e-commerce platforms, built using open-source tools and following Object-Oriented Programming (OOP) principles. The goal of this system is to provide personalized product recommendations to users based on their historical interactions with products. The project integrates multiple models, including Neural Collaborative Filtering and Matrix Factorization, and makes use of popular datasets such as MovieLens and Amazon Product Reviews.

## Features

- **Modular Design:** The project is structured in a modular way, making it easy to extend and maintain.
- **Multiple Models:** Implements Neural Collaborative Filtering using TensorFlow and Matrix Factorization using the Surprise library.
- **Graph Database:** Utilizes Neo4j, an open-source graph database, to manage relationships between users and products.
- **Open-Source Datasets:** The system is trained and evaluated on well-known datasets like MovieLens and Amazon Product Reviews.
- **Dockerized Deployment:** The entire project can be containerized using Docker for easy deployment.

## Project Structure

- `data/`: Contains raw and processed datasets.
  - `raw/`: Raw dataset files.
  - `processed/`: Preprocessed datasets ready for model training.
- `models/`: Includes different recommendation model implementations.
  - `base_model.py`: Abstract base class for all recommendation models.
  - `neural_collaborative_filtering.py`: Implementation of Neural Collaborative Filtering using TensorFlow.
  - `matrix_factorization.py`: Implementation of Matrix Factorization using the Surprise library.
- `utils/`: Utility scripts for data loading, preprocessing, and evaluation.
  - `data_loader.py`: Handles downloading and loading datasets.
  - `preprocess.py`: Contains functions for preprocessing data.
  - `evaluation.py`: Provides evaluation metrics such as RMSE and accuracy.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and other experimental tasks.
- `main.py`: Entry point of the project, where models are trained and evaluated.
- `Dockerfile`: Defines the Docker image for containerizing the application.
- `requirements.txt`: Lists all Python dependencies required to run the project.

## Setup Instructions

### Prerequisites

- Python 3.8 or later installed on your system.
- Docker (optional, for containerization).

### Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
```

2. **Install the Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Project:**

```bash
python main.py
```

### Docker Setup

If you prefer to run the project in a Docker container:

1. **Build the Docker Image:**

```bash
docker build -t ecommerce-recommender .
```

2. **Run the Docker Container:**

```bash
docker run -it --rm ecommerce-recommender
```

### Project Usage

1. **Data Loading:**
   - The `DataLoader` class is used to download and load datasets like MovieLens and Amazon Product Reviews.
   - Datasets are saved in the `data/raw/` directory.

2. **Data Preprocessing:**
   - The `Preprocessor` class handles cleaning and preprocessing of the data.
   - Preprocessed data is saved in the `data/processed/` directory.

3. **Model Training:**
   - The `main.py` script initializes the models, trains them on the preprocessed data, and evaluates their performance.
   - Both Neural Collaborative Filtering and Matrix Factorization models can be trained and evaluated using this script.

4. **Evaluation:**
   - The `Evaluator` class provides methods to calculate metrics like RMSE and accuracy, allowing for thorough evaluation of the models.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue on GitHub if you have any suggestions or find any bugs.

### License

This project is open-source and available under the [MIT License](LICENSE).

### Acknowledgments

This project leverages multiple open-source libraries and datasets. Special thanks to the developers of TensorFlow, PyTorch, Surprise, and Neo4j, as well as the contributors of the MovieLens and Amazon Product Reviews datasets.
