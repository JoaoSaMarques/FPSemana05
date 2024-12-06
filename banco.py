class ContaBancaria:
    pass


conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_info()