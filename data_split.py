# data_split.py
import torch
from torch.utils.data import Subset
import random

def split_data(dataset, num_clients=4):
    data_size = len(dataset)
    indices = list(range(data_size))
    random.shuffle(indices)

    split_size = data_size // num_clients
    client_data = {}

    for i in range(num_clients):
        start_idx = i * split_size
        end_idx = (i + 1) * split_size if i < num_clients - 1 else data_size
        subset_indices = indices[start_idx:end_idx]
        client_data[f'client{i+1}'] = Subset(dataset, subset_indices)

    return client_data
