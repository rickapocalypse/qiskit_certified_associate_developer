import numpy as np
from qiskit import QuantumCircuit, BasicAer, execute
from qiskit.circuit.library import YGate
from qiskit.quantum_info import Operator, average_gate_fidelity, process_fidelity, state_fidelity

# Average between two gates

op_a = Operator(YGate())

op_b = np.exp(1j / 2) * op_a

print(average_gate_fidelity(op_a, op_b))

# the case of unitary operators, it does not depend on global phase.

# Average between two gates using the process fidelity

print(process_fidelity(op_a, op_b))

