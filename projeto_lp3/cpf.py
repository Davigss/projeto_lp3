from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("403.200.138-39"))

cpfs = [
    "296.643.335-30"
    "334.796.027-00"
    "403.200.138-39"
]

print(cpf.validate_list(cpfs))

print("CPF irmão")
