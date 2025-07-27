# model.py
import torch.nn as nn
import torch.nn.functional as F

class TinyCNN(nn.Module):
    def __init__(self):
        super(TinyCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, 1)
        self.conv2 = nn.Conv2d(16, 32, 3, 1)
        self.fc1 = nn.Linear(5 * 5 * 32, 64)
        self.fc2 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))   # [batch, 16, 26, 26]
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)  # [batch, 32, 12, 12]
        x = x.view(-1, 5 * 5 * 32)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
