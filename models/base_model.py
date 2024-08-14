class BaseModel:
    def __init__(self):
        pass

    def train(self, data):
        raise NotImplementedError("Train method not implemented!")

    def predict(self, user_id, item_id):
        raise NotImplementedError("Predict method not implemented!")

    def evaluate(self, test_data):
        raise NotImplementedError("Evaluate method not implemented!")
