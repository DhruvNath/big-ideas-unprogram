{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "isFile = False\n",
    "while (isFile == False):\n",
    "    newfile = input(\"Enter a file please:\")\n",
    "    try:\n",
    "        workFile = open(newfile)\n",
    "        isFile = True\n",
    "    except:\n",
    "        isFile = False\n",
    "        print(\"THAT IS NOT A FILE. PLEASE TRY AGAIN\")\n",
    "\n",
    "count = 0\n",
    "spamSum = 0\n",
    "hiCount = 0\n",
    "for line in workFile:        \n",
    "    spam = line\n",
    "\n",
    "    perc = spam.split(' ', 1)[1]\n",
    "    perc = float(perc)\n",
    "    spamSum += perc\n",
    "    count = count + 1\n",
    "    if perc > .90:\n",
    "        hiCount = hiCount + 1\n",
    "\n",
    "totPerc = spamSum/count\n",
    "        \n",
    "\n",
    "print(\"The average spam confidece is:\" , totPerc)\n",
    "print(\"The number of emails above 90% spam is:\" , hiCount)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
