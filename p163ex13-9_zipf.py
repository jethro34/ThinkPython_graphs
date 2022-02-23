# Reads text from a file, counts word frequencies, generates lists of coordinates, and plots the points,
# in order to check for Zipf's Law.

import string
import math
import matplotlib.pyplot as plt


def read_n_strip(file):
    """ Reads a text file and populates its words / tokens into a histogram dictionary. """

    fin = open(file)
    for line in fin:
        for pre_word in line.replace("--", " ").replace("“", " ").split():
            word = pre_word.strip(string.punctuation + string.whitespace).lower()
            if word != "" and not word.isdigit():
                words[word] = words.get(word, 0) + 1


def hist_to_plot(dikt):
    """ Reads a histogram dictionary and returns a list of tuples of words, log of freq, and log of rank
        by decreasing frequency.
        Output: list [(i1, i2, i3), ...] """

    liste = sorted(sorted(dikt), key=dikt.get, reverse=True)                                    # organizing by value
    return [(wort, math.log(words[wort]), math.log(liste.index(wort) + 1)) for wort in liste]


def plot_hist(lista):
    """ Plots coordinates from tuples in a given list. """

    x = [tupel[1] for tupel in lista[:300]]
    y = [tupel[2] for tupel in lista[:300]]

    plt.plot(x, y)                          # plotting the points

    plt.xlabel('x - axis')                  # naming the x axis
    plt.ylabel('y - axis')                  # naming the x axis

    plt.title("Zipf's Law")                 # titling the graph

    plt.show()                              # showing the plot
    return None


words = {}

read_n_strip("/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/finnish.txt")

for tupel in hist_to_plot(words)[:300]:
    print(tupel)

plot_hist(hist_to_plot(words))
