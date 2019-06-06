import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class Graph:
    def __init__(self, edges_list=None):
        if edges_list:
            self.update(edges_list)
        else:
            self.graph = nx.DiGraph()


    def input_cli(self):
        size = int(input('enter number of seosons: '))
        weight_list = [int(input(f'pages of {i+1}th season: ')) for i in range(size)]
        self.constract_with(size, weight_list)

        return self
        

    def constract_with(self, seasons_len, weight_list):
        G = nx.DiGraph()

        node_numbers = list(map(lambda n: n+1, range(seasons_len))) + ['done']
        G.add_nodes_from(node_numbers)

        for i, node_number in enumerate(node_numbers[:-1]):
            G.add_edge(node_numbers[i], node_numbers[i + 1], weight=weight_list[i])

        self.graph = G

        return self
        

    def show(self):
        G = self.graph
        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size=1000)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=6)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

        edge_labels=dict([((u, v), d['weight']) for u,v,d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_family='sans-serif')

        plt.axis('off')
        plt.show()
        

    def update(self, edge_list):
        G = nx.DiGraph()
        G.add_edges_from(edge_list)
        self.graph = G

        return self

    
    def get_weight_list(self):
        return [edge[2]['weight'] for edge in list(self.graph.edges(data=True))]
    


def answer(page_per_days, wanted_days):
    season_per_day = [1 for i in page_per_days]

    while len(page_per_days) > wanted_days:

        del_index = np.argmin(page_per_days)

        indexes = {ind:page_per_days[ind] for ind in [del_index + 1, del_index - 1] if 0 <= ind < len(page_per_days)}        
        index = min(indexes, key=indexes.get)

        page_per_days[index] += page_per_days[del_index]
        season_per_day[index] += 1
        
        season_per_day.pop(del_index)
        page_per_days.pop(del_index)
    
    return season_per_day


if __name__ == "__main__":
    input_graph = Graph().input_cli()

    season_pages = input_graph.get_weight_list()
    wanted_days = int(input('how many days you want to spend on this book: '))

    season_per_days = answer(season_pages, wanted_days)
    for i, season in enumerate(season_per_days):
        print(f'in day number {i+1} you must read {season} {"season" if season == 1 else "seasons"}')

    Graph().constract_with(len(season_per_days), season_per_days).show()
    