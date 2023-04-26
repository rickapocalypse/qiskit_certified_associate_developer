from qiskit import QuantumCircuit
from qiskit.extensions import Initialize
from qiskit.visualization import plot_bloch_multivector
import numpy as np
import matplotlib.pyplot as plt

# build a random state vector

theta = np.random.uniform(0, np.pi)
phi = np.random.uniform(0, 2*np.pi)
psi = [np.cos(theta/2),np.exp(1j * phi) * np.sin(theta/2)]

# build a quantum circuit
qb = 6
qc = QuantumCircuit(qb)
init_gate = Initialize(psi)
for n in range(0,qb):
    qc.append(init_gate, [n])
    qc.rz((n+1) * np.pi / 6, n)

plot_bloch_multivector(qc)
plt.show()