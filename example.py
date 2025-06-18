import numpy as np
import matplotlib.pyplot as plt

# 假设 factorizations_r.npz 文件位于 alphatensor/algorithms 目录下
data_path = 'C:/Users/Yizen/OneDrive/Documents/Study/Thesis/code/alphatensor-main/alphatensor/algorithms/factorizations_r.npz'
data = np.load(data_path)
print("数据文件中包含的键：", list(data.keys()))

# 假设数据中存储了一个 4x4 矩阵乘法的因式分解，键名称可能为 "U_example", "V_example", "W_example"
# 你需要根据数据实际结构进行调整
U = data.get('U_example')
V = data.get('V_example')
W = data.get('W_example')

if U is not None and V is not None and W is not None:
    print("U =", U)
    print("V =", V)
    print("W =", W)
else:
    print("请检查数据文件中包含的键名称。")

# 此处你还可以添加代码对因式进行可视化或利用算法进行矩阵乘法的验证
