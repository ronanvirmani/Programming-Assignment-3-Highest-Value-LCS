import matplotlib.pyplot as plt

def graph_runtimes(filepath):
    names, sizes, times = [], [], []

    with open(filepath) as f:
        for line in f:
            name, size, time = line.split()
            names.append(name)
            sizes.append(int(size))
            times.append(float(time))

    plt.figure(figsize=(10, 6))
    plt.bar(names, times)
    plt.xlabel('File')
    plt.ylabel('Runtime (ms)')
    plt.title('Highest Value LCS Runtime')
    plt.savefig('runtime_graph.png')

if __name__ == "__main__":
    graph_runtimes('data/runtimes.txt')
