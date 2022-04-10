import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.models import Sequential

from hosm.S03_real_applications.C09_physical_neural_networks.Ch9_Airfoil_Self_Noise import (
    read_ASNData,
    split_data
)


def keras_fit(X_train, Y_train):
    # Keras Model
    model = Sequential()
    model.add(Dense(20, input_dim=5, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    model.fit(X_train, Y_train, epochs=1000, verbose=1)
    model.summary()
    return model


def keras_predict(model, X_test):
    Y_predKM = model.predict(X_test)
    return Y_predKM


def keras_compare(model, X_test, Y_test):
    score = model.evaluate(X_test, Y_test, verbose=0)
    print('Keras Model')
    print(score[0])
    return score


def plot_predicted_vs_actual(Y_test, Y_pred, title="model"):
    # Plot a comparison diagram
    plt.figure(1)
    plt.subplot(111)
    plt.scatter(Y_test, Y_pred)
    plt.plot((0, 1), "r--")
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.title(title)


if __name__ == "__main__":
    ASNData = read_ASNData()
    X_train, X_test, Y_train, Y_test = split_data(ASNData)

    km = keras_fit(X_train, Y_train)
    Y_predKM = keras_predict(km, X_test)

    plot_predicted_vs_actual(Y_test, Y_predKM, title="Keras Model")
