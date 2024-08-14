from utils.data_loader import DataLoader
from utils.preprocess import Preprocessor
from utils.evaluation import Evaluator
from models.neural_collaborative_filtering import NeuralCollaborativeFiltering
from models.matrix_factorization import MatrixFactorization

def main():
    # Load Data
    data_loader = DataLoader('amazon')
    amazon_data = data_loader.download_amazon_reviews()

    # Preprocess Data
    preprocessor = Preprocessor(amazon_data)
    processed_data = preprocessor.preprocess_amazon()

    # Split Data
    train_data, test_data = preprocessor.split_data()

    # Initialize Models
    ncf_model = NeuralCollaborativeFiltering(num_users=1000, num_items=1000)
    mf_model = MatrixFactorization()

    # Train Models
    ncf_model.train(train_data)
    mf_model.train(train_data)

    # Evaluate Models
    evaluator = Evaluator()
    ncf_rmse = evaluator.rmse(test_data['rating'], ncf_model.predict(test_data['userId'], test_data['itemId']))
    mf_rmse = evaluator.rmse(test_data['rating'], mf_model.predict(test_data['userId'], test_data['itemId']))

    print(f"NCF RMSE: {ncf_rmse}")
    print(f"MF RMSE: {mf_rmse}")

if __name__ == "__main__":
    main()
