import torch

x = torch.ones(2,2,requires_grad=True)
print(x)
out = x.mean()
print(out)
out.backward()
print(x)
print(x.grad)