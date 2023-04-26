from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
import numpy as np
import matplotlib.pyplot as plt

theta = np.random.uniform(0, np.pi)
phi = np.random.uniform(0, 2*np.pi)

psi = [np.cos(theta/2),np.exp(1j * phi) * np.sin(theta/2)]

n_qbits = 1
qc = QuantumCircuit(n_qbits)
qc.ry(theta,0)
qc.rz(phi,0)


plot_bloch_multivector(qc)
plot_bloch_multivector(psi)
plt.show()