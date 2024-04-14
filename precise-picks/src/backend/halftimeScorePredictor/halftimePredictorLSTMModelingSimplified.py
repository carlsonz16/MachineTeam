import torch
import torch.nn as nn
from torch.nn.utils.rnn import pad_sequence
import torch.optim as optim
#from halftimePredictorDataPrep import get_pbp_data
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import os

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
    def __init__(self, sequences, labels, padding_value=0):
        self.sequences = [torch.tensor(s, dtype=torch.float32) for s in sequences]
        self.labels = [torch.tensor(l, dtype=torch.float32) for l in labels]
        self.padding_value = padding_value

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.sequences[idx], self.labels[idx]

    def collate_fn(self, batch):
        sequences, labels = zip(*batch)
        sequences_padded = pad_sequence(sequences, batch_first=True, padding_value=self.padding_value)
        labels = torch.stack(labels)
        return sequences_padded, labels

if __name__ == "__main__":
   device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
   print("Using device:", device)
   print(torch.version.cuda)
   print("PyTorch version:", torch.__version__)
   print(torch.cuda.is_available())

# Initialize the list for storing dataframes
   pbp_training_data = []
   score_results = None

   # Specify the path to the directory containing CSV files
   directory_path = r'C:\Users\jdbas\Documents\code\precise-picks\excelPBPDataMinMaxSimplified'

   # Loop through all files in the directory
   for filename in os.listdir(directory_path):
      # Check if the current file is a CSV file
      if filename.endswith('.csv'):
         # Construct the full path to the file
         file_path = os.path.join(directory_path, filename)
         
         # Check if the current file is 'score_results.csv'
         if filename == 'score_results.csv':
               # Read the CSV file into a DataFrame and assign it to score_results
               score_results = pd.read_csv(file_path)
         else:
               # Read the specified columns of the CSV file into a DataFrame and append it to the list
               df = pd.read_csv(file_path, usecols=['scoreHome', 'scoreAway', 'timeUntilEnd'])
               pbp_training_data.append(df)

   score_results_processed = False

   score_results_file_path = os.path.join(directory_path, 'score_results.csv')
   if os.path.exists(score_results_file_path):
      score_results = pd.read_csv(score_results_file_path)
      score_results_processed = True

   # Example of converting your data into a suitable format
   sequences = [df.to_numpy() for df in pbp_training_data]
   labels = score_results.to_numpy()  # Make sure this is in the correct format

   dataset = SequenceDataset(sequences, labels)
   dataloader = DataLoader(dataset, batch_size=500, shuffle=True, collate_fn=dataset.collate_fn)

   # Initialize the model
   input_dim = pbp_training_data[0].shape[1]  # Number of features per event
   hidden_dim = 200  # Or any number you deem appropriate
   output_dim = 2  # Assuming score_results has 2 output features
   num_layers = 3  # Number of LSTM layers

   model = LSTMModel(input_dim, hidden_dim, output_dim, num_layers).to(device)

   # Define loss function and optimizer
   criterion = nn.MSELoss()  # For regression tasks
   optimizer = optim.Adam(model.parameters(), lr=0.001)

   # Train the model
   num_epochs = 500  # Or any number you find suitable
   for epoch in range(num_epochs):
      for sequences, labels in dataloader:
         sequences, labels = sequences.to(device), labels.to(device)
         optimizer.zero_grad()
         outputs = model(sequences)
         loss = criterion(outputs, labels)
         loss.backward()
         optimizer.step()
      print(f'Epoch {epoch+1}, Loss: {loss.item()}')
      
   print('Training Done!')
   torch.save(model.state_dict(), '200hid-3layer-500ranbatch-simplified2.pth')
