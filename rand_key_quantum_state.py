import numpy as np
from qiskit import QuantumCircuit, BasicAer, execute, Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt


qc = QuantumCircuit(1)                              # build a circuit with the one qubit
if np.random.rand() >= 0.5:                         # if the random number is greater than 0.5, append the hadamard gate in the circuit
    qc.h(0)                                         # build a |+> 

else:                                               # if the random number is not greater than 0.5
    qc.x(0)
    qc.h(0)                                         # build a |-> 

back_sv = Aer.get_backend('statevector_simulator')  # backend simulator for generator the statevector
result_sv = execute(qc, back_sv).result()           # to execute the statevector of circuit "qc"
qc_sv = result_sv.get_statevector(qc)               # stores the state vector
plot_bloch_multivector(qc_sv)                       # plot bloch sphere for visualization of the random state
plt.show()                                          # prints the state vector

# verify the key quantum state

if qc_sv[1] > 0:
    print(f'|+> = [{float(qc_sv[0])}, {float(qc_sv[1])}]')
else:
    print(f'|-> = [{float(qc_sv[0])}, {float(qc_sv[1])}]')
