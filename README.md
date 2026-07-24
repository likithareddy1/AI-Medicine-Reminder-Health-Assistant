## ⚡ AMD ROCm Compute Support

This project was developed and tested using AMD GPU acceleration.

Hardware:
- GPU: AMD Radeon 890M
- PyTorch Version: 2.9.1+rocm6.3
- ROCm Support: Enabled

Verification:

```python
import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

Output:
2.9.1+rocm6.3
True
AMD Radeon 890M