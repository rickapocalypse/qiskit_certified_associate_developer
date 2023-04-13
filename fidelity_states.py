import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, BasicAer, execute
from qiskit.circuit.library import YGate
from qiskit.quantum_info import Operator, average_gate_fidelity, process_fidelity, state_fidelity

n = 1/np.sqrt(3)
desired_state = [n,np.sqrt(1-n**2)]

qc = QuantumCircuit(1)
qc.initialize(desired_state, 0) # initialize the circuit with the desired state in the first wire 
qc.draw('mpl')
plt.show()

back_sv = BasicAer.get_backend('statevector_simulator')
result = execute(qc, back_sv).result()
qc_sv = result.get_statevector(qc)



print(state_fidelity(desired_state, qc_sv))
