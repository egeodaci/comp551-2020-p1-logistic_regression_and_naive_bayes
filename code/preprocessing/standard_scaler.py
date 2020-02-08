from math import sqrt


# calculate column means
def column_means(dataset):
    means = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        means[i] = sum(col_values) / float(len(dataset))
    return means


# calculate column standard deviations
def column_stdevs(dataset, means):
    stdevs = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        variance = [pow(row[i] - means[i], 2) for row in dataset]
        stdevs[i] = sum(variance)
    stdevs = [sqrt(x / (float(len(dataset) - 1))) for x in stdevs]
    return stdevs


def standardize_dataset(dataset):

    means = column_means(dataset)
    stdevs = column_stdevs(dataset, means)

    for row in dataset:
        for i in range(len(row)):
            if stdevs[i] == 0:
                row[i] = 0
            else:
                row[i] = (row[i] - means[i]) / stdevs[i]

    return dataset


def feature_scaling(X_train, X_test):
    # TODO: Do without use scikit-learn
    # TODO: Change according selected dataset
    # Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    #
    # return X_train, X_test

    X_train = standardize_dataset(X_train.astype(float))

    X_test = standardize_dataset(X_test.astype(float))

    return X_train, X_test