# client4.py
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from model import TinyCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([transforms.ToTensor()])
trainset = datasets.MNIST('./data', train=True, download=True, transform=transform)
client_data = torch.utils.data.Subset(trainset, list(range(45000, 60000)))  # Client 4 split

train_loader = torch.utils.data.DataLoader(client_data, batch_size=64, shuffle=True)

model = TinyCNN().to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

model.train()
for epoch in range(1):
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

print("[Client 4] Training complete. Model updated.")
