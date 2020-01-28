""" Create lineplot diagram for runtime of algorithms """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot(data, datasets):
    """ Creates lineplot from data """
    # Convert data to image
    df = pd.DataFrame.from_dict(data, orient="index", columns=["Algorithm", "Dataset", "Time"])
    sns.lineplot(x="Dataset", y="Time", data=df, hue="Algorithm")
    # Adjust axes and title
    plt.xlabel("Dataset")
    plt.xticks([0, 1, 2, 3, 4], datasets)
    plt.ylabel("Runtime (ms)")
    plt.yscale("log")
    plt.subplots_adjust(top=0.9)
    plt.suptitle(f"Runtime of algorithms for each dataset")
    plt.savefig(f"plots/timings.png", bbox_inches='tight')


if __name__ == "__main__":
    # Seaborn
    sns.set()
    sns.set_palette("husl")
    # Data
    datasets = ["Zachary karate", "US football", "email-Eu-core", "corp-small", "corp-large"]
    data = {
        0: ["LPA", 0, 3.697299799999999],
        1: ["LPA", 1, 16.386056000000004],
        2: ["LPA", 2, 508.3435775],
        3: ["LPA", 3, 324.15874],
        4: ["LPA", 4, 129840.73829640001],
        5: ["BC", 0, 97.74692049999999],
        6: ["BC", 1, 5947.0302582],
        7: ["BC", 2, 146602.3483275],
        8: ["BC", 3, 9306.9722892],
        10: ["M", 0, 6.2677382],
        11: ["M", 1, 37.1651887],
        12: ["M", 2, 3003.0499936],
        13: ["M", 3, 856.9651601999998],
        12: ["M", 4, 17199643.719435],
    }
    # Plot
    plot(data, datasets)
