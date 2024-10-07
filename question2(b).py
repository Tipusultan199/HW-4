import numpy as np

# Given parameters
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 1])
omega_hat = np.array([2/3, 2/3, 1/3])

# Skew-symmetric matrix for omega_hat
omega_hat_skew = np.array([[0, -omega_hat[2], omega_hat[1]],
                           [omega_hat[2], 0, -omega_hat[0]],
                           [-omega_hat[1], omega_hat[0], 0]])

# Rodrigues' rotation formula
def rotation_matrix(theta):
    I = np.identity(3)
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    return I + sin_theta * omega_hat_skew + (1 - cos_theta) * np.dot(omega_hat_skew, omega_hat_skew)

# Increase the resolution and tolerance
thetas = np.linspace(-2*np.pi, 2*np.pi, 1000)  # finer resolution and wider range of theta
tolerance = 1e-1  # relaxed tolerance

# Finding the angle theta
matching_theta = None
for theta in thetas:
    v_rotated = np.dot(rotation_matrix(theta), v1)
    if np.allclose(v_rotated, v2, atol=tolerance):  # relaxed tolerance
        matching_theta = theta
        break

if matching_theta is not None:
    print(f"The matching theta is approximately: {matching_theta} radians")
else:
    print("No matching theta found.")
