# -*- coding: utf-8 -*-
"""estruturas_condicionais_ternaria

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xJh_j1fknPHGLrfqVmSPieaTVekOvEUk
"""

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")