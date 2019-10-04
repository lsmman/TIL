'''
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
x_test = data_vy[idx_test]

# 4
plt.scatter(data_x, data_vy, label='target')

plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

plt.show()