# utils.py
import torch
from model import TinyCNN

def serialize_model(model):
    return model.state_dict()

def deserialize_model(state_dict):
    model = TinyCNN()
    model.load_state_dict(state_dict)
    return model

def evaluate_model(model, test_loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    accuracy = 100.0 * correct / total
    return accuracy
