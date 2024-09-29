import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# Function to calculate the skew-symmetric matrix
def skew_symmetric(omega):
    return np.array([[0, -omega[2], omega[1]],
                     [omega[2], 0, -omega[0]],
                     [-omega[1], omega[0], 0]])

# Rodrigues' formula for calculating the matrix exponential
def axis_angle_to_rotation_matrix(omega, theta):
    omega_hat = skew_symmetric(omega)
    R = np.eye(3) + np.sin(theta) * omega_hat + (1 - np.cos(theta)) * np.dot(omega_hat, omega_hat)
    return R

# Function to plot the frame and rotation axis
def plot_frame_and_axis(R, omega):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the original frame axes
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='x_s (Original)')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='y_s (Original)')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='z_s (Original)')

    # Plot the rotated frame
    ax.quiver(0, 0, 0, R[0, 0], R[1, 0], R[2, 0], color='r', linestyle='dashed', label='x_s (Rotated)')
    ax.quiver(0, 0, 0, R[0, 1], R[1, 1], R[2, 1], color='g', linestyle='dashed', label='y_s (Rotated)')
    ax.quiver(0, 0, 0, R[0, 2], R[1, 2], R[2, 2], color='b', linestyle='dashed', label='z_s (Rotated)')

    # Plot the rotation axis
    ax.quiver(0, 0, 0, omega[0], omega[1], omega[2], color='k', label='Rotation Axis (omega)')

    # Set plot limits and labels
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Adjust legend position to the side
    ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), borderaxespad=0)

    plt.show()

# Given omega and theta
omega = np.array([1, 2, 0])  # Axis of rotation
theta = np.linalg.norm(omega)  # Magnitude of rotation

# Normalize omega
omega_normalized = omega / np.linalg.norm(omega)

# Calculate the rotation matrix using Rodrigues' formula
R = axis_angle_to_rotation_matrix(omega_normalized, theta)

# Print the calculated rotation matrix
print("Rotation matrix R:")
print(R)

# Plot the rotated frame and rotation axis with the legend on the side
plot_frame_and_axis(R, omega_normalized)
