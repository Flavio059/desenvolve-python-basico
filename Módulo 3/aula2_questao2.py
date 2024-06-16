{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7ecd0650-fbb4-4627-ad7b-049f3de89383",
   "metadata": {},
   "source": [
    "2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade\n",
    "(ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d0cde5a-281e-4576-a723-a93ada230881",
   "metadata": {},
   "outputs": [],
   "source": [
    "juliana= int(input(\"Informe a idade de Juliana: \"))\n",
    "cris= int(input(\"Informe a idade de Cris: \"))\n",
    "print(juliana>=17 or cris>=17)"
   ]
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
