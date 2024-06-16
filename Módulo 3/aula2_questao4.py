{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "211cf884-4463-46f6-a57e-2d6964270490",
   "metadata": {},
   "source": [
    "Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. \n",
    "Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:\r\n",
    "Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.\r\n",
    "Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.\r\n",
    "Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.\r\n",
    "O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida. Segue um exemplo de interação com seu código no terminal, com entradas de dados destacadas em negrito e as impressões de seu código em itálico.\r\n",
    "\r\n",
    "Escolha a classe (guerreiro, mago ou arqueiro): mago\r\n",
    "Digite os pontos de força (de 1 a 20): 8\r\n",
    "Digite os pontos de magia (de 1 a 20): 17\r\n",
    "Pontos de atributo consistentes com a classe escolhida: True\r\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e0d1b66f-37ee-4173-b320-2003b92503e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha a classe (guerreiro, mago ou arqueiro):  mago\n",
      "Digite os pontos de força (de 1 a 20):  5\n",
      "Digite os pontos de magia (de 1 a 20):  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pontos de atributo consistentes com a classe escolhida: True\n"
     ]
    }
   ],
   "source": [
    "classe = input(\"Escolha a classe (guerreiro, mago ou arqueiro): \")\n",
    "pforca = int(input(\"Digite os pontos de força (de 1 a 20): \"))\n",
    "pmagia = int(input(\"Digite os pontos de magia (de 1 a 20): \"))\n",
    "\n",
    "if classe == \"guerreiro\":\n",
    "    if pforca >=15 and pmagia <= 10:\n",
    "        print(\"Pontos de atributo consistentes com a classe escolhida: True\")\n",
    "    else:\n",
    "        print(\"Pontos de atributo consistentes com a classe escolhida: False\")\n",
    "elif classe == \"mago\":\n",
    "    if pforca <= 10 and pmagia >= 15:\n",
    "        print(\"Pontos de atributo consistentes com a classe escolhida: True\")\n",
    "    else:\n",
    "        print(\"Pontos de atributo consistentes com a classe escolhida: False\")\n",
    "else:\n",
    "    if (pforca > 5 and pforca <= 15) and (pmagia> 5 and pmagia <= 15):\n",
    "        print(\"Pontos de atributo consistentes com a classe escolhida: True\")\n",
    "    else:\n",
    "        print(\"Pontos de atributo consistentes com a classe escolhida: False\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c21ddd7-e947-4b7f-ab68-440d2c995da6",
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
