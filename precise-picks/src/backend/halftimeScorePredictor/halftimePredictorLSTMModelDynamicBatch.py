import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import os
import numpy as np
from dataLengthReporter import get_dataset_grouped  # Assuming this is a function you've defined elsewhere

directory_path = r"C:\Users\jdbas\Documents\code\precise-picks\excelPBPDataMinMaxSimplified"

class LSTMModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers):
        super(LSTMModel, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        
        # Define the LSTM layer
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        
        # Define the output layer
        self.linear = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        
        # Forward propagate the LSTM
        out, _ = self.lstm(x, (h0, c0))
        
        # Decode the hidden state of the last time step
        out = self.linear(out[:, -1, :])
        return out

class SequenceDataset(Dataset):
    def __init__(self, sequences, labels):
        self.sequences = sequences
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        sequence = torch.tensor(self.sequences[idx], dtype=torch.float32)
        label = torch.tensor(self.labels[idx], dtype=torch.float32)
        return sequence, label

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)

    # Initialize the model with common parameters
    hidden_dim = 200
    num_layers = 3
    output_dim = 2  # For simplicity, assuming score_results has 2 output features
    num_epochs = 1000

    # Assume a consistent input_dim based on your dataset's feature size
    input_dim = 229  # Set this based on your actual dataset
    model = LSTMModel(input_dim=input_dim, hidden_dim=hidden_dim, output_dim=output_dim, num_layers=num_layers).to(device)
    
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    dimensions_group = get_dataset_grouped(directory_path)

    for dimension, group in dimensions_group.items():
      dataframes, labels_tuples = group['dataframes'], group['labels']
      print(f"Processing dimension: {dimension}")

      sequences = [df.to_numpy(dtype=np.float32) for df in dataframes]
      labels = torch.tensor(labels_tuples, dtype=torch.float32)
      
      # Use the length of labels_tuples or dataframes as batch size
      batch_size = len(labels_tuples)

      dataset = SequenceDataset(sequences, labels)
      dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

      # Train the model with this dimension's data
      for epoch in range(num_epochs):
         for sequences, labels in dataloader:
               sequences, labels = sequences.to(device), labels.to(device)
               optimizer.zero_grad()
               outputs = model(sequences)
               loss = criterion(outputs, labels)
               loss.backward()
               optimizer.step()
         print(f'Dimension {dimension} - Epoch {epoch+1}, Loss: {loss.item()}')

    # Save the model after training on all dimensions
    torch.save(model.state_dict(), '200hid-3layer.pth')
    print('Training completed and model saved as 200hid-3layer.pth.')

