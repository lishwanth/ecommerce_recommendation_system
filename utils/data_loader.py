import pandas as pd
import os
from surprise import Dataset
from surprise.model_selection import train_test_split

class DataLoader:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.data_dir = os.path.join('data', 'raw')

    def download_movielens(self):
        if not os.path.exists(os.path.join(self.data_dir, 'movielens')):
            data = Dataset.load_builtin('ml-100k')
            trainset, testset = train_test_split(data, test_size=0.2)
            return trainset, testset

    def download_amazon_reviews(self):
        # Download Amazon Product Reviews dataset
        amazon_url = "http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/All_Beauty_5.json.gz"
        amazon_reviews_path = os.path.join(self.data_dir, 'amazon_reviews.json.gz')
        if not os.path.exists(amazon_reviews_path):
            df = pd.read_json(amazon_url, lines=True, compression='gzip')
            df.to_csv(os.path.join(self.data_dir, 'amazon_reviews.csv'), index=False)
        return pd.read_csv(os.path.join(self.data_dir, 'amazon_reviews.csv'))
