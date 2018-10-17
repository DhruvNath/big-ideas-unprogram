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
    "            for line in workFile:\n",
    "                print(line)\n",
    "            #return workFile\n",
    "        except:\n",
    "            isFile = False\n",
    "            print(\"THAT IS NOT A FILE. PLEASE TRY AGAIN\")\n",
    "\n",
    "loadFile()\n"
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
