""" Create network visualisation of karate club network"""

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

COLORS = ["#F44336", "#3F51B5"]

def parse_input(file_name):
    """ Retrieve communities from file """
    with open(file_name) as file:
        return [int(line.split()[1]) for line in file.readlines()]


def create_figure(ground, result):
    """ Create image """
    graph = nx.read_edgelist("datasets/karate/edges.txt")
    edgecolors = [COLORS[i] for i in ground]
    nodecolors = [COLORS[i] for i in result]
    # Create image
    position = nx.spring_layout(graph)
    nx.draw(graph, position, node_color=nodecolors, edgecolors=edgecolors, linewidths=2)
    # Save image
    plt.suptitle(f"Zachary karate network compared to ground-truth")
    plt.savefig("plots/karate-graph.png", bbox_inches="tight")


def calc_acc(ground, result, n):
    """ Calculates accuracy """
    sum = 0
    size = len(ground)
    for i in range(size):
        for j in range(i + 1, size):
            eq_ground = ground[i] == ground[j]
            eq_result = result[i] == result[j]
            if eq_ground == eq_result:
                sum = sum + 1
    return 2 * sum / (n * n - n)


if __name__ == "__main__":
    ground = parse_input("datasets/karate/communities.txt")
    result = parse_input("results/karate/result-lpa-3.txt")
    accuracy = calc_acc(ground, result, 34)
    create_figure(ground, result)
    print(round(accuracy, 4))
