# Newton's iteration method for solving nonlinear equations
# f1 = 2x**2 -4x -2y + 1 = 0
# f2 = x**2 + 4y**2 -4 = 0
# F' = [4x - 4, -2]
#      [    2x, 8y] 
# F'-1 = 1 / 4 * (8xy - 8y -x)
# x2 = x1 - (8x**2y - 16xy -4y**2 + x**2 + 4y - 4) / (8xy -8y -x) 
# y2 = y1 - (-x**3 + 3x**2 +2xy -9x + 8xy**2 - 4y**2 + 4) / (8xy -8y -x)
import matplotlib.pyplot as plt

def newtown_iteration(res):
    x = res[0]
    y = res[1]
    denominator = 8 * x * y - 8 * y - x
    res_new = [
        x - (8 * x**2 * y - 16 * x * y - 4 * y**2 + x**2 + 4 * y - 4) / denominator,
        y - (-x**3 + 3 * x**2 + 2 * x * y - 9 * x + 8 * x * y**2 - 4 * y**2 + 4) / denominator
    ]
    return res_new

def is_accuaracy_achieved(res, res_new, threshold=1e-5):
    if (abs(res_new[0] - res[0]) < threshold and abs(res_new[1] - res[1]) < threshold):
        return True
    return False

if __name__ == "__main__":
    res = [-1.5, 0.5]
    res_list = [res]
    max_iter_num = 10000
    iter_num = 0
    plt.scatter(res[0], res[1], s=20, c='r', label="original")
    while iter_num < max_iter_num:
        res_new = newtown_iteration(res)
        res_list.append(res_new)
        plt.scatter(res_new[0], res_new[1], s=20, c='b', label=iter_num)
        if is_accuaracy_achieved(res, res_new):
            break
        iter_num = iter_num + 1
        res = res_new
    print("Iter_num: {}, res {}".format(iter_num, res))
    plt.show()

