from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit.from_qasm_file('./quantum_artifact.qasm')
backend = Aer.get_backend("qasm_simulator")
job = execute(qc, backend)
result = job.result()
print(result.get_counts())
