from qiskit import QuantumCircuit, BasicAer, execute, Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

def quantum_coin_flipping():
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)

    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1).result()
    count = job.data(qc)
    if count['counts'].get('0x0') == True:
        return True
    else:
        return False

qc = QuantumCircuit(1)                              # build a circuit with the one qubit
if quantum_coin_flipping():                         # if the random number is greater than 0.5, append the hadamard gate in the circuit
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
