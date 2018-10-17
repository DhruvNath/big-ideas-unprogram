{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def loadFile():\n",
    "    isFile = False\n",
    "    while (isFile == False):\n",
    "        newfile = input(\"Enter a file please:\")\n",
    "        try:\n",
    "            workFile = open(newfile)\n",
    "            isFile = True\n",
    "            return workFile\n",
    "        except:\n",
    "            isFile = False\n",
    "            print(\"THAT IS NOT A FILE. PLEASE TRY AGAIN\")\n",
    "\n",
    "workFile = loadFile()\n",
    "allWords = []\n",
    "for line in workFile:\n",
    "    line = line.lower()\n",
    "    line = line.split('\\n')[0]\n",
    "    lineCheck = line.split(' ')\n",
    "    for word in lineCheck:\n",
    "        if word not in allWords:\n",
    "            allWords.append(word)\n",
    "            \n",
    "allWords.sort()\n",
    "print(allWords)"
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
