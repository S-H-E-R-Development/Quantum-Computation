token = "9893816a20245ce64d0244516e6f47f0caaf815c1b3e149300cea30d50c8885fc94f1c7d12e8464a4a37860f90f67e2c7ec2b38a7b8460c9973bbba2b25a6fbe"
from qiskit_ibm_runtime import QiskitRuntimeService
 
QiskitRuntimeService.save_account(
  token=token,
  channel="ibm_quantum" # `channel` distinguishes between different account types
) 