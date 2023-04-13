from qiskit import IBMQ, BasicAer, QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider
from qiskit.tools import job_monitor
from qiskit.visualization import plot_gate_map, plot_error_map
from qiskit.providers.ibmq import least_busy
from qiskit_ibm_runtime import QiskitRuntimeService
import matplotlib.pyplot as plt

# Importing files and exporting string with QASM

# for import the file with the type .qasm
# qc_open = QuantumCircuit.from_qasm_file('myfile.qasm')
# qc_open.draw('mpl')
# plt.show()

# Exporting string with QASM

temp = QuantumCircuit(2)
temp.h(0)
temp.h(1)
temp.s(0)
temp.s(1)

qasm_str = temp.qasm()

qc_open1 = QuantumCircuit.from_qasm_str(qasm_str)

backend_sim = BasicAer.get_backend('qasm_simulator')
job = execute(qc_open1, backend_sim, shots = 1024)

job_monitor(job)