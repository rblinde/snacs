""" Runs the algorithms on different datasets """

import time
import networkx as nx
from networkx.algorithms import community
from collections import defaultdict

def write_to_file(name, communities):
    """ Writes results to file, unsorted => use bash to sort """
    sequence = {}

    for i, c in enumerate(communities):
        for node in list(c):
            sequence[int(node)] = i

    # sequence = sorted(list(sequence.items()))
    sequence = sorted(list(sequence.items()))
    sequence = [f"{i[0]} {i[1]}\n" for i in sequence]

    with open(name, "w") as file:
        file.writelines(sequence)


def coms_normal(result):
    return [set(x) for x in result]


def coms_gen(result):
    return [set(x) for x in next(result)]


def run(dataset, name, algorithm, fn):
    """ Runs algorithm on dataset, if lpa 10 times """
    def iteration(i):
        start = time.time()
        result = algorithm(G)
        middle = time.time()
        communities = fn(result)
        end = time.time()
        run_time = round((end - start) * 1000, 6)
        middle_time = round((middle - start) * 1000, 6)
        print(f"RTime | {name} | {dataset} | {i} | {run_time}", file=open("times.txt", "a"))
        print(f"MTime | {name} | {dataset} | {i} | {middle_time}", file=open("times.txt", "a"))
        write_to_file(f"results/{dataset}/result-{name}-{i}.txt", communities)
        # Output
        print(f"Dataset {dataset} completed iteration {i} for algorithm {name}!")

    G = nx.read_edgelist(f"datasets/{dataset}/edges.txt")
    iteration(0)
    if name == "lpa":
        for i in range(1, 10):
            iteration(i)


if __name__ == '__main__':
    for dataset in ["karate", "football", "email", "corporate-small", "corporate"]:
        run(dataset, "lpa", community.asyn_lpa_communities, coms_normal)
        run(dataset, "gn", community.girvan_newman, coms_gen)
        run(dataset, "gm", community.greedy_modularity_communities, coms_normal)
