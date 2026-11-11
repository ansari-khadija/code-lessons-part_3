# Topic: Tensors and Tensor Operations

import torch
import numpy as np

print("\n========== 1. PYTORCH INFORMATION ==========")

# Check PyTorch version
print("PyTorch Version:", torch.__version__)

# Check whether GPU (CUDA) is available
print("CUDA Available:", torch.cuda.is_available())

print("\n========== 2. CREATING TENSORS ==========")

# Create a tensor from a Python list
x = torch.tensor([1, 2, 3, 4, 5])
print("Basic Tensor:", x)

# Create a tensor containing only zeros
zeros = torch.zeros(3, 3)
print("Zeros:\n", zeros)

# Create a tensor containing only ones
ones = torch.ones(2, 3)
print("Ones:\n", ones)

# Create a tensor filled with a specific value
full = torch.full((2, 3), 7)
print("Full:\n", full)

# Create an identity matrix
identity = torch.eye(3)
print("Identity Matrix:\n", identity)

# Create random values between 0 and 1
random_tensor = torch.rand(3, 3)
print("Random:\n", random_tensor)

# Create random values from a standard normal distribution
normal_tensor = torch.randn(3, 3)
print("Normal Distribution:\n", normal_tensor)

# Create numbers from start to end-1
arange_tensor = torch.arange(1, 11)
print("Arange:", arange_tensor)

# Create evenly spaced values between two endpoints
linspace_tensor = torch.linspace(0, 10, 5)
print("Linspace:", linspace_tensor)

# Create a tensor with the same shape as another tensor
same = torch.zeros_like(random_tensor)
print("Zeros Like:\n", same)

print("\n========== 3. TENSOR PROPERTIES ==========")

matrix = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

# Shape: size of each dimension
print("Shape:", matrix.shape)

# Number of dimensions
print("Dimensions:", matrix.ndim)

# Data type
print("Data Type:", matrix.dtype)

# Total number of elements
print("Total Elements:", matrix.numel())

# Size (similar to shape)
print("Size:", matrix.size())

# Memory device
print("Device:", matrix.device)

print("\n========== 4. DATA TYPES ==========")

x = torch.tensor([1, 2, 3])

# Convert integer tensor into float
float_tensor = x.float()
print("Float:", float_tensor)

# Convert into double precision
double_tensor = x.double()
print("Double:", double_tensor)

# Convert into integer
int_tensor = float_tensor.int()
print("Integer:", int_tensor)

# Convert using to()
converted = x.to(dtype=torch.float32)
print("Converted:", converted)

print("\n========== 5. RESHAPING ==========")

x = torch.arange(12)

# Reshape into 3 rows and 4 columns
reshaped = x.reshape(3, 4)
print("Reshape:\n", reshaped)

# View tensor with another shape (when strides permit)
viewed = x.view(2, 6)
print("View:\n", viewed)

# Flatten: Convert into one dimension
flattened = reshaped.flatten()
print("Flatten:", flattened)

# Squeeze: Remove dimensions of size 1
a = torch.rand(1, 3, 1, 4)
print("Before Squeeze:", a.shape)
print("After Squeeze:", a.squeeze().shape)

# Unsqueeze: Add a dimension
b = torch.tensor([1, 2, 3])
print("Unsqueeze:", b.unsqueeze(0).shape)

# Transpose: Swap two dimensions
print("Transpose:\n", reshaped.T)

print("\n========== 6. INDEXING AND SLICING ==========")

x = torch.tensor([10, 20, 30, 40, 50])

# Access first element
print("First:", x[0])

# Access last element
print("Last:", x[-1])

# Get elements from index 1 to 3
print("Slice:", x[1:4])

