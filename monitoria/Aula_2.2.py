from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.extensions import Initialize
import numpy as np
import matplotlib.pyplot as plt

theta = np.random.uniform(0, np.pi)
phi = np.random.uniform(0, 2*np.pi)

psi = [np.cos(theta/2),np.exp(1j * phi) * np.sin(theta/2)]

plot_bloch_multivector(psi)

qb = 1
qc = QuantumCircuit(qb)
init_gate = Initialize(psi)
qc.append(init_gate, [0])
qc.measure_all()

plt.show()