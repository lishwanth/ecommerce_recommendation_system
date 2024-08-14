import pandas as pd
from sklearn.model_selection import train_test_split

class Preprocessor:
    def __init__(self, data):
        self.data = data

    def preprocess_movielens(self):
        # Implement preprocessing specific to MovieLens dataset
        # Example: Converting ratings to a matrix, normalizing, etc.
        pass

    def preprocess_amazon(self):
        # Implement preprocessing specific to Amazon dataset
        self.data.dropna(subset=['reviewText'], inplace=True)
        self.data['reviewLength'] = self.data['reviewText'].apply(len)
        return self.data

    def split_data(self, test_size=0.2):
        train, test = train_test_split(self.data, test_size=test_size)
        return train, test
