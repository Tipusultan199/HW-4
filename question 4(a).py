from sympy import symbols, cos, sin, Matrix
alpha_rpy, beta_rpy, gamma_rpy = symbols('alpha_rpy beta_rpy gamma_rpy')

Rx = Matrix([[1, 0, 0], [0, cos(gamma_rpy), -sin(gamma_rpy)], [0, sin(gamma_rpy), cos(gamma_rpy)]])
Ry = Matrix([[cos(beta_rpy), 0, sin(beta_rpy)], [0, 1, 0], [-sin(beta_rpy), 0, cos(beta_rpy)]])
Rz = Matrix([[cos(alpha_rpy), -sin(alpha_rpy), 0], [sin(alpha_rpy), cos(alpha_rpy), 0], [0, 0, 1]])

R_rpy = Rz * Ry * Rx
