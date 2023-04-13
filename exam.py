# General tools
import numpy as np
import matplotlib.pyplot as plt
import math
# Importing standard Qiskit libraries
from qiskit import execute,QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, transpiler
from qiskit_ibm_provider import IBMProvider
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.quantum_info import Operator, average_gate_fidelity, process_fidelity, state_fidelity
from qiskit.circuit.library import XGate

# # Loading your IBM Quantum account(s)
# provider = IBMProvider()

# # given this code, what de probabilities that measurement the result in /0> ?
# qc = QuantumCircuit(1)
# qc.ry(3 * math.pi/4, 0)

# #measurement the result
# qc.measure_all()
# qasm_simulator = Aer.get_backend('qasm_simulator')
# result = execute(qc, qasm_simulator).result()
# counts = result.get_counts() #count the number of measurements in state /0> and /1>
# plot_histogram(counts)
# plt.show()

# Assuming the fragment below, which three code fragments would produce the circuit illustrated?

# inp_reg = QuantumRegister(2, name='inp')
# ancilla = QuantumRegister(1, name='anc')
# qc = QuantumCircuit(inp_reg, ancilla)

# qc.h(inp_reg[0:2])
# qc.x(ancilla[0])
# qc.draw('mpl')
# plt.show()

# Given an empty QuantumCircuit object, qc, with three qubits and three classical bits, which one of these code fragments would create this circuit?

# qc = QuantumCircuit(3,3)
# qc.measure([0,1,2], [0,1,2])
# qc.draw('mpl')
# plt.show()

# Which code fragment will produce a maximally entangled, or Bell, state?

# bell = QuantumCircuit(2)
# bell.h(0)
# bell.x(1)
# bell.cx(0, 1)
# bell.draw('mpl')
# plt.show()

# Given this code, which two inserted code fragments result in the state vector represented by this Bloch sphere?

# qc = QuantumCircuit(1)
# qc.ry(math.pi / 2,0)
# simulator = Aer.get_backend('statevector_simulator')
# job = execute(qc, simulator)
# result = job.result()
# outputstate = result.get_statevector(qc)
# plot_bloch_multivector(outputstate)
# plt.show()

# S-gate is a Qiskit phase gate with what value of the phase parameter?
# qc = QuantumCircuit(2)
# qc.s(1)
# qc.draw('mpl')
# simulator = Aer.get_backend('statevector_simulator')
# job = execute(qc, simulator)
# result = job.result()
# outputstate = simulator.run(qc).result().get_statevector()
# plot_bloch_multivector(outputstate)
# plt.show()

# Which two code fragments, when inserted into the code below, will produce the statevector shown in the output?
# qc = QuantumCircuit(2)
# v = [1/math.sqrt(2), 0, 0, 1/math.sqrt(2)]
# qc.initialize(v,[0,1])

# simulator = Aer.get_backend('statevector_simulator')
# result = execute(qc, simulator).result()
# statevector = result.get_statevector()
# print(statevector)

# Which two options would place a barrier across all qubits to the QuantumCircuit below?

# qc.barrier()
# qc.barrier([0,1,2])

# .What code fragment codes the equivalent circuit if you remove the barrier in the following QuantumCircuit?

# qc =QuantumCircuit(1,1)
# qc.h(0)
# qc.s(0)
# qc.h(0)
# qc.measure(0,0)
# qc.draw('mpl')
# plt.show()

# Given the following code, what is the depth of the circuit?

# qc = QuantumCircuit(2, 2)
# qc.h(0)
# qc.barrier(0)
# qc.cx(0,1)
# qc.x(0)
# qc.x(1)
# qc.barrier([0,1])

# print(qc.depth())

# Which code snippet would execute a circuit given these parameters?
# qc = QuantumCircuit(3, 3)
# qc.h([0,2])
# qc.cx(0,1)
# qc.s(1)
# qc.barrier()
# qc.measure([0,1,2],[0,1,2])

# qasm_sim = Aer.get_backend('qasm_simulator')  
# couple_map = [[0, 1], [1, 2]]
# job = execute(qc, backend=qasm_sim, shots=1024, coupling_map=couple_map)

# result_sim = job.result()
# counts = result_sim.get_counts(qc)
# plot_histogram(counts)
# plt.show()

# Which of these would execute a circuit on a set of qubits which are coupled in a custom way?

# A.execute(qc, backend, shots=1024, coupling_map=[[0,1], [1,2]]) 

# the cloupling map is used for list of pars qbits in the processor that are physically linked

# Which three simulators are available in BasicAer?

# QasmSimulatorPy / StatevectorSimulatorPy / UnitarySimulatorPy

#  Which line of code would assign a statevector simulator object to the variable backend?

# backend = BasicAer.get_backend('statevector_simulator')

#  Which code fragment would yield an operator that represents a single-qubit X gate?

# qc = QuantumCircuit(1)
# qc.x(0)
# op = Operator(qc)

# What would be the fidelity result(s) for these two operators, which differ only by global phase?

# op_a = Operator(XGate())
# op_b = np.exp(1j * 0.5) * Operator(XGate())

# print(average_gate_fidelity(op_a, op_b))
# print(process_fidelity(op_a, op_b))

# Given this code fragment, which output fits most closely with the measurement probability distribution?

qc = QuantumCircuit(2, 2)
qc.x(0)
qc.measure([0,1], [0,1])
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()
counts  = result.get_counts(qc)
print(counts)