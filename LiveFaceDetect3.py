import matplotlib.pyplot as plt

# Accuracy ranges for different motion detection methods
methods = ["Background Subtraction", "Frame Differencing", "Optical Flow", "LSTM Networks", "3D CNNs", "Haar Cascade (OpenCV)"]
accuracy_ranges = [(80, 90), (70, 85), (85, 95), (90, 97), (92, 98), (85, 98)]  # Haar Cascade accuracy range is assumed similar to Background Subtraction

# Extract lower and upper bounds of accuracy ranges
lower_accuracy = [accuracy[0] for accuracy in accuracy_ranges]
upper_accuracy = [accuracy[1] for accuracy in accuracy_ranges]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(methods, lower_accuracy, width=0.4, label="Lower Bound", align='center')
plt.bar(methods, upper_accuracy, width=0.4, label="Upper Bound", align='edge')
plt.xlabel("Motion Detection Method")
plt.ylabel("Accuracy (%)")
plt.title("Comparison of Motion Detection Accuracy")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the graph
plt.tight_layout()
plt.show()