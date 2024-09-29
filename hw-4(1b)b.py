import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot the axes
def plot_frame(R, omega):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Original frame (identity matrix)
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='x-axis (original)')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='y-axis (original)')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='z-axis (original)')

    # Rotated frame
    ax.quiver(0, 0, 0, R[0, 0], R[1, 0], R[2, 0], color='r', linestyle='dashed', label='x-axis (rotated)')
    ax.quiver(0, 0, 0, R[0, 1], R[1, 1], R[2, 1], color='g', linestyle='dashed', label='y-axis (rotated)')
    ax.quiver(0, 0, 0, R[0, 2], R[1, 2], R[2, 2], color='b', linestyle='dashed', label='z-axis (rotated)')

    # Plot the axis of rotation
    ax.quiver(0, 0, 0, omega[0], omega[1], omega[2], color='k', label='Rotation Axis (omega)')
    
    # Set labels and limits
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show()

# Plot the frame and rotation axis
plot_frame(R, omega_normalized)
