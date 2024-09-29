import numpy as np

def rotation_matrix_to_axis_angle(R):
    # Calculate theta
    theta = np.arccos((np.trace(R) - 1) / 2)
    
    # Calculate the skew-symmetric matrix [omega_hat]
    omega_hat = (R - R.T) / (2 * np.sin(theta))
    
    # Extract the axis of rotation from omega_hat
    omega = np.array([omega_hat[2, 1], omega_hat[0, 2], omega_hat[1, 0]])
    
    return omega, theta

# Given rotation matrix R_{S_a}
R = np.array([[0, -1, 0],
              [0,  0, -1],
              [1,  0,  0]])

# Compute axis and angle
omega, theta = rotation_matrix_to_axis_angle(R)

print("Axis of rotation (omega):", omega)
print("Angle of rotation (theta in degrees):", np.degrees(theta))
