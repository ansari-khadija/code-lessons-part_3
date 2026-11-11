# Topic: Autograd, Gradients and Backpropagation
import torch
import torch.nn 

print("========== 1. AUTOGRAD ==========")

# requires_grad=True enables gradient tracking
x = torch.tensor(5.0, requires_grad=True)

# Mathematical operation
y = x ** 2

# Calculate gradient
y.backward()

print("Value:", y.item())
print("Gradient:", x.grad)


print("\n========== 2. COMPUTATIONAL GRAPH ==========")

a = torch.tensor(3.0, requires_grad=True)

b = a * 2
c = b ** 2

print("Result:", c)
print("Grad Function:", c.grad_fn)

c.backward()

print("Gradient:", a.grad)


print("\n========== 3. MULTIPLE VARIABLES ==========")

x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

z = x**2 + y**2

z.backward()

print("Gradient X:", x.grad)
print("Gradient Y:", y.grad)


print("\n========== 4. GRADIENT ZEROING ==========")

x = torch.tensor(2.0, requires_grad=True)

y = x**2
y.backward()

print("First Gradient:", x.grad)

# Clear existing gradients
x.grad.zero_()

print("After Zeroing:", x.grad)


print("\n========== 5. NO GRAD ==========")

x = torch.tensor(5.0, requires_grad=True)

# Disable gradient tracking temporarily
with torch.no_grad():
    y = x**2

print("Requires Grad:", y.requires_grad)


print("\n========== 6. DETACH ==========")

x = torch.tensor(5.0, requires_grad=True)

y = x**2

# Disconnect from computational graph
z = y.detach()

print("Original:", y)
print("Detached:", z)
print("Detached Requires Grad:", z.requires_grad)


print("\n========== 7. GRADIENT DESCENT ==========")

# We want to find the minimum of f(x) = x²

x = torch.tensor(10.0, requires_grad=True)

learning_rate = 0.1

for epoch in range(10):

    # Forward pass
    loss = x**2

    # Calculate gradient
    loss.backward()

    # Update x without tracking this operation
    with torch.no_grad():
        x -= learning_rate * x.grad

    # Clear gradient for next iteration
    x.grad.zero_()

    print("Epoch:", epoch + 1,
          "Loss:", loss.item(),
          "X:", x.item())


print("\n========== 8. OPTIMIZERS ==========")

# Create a trainable parameter
weight = torch.nn.Parameter(torch.tensor(10.0))

# Adam optimizer
optimizer = torch.optim.Adam([weight], lr=0.1)

for epoch in range(10):

    optimizer.zero_grad()

    loss = weight**2

    loss.backward()

    optimizer.step()

    print("Epoch:", epoch + 1,
          "Weight:", weight.item(),
          "Loss:", loss.item())


print("\n========== 9. CUDA ==========")

# Select GPU if available, otherwise CPU
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

x = torch.tensor([1.0, 2.0, 3.0]).to(device)

print("Device:", x.device)
print("Tensor:", x)


print("\n========== LESSON COMPLETED ==========")
