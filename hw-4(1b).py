import numpy as np
from scipy.linalg import expm

# Skew-symmetric matrix for omega
def skew_symmetric(omega):
    return np.array([[0, -omega[2], omega[1]],
                     [omega[2], 0, -omega[0]],
                     [-omega[1], omega[0], 0]])

# Rodrigues' formula for matrix exponential
def axis_angle_to_rotation_matrix(omega, theta):
    omega_hat = skew_symmetric(omega)
    R = np.eye(3) + np.sin(theta) * omega_hat + (1 - np.cos(theta)) * np.dot(omega_hat, omega_hat)
    return R

# Given omega and theta
omega = np.array([1, 2, 0])  # Axis of rotation
theta = np.sqrt(5)  # Magnitude of rotation (norm of omega)

# Normalize omega
omega_normalized = omega / np.linalg.norm(omega)

# Calculate the rotation matrix using Rodrigues' formula
R = axis_angle_to_rotation_matrix(omega_normalized, theta)

print("Rotation matrix R:")
print(R)
