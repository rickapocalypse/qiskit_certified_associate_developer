from qiskit import IBMQ, BasicAer, QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider
from qiskit.tools import job_monitor
from qiskit.visualization import plot_gate_map, plot_error_map
from qiskit.providers.ibmq import least_busy
from qiskit_ibm_runtime import QiskitRuntimeService
import matplotlib.pyplot as plt

provider = IBMProvider()
# the least busy backend among other configuration preferences can be also selected directly by
BasicAer.backends()
backend = least_busy(provider.backends(filters=lambda b: b.configuration().n_qubits >= 3 and
                                   not b.configuration().simulator and b.status().operational==True))

print(backend)
plot_gate_map(backend, plot_directed = True)
plot_error_map(backend)
plt.show()
