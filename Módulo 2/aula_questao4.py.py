{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "052d1d11-ef4f-4e7d-b263-42b457918b7c",
   "metadata": {},
   "source": [
    "4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível\n",
    "de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada\n",
    "exatamente como indicado. \r\n",
    "\r\n",
    "Entrada:\r\n",
    "576\r\n",
    "\r\n",
    "Saída:\r\n",
    "5 nota(s) de R$100,00\r\n",
    "1 nota(s) de R$50,00\r\n",
    "1 nota(s) de R$20,00\r\n",
    "0 nota(s) de R$10,00\r\n",
    "1 nota(s) de R$5,00\r\n",
    "0 nota(s) de R$2,00\r\n",
    "1 nota(s) de R$1,00"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d38088f3-0fde-4c7a-afa1-a2cd7ae482bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite um valor inteiro:  50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "0 nota(s) de 100,00\n",
      "1 nota(s) de 50,00\n",
      "0 nota(s) de 20,00\n",
      "0 nota(s) de 10,00\n",
      "0 nota(s) de 5,00\n",
      "0 nota(s) de 2,00\n",
      "0 nota(s) de 1,00\n",
      "\n"
     ]
    }
   ],
   "source": [
    "saque = int(input(\"Digite um valor inteiro: \"))\n",
    "\n",
    "notas100 = saque // 100\n",
    "saque %= 100\n",
    "\n",
    "notas50 = saque // 50\n",
    "saque %= 50\n",
    "\n",
    "notas20 = saque // 20\n",
    "saque %= 20\n",
    "\n",
    "notas10 = saque // 10\n",
    "saque %= 10\n",
    "\n",
    "notas5 = saque // 5\n",
    "saque %= 5\n",
    "\n",
    "notas2 = saque // 2\n",
    "saque %= 2\n",
    "\n",
    "notas1 = saque // 1\n",
    "\n",
    "print(f'\\n{notas100} nota(s) de 100,00\\n{notas50} nota(s) de 50,00\\n{notas20} nota(s) de 20,00\\n{notas10} nota(s) de 10,00\\n{notas5} nota(s) de 5,00\\n{notas2} nota(s) de 2,00\\n{notas1} nota(s) de 1,00\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55ea572a-1c75-4b95-9318-90c30573f8d3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
