import os
import ast
import matplotlib.pyplot as plt
import seaborn as sns

# Define the folder path where C++ creates files
folder_path = r"C:\Users\lilha\OneDrive\Pictures\Desktop\SVPCET Practicals\DSA Practical\codes\Practical 3\test"

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"Folder '{folder_path}' not found!")
    exit()

execution_times = []  # List to store execution times
file_names = sorted(os.listdir(folder_path))  # Get sorted file list

# Read each file and extract execution times
for file in file_names:
    file_path = os.path.join(folder_path, file)

    with open(file_path, "r") as f:
        content = f.read().strip()
            
        try:
            times_list = ast.literal_eval(content)  # Convert string to list safely
            execution_times.append(times_list)
        except (SyntaxError, ValueError):
            print(f"Error reading {file_path}")

# Check if any execution times were loaded
if not execution_times:
    print("No valid execution time data found!")
    exit()

# Generate colors for plotting
colors = sns.color_palette("tab10", len(execution_times))

# Plot execution times
plt.figure(figsize=(10, 6))
for idx, times in enumerate(execution_times):
    plt.plot(times, marker='o', linestyle='-', color=colors[idx], label=f"Test {idx+1}")
# Customize the plot
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (ns)")
plt.title("Merge Sort Execution Time for Different Test Cases")
plt.xscale("log")  # Log scale for better visualization
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


