"""
K-fold cross validation

In k-fold cross-validation (k-fold CV),
the set of observations is randomly divided into k groups, or folders, of approximately equal size.

The first folder is considered as a validation set and the function is estimated on the remaining k-1 folders.

The mean square error MSE 1 is then calculated on the observations of the folder that's kept out.

This procedure is repeated k times,
each time choosing a different folder for validation,
thus obtaining k estimates of the test error.

The k-fold CV estimate is calculated by averaging these values, as follows:

𝑘𝑘
1
𝐶𝐶𝐶𝐶 (𝑘𝑘) = ∑ 𝑀𝑀𝑀𝑀𝑀𝑀 𝑖𝑖
𝑘𝑘
𝑖𝑖=1

This method has the advantage of being less computationally intensive if k << n.
Furthermore, the k-fold CV tends to have less variability than the LOOCV on different size datasets n.

Choosing k is crucial in k-fold cross-validation.
What happens when k changes in cross validation?

Let's see what an extreme choice of k entails:

• A high k value results in larger training sets and therefore less bias.
This implies small validation sets, and therefore greater variance.

• A low k value results in smaller training sets and therefore greater bias.
This implies larger validation sets, and therefore low variance.

Cross-validation using Python
In this section, we will look at an example of the application of cross-validation.
First, we will create an example dataset that contains simple data to identify in order to verify the
procedure being performed by the algorithm.
Then, we will apply k-fold cross-validation and analyze the results:
"""

import numpy as np
from sklearn.model_selection import KFold


def kfcv():
    StartedData = np.arange(10, 110, 10)
    print(StartedData)

    kfold = KFold(
        n_splits=5,
        shuffle=True,
        random_state=1
    )

    for TrainData, TestData in kfold.split(StartedData):
        print("Train Data :", StartedData[TrainData], "Test Data :", StartedData[TestData])


if __name__ == "__main__":
    kfcv()
