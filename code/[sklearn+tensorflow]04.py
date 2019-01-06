'''
***说明：本文依据《Sklearn 与 TensorFlow 机器学习实用指南》完成，所有版权和解释权均归作者和翻译成员所有，我只是搬运和做注解。***
第四章是对模型训练内部工作流程的了解，帮助炼丹师们找到恰当的学习模型、算法、数据集。  
**为了尽量简单（懒），在这里默认已经了解线性回归、多项式回归、损失函数、梯度下降**
### 1. 简单的线性回归模型，讨论两种不同训练方法的最优解
- 封闭方程求根运算，得到模型在当前训练集上的最优解。
- 迭代优化（梯度下降GD），调整模型参数获取最小损失函数。批量梯度下降、随机梯度下降、小批量梯度下降。
### 2. 多项式回归，用来拟合非线性数据集
- 介绍正则方式减少过拟合的出现
- 介绍Logistic回归和Softmax回归

### 1. 线性回归
线性模型的描述指**通过计算输入变量的加权和，并加上一个常数偏置项（截距项）来得到一个预测值**。  
#### 线性回归模型的表示
y=θ_0+θ_1x_1+θ_2x_2+...+θ_nx_n  
- y表示预测结果
- n表示特征个数
- x_i表示第i个特征的数值
- θ_j表示第j个参数
y=h_θ(X)=θ^TX
- 这是上式的向量化表示，在吴恩达机器学习教程中有专门提到。
- θ^TX表示θ^T和X的点积
- h_θ(X)表示参数为θ的假设函数
#### 线性回归模型的训练
**均方根误差RMSE或均方误差MSE**，训练目标就是找到一个线性回归模型，让其RMSE或MSE最小。  
$$MSE(X, h_θ)=1/m\Sigma_{i=1}^m(\theta^TX^i-y^i)^2$$
#### 1. 公式求解损失函数（通过解正态方程直接得到最后的结果）

'''