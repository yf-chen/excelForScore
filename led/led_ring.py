# 环形点亮LED
orders = [[2, 2], [1, 2], [1, 1], [2, 1], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 2], [0, 1], [0, 0],
          [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [3, 4], [2, 4], [1, 4], [0, 4]]
print(orders)


def getMatrix():
    # 环形点亮LED矩阵数组生成逻辑
    n = 5  # 矩阵的大小为 5x5
    matrixs = []  # 先初始化一个全 0 的矩阵
    # 中心坐标
    x, y = n // 2, n // 2
    matrixs.append([x, y])
    # 方向和步长
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 左、上、右、下
    # steps = [1, 1, 2, 2, 3, 3, 4, 4, 4]  # 每个方向走的步长
    # print(steps)
    ss = []
    for s in range(1, n):
        if (s != n - 1):
            ss.append(s)
            ss.append(s)
        else:
            ss.append(s)
            ss.append(s)
            ss.append(s)
    print(ss)
    direction_idx = 0  # 当前方向的索引
    for step in ss:
        for i in range(0, step):
            dx, dy = directions[direction_idx]
            x += dx
            y += dy
            matrixs.append([x, y])
        if (direction_idx == 3):
            direction_idx = 0
        else:
            direction_idx += 1
    return matrixs


matrix = getMatrix()

print(matrix)
print(matrix)
