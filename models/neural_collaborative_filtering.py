import tensorflow as tf
from .base_model import BaseModel

class NeuralCollaborativeFiltering(BaseModel):
    def __init__(self, num_users, num_items, embedding_size=50):
        super().__init__()
        self.num_users = num_users
        self.num_items = num_items
        self.embedding_size = embedding_size
        self.model = self.build_model()

    def build_model(self):
        user_input = tf.keras.layers.Input(shape=(1,))
        item_input = tf.keras.layers.Input(shape=(1,))

        user_embedding = tf.keras.layers.Embedding(self.num_users, self.embedding_size)(user_input)
        item_embedding = tf.keras.layers.Embedding(self.num_items, self.embedding_size)(item_input)

        dot_product = tf.keras.layers.dot([user_embedding, item_embedding], axes=2)
        output = tf.keras.layers.Flatten()(dot_product)
        output = tf.keras.layers.Dense(1, activation='sigmoid')(output)

        model = tf.keras.Model(inputs=[user_input, item_input], outputs=output)
        model.compile(optimizer='adam', loss='binary_crossentropy')
        return model

    def train(self, train_data, epochs=10, batch_size=32):
        user_input, item_input, labels = train_data
        self.model.fit([user_input, item_input], labels, epochs=epochs, batch_size=batch_size)

    def predict(self, user_id, item_id):
        return self.model.predict([user_id, item_id])

    def evaluate(self, test_data):
        user_input, item_input, labels = test_data
        return self.model.evaluate([user_input, item_input], labels)
