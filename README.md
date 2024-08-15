
# E-commerce Recommendation System

## Overview

This project is a modular recommendation system for e-commerce platforms. It leverages Object-Oriented Programming (OOP) principles and integrates a variety of open-source tools to build, train, and evaluate personalized product recommendation models. The system uses popular datasets such as MovieLens and Amazon Product Reviews to develop models that suggest relevant products to users based on their historical interactions.

## Tools and Technologies Used

### 1. **Python**
   - **Role:** The core programming language used to develop the entire project, including data processing, model building, and evaluation.

### 2. **TensorFlow**
   - **Role:** Used to implement the Neural Collaborative Filtering model. TensorFlow provides a flexible and efficient platform for building and training deep learning models.

### 3. **PyTorch**
   - **Role:** Could be used as an alternative to TensorFlow for implementing deep learning models, providing dynamic computational graphs and extensive support for research and development.

### 4. **Pandas**
   - **Role:** Essential for data manipulation and analysis. Pandas is used to handle dataframes, clean data, and perform preprocessing tasks.

### 5. **Surprise Library**
   - **Role:** A specialized Python library designed for building and evaluating recommender systems. It is used to implement the Matrix Factorization model.

### 6. **Neo4j**
   - **Role:** An open-source graph database used to manage and analyze the relationships between users and products, enabling more complex recommendation scenarios.

### 7. **scikit-learn**
   - **Role:** Provides additional tools for data preprocessing, model evaluation, and metrics computation.

### 8. **Matplotlib and Seaborn**
   - **Role:** Used for data visualization to help in understanding the dataset and model performance through plots and graphs.

### 9. **Docker**
   - **Role:** Containerizes the application, ensuring that it runs in a consistent environment across different systems.

### 10. **Jupyter Notebook**
   - **Role:** Used for exploratory data analysis and experimentation. Jupyter Notebooks help in understanding the data and iterating on models.

## Project Structure

```plaintext
ecommerce_recommendation_system/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── datasets/
│
├── models/
│   ├── base_model.py
│   ├── neural_collaborative_filtering.py
│   └── matrix_factorization.py
│
├── utils/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── evaluation.py
│
├── notebooks/
│   └── exploratory_data_analysis.ipynb
│
├── main.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

### Directory Breakdown

- **`data/`:** Contains all the data files.
  - **`raw/`:** Stores raw dataset files.
  - **`processed/`:** Stores preprocessed datasets ready for training.
  - **`datasets/`:** Contains additional dataset files if needed.
  
- **`models/`:** Houses the model implementations.
  - **`base_model.py`:** Abstract base class for all models, ensuring a consistent interface.
  - **`neural_collaborative_filtering.py`:** Implements the Neural Collaborative Filtering model using TensorFlow.
  - **`matrix_factorization.py`:** Implements the Matrix Factorization model using the Surprise library.
  
- **`utils/`:** Utility scripts for data loading, preprocessing, and evaluation.
  - **`data_loader.py`:** Handles downloading and loading datasets.
  - **`preprocess.py`:** Contains functions for cleaning and preprocessing the data.
  - **`evaluation.py`:** Provides evaluation metrics such as RMSE and accuracy.
  
- **`notebooks/`:** Contains Jupyter notebooks for exploratory data analysis.
  - **`exploratory_data_analysis.ipynb`:** Notebook for performing EDA on the datasets.
  
- **`main.py`:** The main script to run the project, training, and evaluating models.
- **`requirements.txt`:** Lists the Python dependencies required to run the project.
- **`Dockerfile`:** Used to containerize the project, ensuring consistent execution environments.

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

## Project Usage

1. **Data Loading:**
   - Use the `DataLoader` class to download and load datasets like MovieLens and Amazon Product Reviews.
   - The datasets are stored in the `data/raw/` directory.

2. **Data Preprocessing:**
   - The `Preprocessor` class cleans and preprocesses the data, making it suitable for training.
   - Preprocessed data is saved in the `data/processed/` directory.

3. **Model Training:**
   - The `main.py` script initializes the models, trains them on the preprocessed data, and evaluates their performance.
   - Models implemented include Neural Collaborative Filtering and Matrix Factorization.

4. **Evaluation:**
   - The `Evaluator` class provides methods to calculate metrics like RMSE and accuracy, allowing for thorough evaluation of the models.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue on GitHub if you have any suggestions or find any bugs.

### License

This project is open-source and available under the [MIT License](LICENSE).

### Acknowledgments

This project leverages multiple open-source libraries and datasets. Special thanks to the developers of TensorFlow, PyTorch, Surprise, and Neo4j, as well as the contributors of the MovieLens and Amazon Product Reviews datasets.
