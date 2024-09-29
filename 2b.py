import numpy as np
from scipy.optimize import fsolve

# Function to calculate the skew-symmetric matrix of omega
def skew_symmetric(omega):
    return np.array([[0, -omega[2], omega[1]],
                     [omega[2], 0, -omega[0]],
                     [-omega[1], omega[0], 0]])

# Rodrigues' formula for the rotation matrix
def rotation_matrix(omega, theta):
    omega_hat = skew_symmetric(omega)
    R = np.eye(3) + np.sin(theta) * omega_hat + (1 - np.cos(theta)) * np.dot(omega_hat, omega_hat)
    return R

# Define the vectors and axis
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 1])
omega = np.array([2/3, 2/3, 1/3])

# Function to solve for theta
def equation(theta):
    R = rotation_matrix(omega, theta)
    v2_computed = np.dot(R, v1)
    return np.linalg.norm(v2_computed - v2)

# Solve for theta using an initial guess
theta_solution = fsolve(equation, np.pi / 4)

# Display the results
print("Theta (in radians):", theta_solution)
print("Theta (in degrees):", np.degrees(theta_solution))

# Now apply the found theta to check v2
theta = theta_solution[0]  # Using the solution found
R = rotation_matrix(omega, theta)  # Compute the rotation matrix with the found theta
v2_computed = np.dot(R, v1)  # Compute the rotated vector

# Display the computed v2
print("Computed v2 after rotation:", v2_computed)

