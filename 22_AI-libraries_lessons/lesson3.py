import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# =====================================
# 1. PREPARE DATA
# =====================================

# Sample training data
X = torch.tensor([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [4.0, 5.0],
    [5.0, 6.0],
    [6.0, 7.0]
])

# Labels: 0 or 1
y = torch.tensor([0, 0, 0, 1, 1, 1])

# =====================================
# 2. DATASET AND DATALOADER
# =====================================

dataset = TensorDataset(X, y)

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

# =====================================
# 3. BUILD NEURAL NETWORK
# =====================================

class MyModel(nn.Module):

    def __init__(self):

        super().__init__()

        # Input layer -> Hidden layer
        self.layer1 = nn.Linear(2, 8)

        # Activation function
        self.relu = nn.ReLU()

        # Hidden layer -> Output layer
        self.layer2 = nn.Linear(8, 2)

    def forward(self, x):

        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)

        return x


# Create model
model = MyModel()

print(model)

# =====================================
# 4. LOSS FUNCTION
# =====================================

# CrossEntropyLoss for classification
criterion = nn.CrossEntropyLoss()

# =====================================
# 5. OPTIMIZER
# =====================================

# Adam updates model weights
optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)

# =====================================
# 6. TRAINING LOOP
# =====================================

epochs = 100

for epoch in range(epochs):

    total_loss = 0

    for inputs, labels in loader:

        # Reset gradients
        optimizer.zero_grad()

        # Forward propagation
        outputs = model(inputs)

        # Calculate loss
        loss = criterion(outputs, labels)

        # Backpropagation
        loss.backward()

        # Update weights
        optimizer.step()

        total_loss += loss.item()

    if (epoch + 1) % 10 == 0:
        print(
            f"Epoch {epoch+1}, "
            f"Loss: {total_loss / len(loader):.4f}"
        )

# =====================================
# 7. MODEL EVALUATION
# =====================================

model.eval()

with torch.no_grad():

    outputs = model(X)

    # Select class with highest score
    predictions = torch.argmax(outputs, dim=1)

    accuracy = (predictions == y).float().mean()

    print("Predictions:", predictions)
    print("Actual:", y)
    print("Accuracy:", accuracy.item())

# =====================================
# 8. SAVE MODEL
# =====================================

torch.save(model.state_dict(), "model.pth")

print("Model saved!")

# =====================================
# 9. LOAD MODEL
# =====================================

new_model = MyModel()

new_model.load_state_dict(
    torch.load("model.pth", weights_only=True)
)

new_model.eval()

print("Model loaded!")

# =====================================
# 10. MAKE NEW PREDICTION
# =====================================

new_data = torch.tensor([[2.5, 3.5]])

with torch.no_grad():

    result = new_model(new_data)

    prediction = torch.argmax(result, dim=1)

    print("New Prediction:", prediction.item())

print("TRAINING COMPLETED!")
