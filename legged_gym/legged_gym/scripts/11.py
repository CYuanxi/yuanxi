import torch
print(torch.__version__)
print(torch.version.cuda)
 
# 查看编译时包含的算力架构
from torch.utils.cpp_extension import CUDA_HOME
print("CUDA_HOME:", CUDA_HOME)
 
# 这个函数能看到 torch 是否支持 sm_120
print("编译的 GPU 架构支持:", torch._C._cuda_getArchFlags())
