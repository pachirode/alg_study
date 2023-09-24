# python 实现梯度下降算法
# L(x, y) = x**2 + 2y**3

x = 2
y = 3
iter_num = 0
iter_step = 0.01
threshold = 1e-6
loss = 1
l = x ** 2 + 2 * y ** 3
l_lis = [l]
loss_lis = []

while loss > threshold:
    x = x - iter_step * 2 * x
    y = y - iter_step * 6 * y ** 2 
    loss = abs(x ** 2 + 2 * y ** 3 - l)
    loss_lis.append(loss)
    l = x ** 2 + 2 * y ** 3
    iter_num = iter_num + 1
    l_lis.append(l)

print("Iteration number: {}, value: {}".format(iter_num, l))
