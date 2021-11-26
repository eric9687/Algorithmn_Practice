import torch

class PowModel(torch.nn.Module):

  def __init__(self):
    super(PowModel, self).__init__()
    self.powParam = torch.nn.Parameter(torch.tensor(1.0))

  def forward(self, x, q):
    return self.powParam * x ** q

class LogModel(torch.nn.Module):

  def __init__(self):
    super(LogModel, self).__init__()
    self.logParam = torch.nn.Parameter(torch.tensor(1.0))

  def forward(self, x):
    return self.logParam * torch.log(x)

class PowLogModel(torch.nn.Module):

  def __init__(self):
    super(PowLogModel, self).__init__()
    self.powModel = PowModel()
    self.logModel = LogModel()

  def forward(self, x, q):
    y = self.powModel(x, q)
    z = self.logModel(y)
    return z

powLogModel = PowLogModel()

def backward_hook(module, grad_input, grad_output):
  print('grad_input', grad_input)
  print('grad_output', grad_output)
  return grad_input

hook = powLogModel.powModel.register_backward_hook(backward_hook)

x = torch.tensor(5.0, requires_grad=True)
q = torch.tensor(3.0, requires_grad=True)
z = powLogModel(x, q)
z.backward()

hook.remove()

print('x', x)
print('x.grad', x.grad)
print('q', q)
print('q.grad', q.grad)
print('z', z)

for name, parameter in powLogModel.named_parameters():
  print(name, f'data({parameter.data}), grad({parameter.grad})')