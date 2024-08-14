from surprise import SVD
from .base_model import BaseModel

class MatrixFactorization(BaseModel):
    def __init__(self):
        super().__init__()
        self.model = SVD()

    def train(self, trainset):
        self.model.fit(trainset)

    def predict(self, user_id, item_id):
        return self.model.predict(user_id, item_id)

    def evaluate(self, testset):
        return self.model.test(testset)