# Matrix indexing
matrix = torch.tensor([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# First row
print("First Row:", matrix[0])

# Second column
print("Second Column:", matrix[:, 1])

# Specific element
print("Specific Element:", matrix[1, 2])

# Boolean masking
print("Values greater than 5:", matrix[matrix > 5])

print("\n========== 7. MATHEMATICAL OPERATIONS ==========")

a = torch.tensor([10.0, 20.0, 30.0])
b = torch.tensor([1.0, 2.0, 3.0])

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Element-wise multiplication
print("Multiplication:", a * b)

# Element-wise division
print("Division:", a / b)

# Power
print("Power:", a ** 2)

# Sum
print("Sum:", torch.sum(a))

# Mean
print("Mean:", torch.mean(a))

# Maximum
print("Maximum:", torch.max(a))

# Minimum
print("Minimum:", torch.min(a))

# Index of maximum value
print("Argmax:", torch.argmax(a))

# Index of minimum value
print("Argmin:", torch.argmin(a))

# Square root
print("Square Root:", torch.sqrt(a))

# Absolute value
print("Absolute:", torch.abs(torch.tensor([-1., -2., 3.])))

# Exponential
print("Exponential:", torch.exp(a))

# Natural logarithm
print("Log:", torch.log(a))

print("\n========== 8. MATRIX MULTIPLICATION ==========")

a = torch.tensor([
    [1, 2],
    [3, 4]
])

b = torch.tensor([
    [5, 6],
    [7, 8]
])

# Element-wise multiplication
print("Element-wise:\n", a * b)

# Matrix multiplication
print("Matmul:\n", torch.matmul(a, b))

# Alternative matrix multiplication
print("MM:\n", torch.mm(a, b))

# @ operator
print("Using @:\n", a @ b)

print("\n========== 9. COMBINING TENSORS ==========")

a = torch.tensor([1, 2])
b = torch.tensor([3, 4])

# Concatenate: Join along an existing dimension
print("Cat:", torch.cat((a, b)))

# Stack: Join using a new dimension
print("Stack:\n", torch.stack((a, b)))

# Split into chunks of size 2
x = torch.arange(8)
print("Split:", torch.split(x, 2))

# Chunk into 4 sections
print("Chunk:", torch.chunk(x, 4))

print("\n========== 10. COMPARISON ==========")

a = torch.tensor([10, 20, 30, 40])

# Greater than
print("Greater:", a > 20)

# Less than
print("Less:", a < 30)

# Equal to
print("Equal:", a == 20)

# Check whether all values satisfy condition
print("All:", torch.all(a > 5))

# Check whether any value satisfies condition
print("Any:", torch.any(a > 30))

print("\n========== 11. NUMPY CONVERSION ==========")

# NumPy array to PyTorch tensor
numpy_array = np.array([1, 2, 3, 4])

tensor = torch.from_numpy(numpy_array)

print("From NumPy:", tensor)

# PyTorch tensor to NumPy array
tensor = torch.tensor([10, 20, 30])

numpy_result = tensor.numpy()

print("To NumPy:", numpy_result)

# NOTE:
# CPU tensors with compatible data types can share memory
# with NumPy arrays when using from_numpy() and numpy().

print("\n========== 12. GPU AND CPU ==========")

# Check CUDA availability
if torch.cuda.is_available():

    device = torch.device("cuda")

    print("GPU Available:", torch.cuda.get_device_name(0))

else:

    device = torch.device("cpu")

    print("GPU Not Available. Using CPU.")

# Move tensor to selected device
x = torch.tensor([1, 2, 3])

x = x.to(device)

print("Tensor Device:", x.device)

# Move tensor back to CPU
x_cpu = x.cpu()

print("CPU Tensor:", x_cpu)

print("\n========== 13. RANDOM SEED ==========")

# Set seed for reproducible random values
torch.manual_seed(42)

x = torch.rand(3, 3)

print("Random Tensor with Seed:\n", x)

print("\n========== 14. USEFUL FUNCTIONS ==========")

x = torch.tensor([1.0, 2.0, 3.0])

# Clone: Create an independent copy
y = x.clone()

# Detach: Create a tensor disconnected from autograd
z = x.detach()

print("Clone:", y)
print("Detach:", z)

# Check if tensor contains any NaN values
nan_tensor = torch.tensor([1.0, float("nan"), 3.0])
print("Is NaN:", torch.isnan(nan_tensor))

# Check if values are finite
print("Is Finite:", torch.isfinite(nan_tensor))

# Replace values using clamp
values = torch.tensor([-10.0, 5.0, 100.0])
print("Clamp:", torch.clamp(values, min=0, max=50))

print("\n========== PYTORCH TENSOR LESSON COMPLETED ==========")
