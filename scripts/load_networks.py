import argparse

import networkx as nx
import pandas as pd


def main():

    # Read arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--networks_file', default=None, type=str, required=True, help='Networks file')
    parser.add_argument('--type', default=None, type=str, required=True, help='Weighted or unweighted network')
    args = parser.parse_args()

    # Load networks
    networks = pd.read_csv(args.networks_file)

    # Extract weighted or unweighted network
    if args.type == 'weighted':
        G = nx.Graph()
        edges = zip(
            networks['node_1'],
            networks['node_2'],
            networks['weighted']
        )
        G.add_weighted_edges_from(edges)
    else:
        G = nx.Graph()
        edges = zip(
            networks[networks.unweighted == 1]['node_1'],
            networks[networks.unweighted == 1]['node_2']
        )
        G.add_edges_from(edges)

    # Do something with network here


if __name__ == '__main__':
    main()
