import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate axis-angle representation
def rotation_matrix_to_axis_angle(R):
    # Calculate theta (rotation angle)
    theta = np.arccos((np.trace(R) - 1) / 2)
    
    # Check if theta is close to 0 or pi to handle special cases
    if np.isclose(theta, 0):
        # No rotation case
        omega = np.array([0, 0, 0])  # No unique axis, any axis would work
    elif np.isclose(theta, np.pi):
        # Special case when theta is pi (180 degrees)
        # Find the eigenvector corresponding to the eigenvalue 1 (the rotation axis)
        eigenvalues, eigenvectors = np.linalg.eig(R)
        omega = eigenvectors[:, np.isclose(eigenvalues, 1)].flatten()
    else:
        # Regular case where sin(theta) is not zero
        omega_hat = (R - R.T) / (2 * np.sin(theta))
        omega = np.array([omega_hat[2, 1], omega_hat[0, 2], omega_hat[1, 0]])
    
    # Normalize omega
    omega = omega / np.linalg.norm(omega)
    
    return omega, theta

# Function to plot the rotation axis
def plot_axis(omega):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the frame axes
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='x_s (Frame s)')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='y_s (Frame s)')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='z_s (Frame s)')

    # Plot the rotation axis (omega)
    ax.quiver(0, 0, 0, omega[0], omega[1], omega[2], color='k', label='Rotation Axis (omega)')

    # Set limits and labels
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show()

# Given rotation matrix R_{S_a}
R = np.array([[0, 0, 1],
              [0, -1, 0],
              [1, 0, 0]])

# Calculate the axis-angle representation
omega, theta = rotation_matrix_to_axis_angle(R)

print("Axis of rotation (omega):", omega)
print("Angle of rotation (theta in degrees):", np.degrees(theta))

# Plot the rotation axis in the {s} frame
plot_axis(omega)

