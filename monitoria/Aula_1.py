# =================== Bibliotecas ==================== #
import numpy as np
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
from qiskit.extensions import Initialize
# ====================== Tarefa 2 ==================== #


psi = [np.random.rand(), np.random.rand()]
norma = np.linalg.norm(psi)
psi = psi/norma

print(psi)
plot_bloch_multivector(psi)


# ======================= Tarefa 2 ==================== #

# theta = np.random.uniform(0, np.pi)
# phi = np.random.uniform(0, 2*np.pi)

# psi = [np.cos(theta/2), np.exp(1j * phi) * np.sin(theta/2)]
# plot_bloch_multivector(psi)


# ===================================================== #

# qb = 3
# cb = 3

# qc = QuantumCircuit(qb, cb)
# qc.h(0)
# qc.y(2)
# qc.barrier()
# qc.z(0)
# qc.h(1)
# qc.h(2)
# qc.barrier()

# back_sv = Aer.get_backend('statevector_simulator')  
# result_sv = execute(qc, back_sv).result()           
# qc_sv = result_sv.get_statevector(qc)               
# plot_bloch_multivector(qc_sv)  

# qc.measure([0,1,2], [0,1,2])
qc = QuantumCircuit(1,1)
init_gate = Initialize(psi)
init_gate.label = f'Estado inicial'
qc.append(init_gate, [0])
qc.measure(0,0)
qc.draw('mpl')

qasm_sim = Aer.get_backend('qasm_simulator')  
job = execute(qc, backend=qasm_sim, shots=10000)

result_sim = job.result()
counts = result_sim.get_counts(qc)
plot_histogram(counts)
plt.show()

