from sklearn.metrics import mean_squared_error, accuracy_score

class Evaluator:
    def __init__(self):
        pass

    def rmse(self, true_ratings, predicted_ratings):
        return mean_squared_error(true_ratings, predicted_ratings, squared=False)

    def accuracy(self, true_labels, predicted_labels):
        return accuracy_score(true_labels, predicted_labels)
