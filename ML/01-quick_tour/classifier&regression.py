# A. 데이터 준비
# B. 분류
# C. 회귀

'''
A. 데이터 준비
    1. 데이터를 x(-1, 1), y(-1, 2) 범위에서 2차함수 형태(y=x^2)로 무작위 생성하고 노이즈를 적용하여 준비
    2. 학습 데이터와 테스트 데이터로 분할 함수 작성
    3. 준비 된 데이터를 분할
    4. 그래프 그리기 (노이즈 있는 데이터와 없는 데이터 전부)
'''

# 1 

import matplotlib.pyplot as plt
import numpy as np

x_max = 1
x_min = -1

y_max = 2
y_min = -1

SCALE = 50

TEST_RATE = 0.3

data_x = np.arange(x_min, x_max, 1/ float(SCALE)).reshape(-1, 1)

data_ty = data_x**2 # 데이터 원본
data_vy = data_ty + np.random.randn(len(data_ty), 1) * 0.5 # 노이즈 적용


# 2
def split_train_set(array):
    length = len(array)
    n_train = int (length * (1-TEST_RATE))

    indices = list(range(length))
    np.random.shuffle(indices)

    idx_train = indices[:n_train]
    idx_test = indices[n_train:]

    return sorted(array[idx_train]), sorted(array[idx_test])

# 3
indices = np.arange(len(data_x))
idx_train, idx_test = split_train_set(indices)

x_train = data_x[idx_train]
y_train = data_vy[idx_train]

x_test = data_x[idx_test]
y_test = data_vy[idx_test]

# 4
def plot_basic_data():
    plt.scatter(data_x, data_vy, label='target')

    plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    plt.show()

'''
B. 분류

원점에서 CLASS_RADIUS 0.6를 분류 기준으로 두고
SVM을 활용해 분류 분포를 학습한다.
'''
# 클래스의 임계값

def classifier():
    CLASS_RADIUS = 0.6

    labels = (data_x**2 + data_vy**2) < CLASS_RADIUS**2

    label_train = labels[idx_train]
    label_test = labels[idx_test]

    # 그래프 그리기

    plt.scatter(x_train[label_train], y_train[label_train], c='black', s=30, marker='*', label='near train')
    plt.scatter(x_train[label_train != True], y_train[label_train != True], c='black', s=30, marker='+', label='far train')

    plt.scatter(x_test[label_test], y_test[label_test], c='black', s=30, marker='^', label='near test')
    plt.scatter(x_test[label_test != True], y_test[label_test != True], c='black', s=30, marker='x', label='far test')

    plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')

    circle = plt.Circle((0,0), CLASS_RADIUS, alpha=0.1, label='near area')
    ax=plt.gca()
    ax.add_patch(circle)

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.show()

    # 학습

    from sklearn import svm
    from sklearn.metrics import confusion_matrix, accuracy_score

    data_train = np.c_[x_train, y_train]
    data_test = np.c_[x_test, y_test]

    classifier = svm.SVC(gamma=1)
    classifier.fit(data_train, label_train.reshape(-1))

    pred_test = classifier.predict(data_test)

    # Accuracy를 표시
    print('accuracy_score:\n', accuracy_score(label_test.reshape(-1), pred_test))

    # 혼동 행렬을 표시
    print('Confusion matrix:\n', confusion_matrix(label_test.reshape(-1), pred_test))


'''
C. 회귀
1차식, 2차식, 9차식을 회귀
'''
def regression():
    from sklearn import linear_model

    ### 1차식으로 회귀

    X1_TRAIN = x_train
    X1_TEST = x_test

    model = linear_model.LinearRegression()
    model.fit(X1_TRAIN, y_train)

    plt.plot(x_test, model.predict(X1_TEST), linestyle='-.', label='poly deg 1')

    ### 2차식으로 회귀

    X2_TRAIN = np.c_[x_train**2, x_train]
    X2_TEST = np.c_[x_test**2, x_test]

    model = linear_model.LinearRegression()
    model.fit(X2_TRAIN, y_train)

    plt.plot(x_test, model.predict(X2_TEST), linestyle='--', label='poly deg 2')

    ### 9차식으로 회귀

    X9_TRAIN_list = tuple(x_train**pow_num for pow_num in range(1, 10))
    X9_TRAIN = np.c_[X9_TRAIN_list]
    X9_TEST_list = tuple(x_test**pow_num for pow_num in range(1, 10))
    X9_TEST = np.c_[X9_TEST_list]

    model = linear_model.LinearRegression()
    model.fit(X9_TRAIN, y_train)

    plt.plot(x_test, model.predict(X9_TEST), linestyle='-',label='poly deg 9')


    plt.scatter(x_train, y_train, c='black', s=30, marker='v',label='train')
    plt.scatter(x_test, y_test, c='black', s=30, marker='x',label='test')

    # 원래 선을 표시
    plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')

    # x축/y축의 범위를 설정
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # 범례의 표시 위치를 지정
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',borderaxespad=0)

    # 그래프를 표시
    plt.show()

### 클러스터링
def clustering():
    from sklearn import cluster

    data = np.c_[data_x, data_vy]

    model = cluster.KMeans(n_clusters=3)
    model.fit(data)

    labels = model.labels_

    plt.scatter(data_x[labels == 0], data_vy[labels == 0], marker='v', label='cluster 0')
    plt.scatter(data_x[labels == 1], data_vy[labels == 1], marker='x', label='cluster 1')
    plt.scatter(data_x[labels == 2], data_vy[labels == 2], marker='o', label='cluster 2')

    plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)


    # 범례의 표시 위치를 지정
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',borderaxespad=0)

    # 그래프를 표시
    plt.show()