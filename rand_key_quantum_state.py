import numpy as np
from qiskit import QuantumCircuit, BasicAer, execute

qc = QuantumCircuit(1)
if np.random.rand() >= 0.5:
    qc.h(0)

else:
    qc.x(0)
    qc.h(0)

back_sv = BasicAer.get_backend('statevector_simulator')
result = execute(qc, back_sv).result()
qc_sv = result.get_statevector(qc)
print(qc_sv)

# verify the key quantum state

if qc_sv[1] > 0:
    print(f'|+> = {qc_sv}')
else:
    print(f'|-> = {qc_sv}')
