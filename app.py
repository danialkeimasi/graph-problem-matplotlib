import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Graph:
    """ directed weighted graph """

    def __init__(self, edgelist=[]):
        """ edge list is a special list that shows a graph """

        self.constract_by_edgelist(edgelist)

    def input_cli(self):
        """ a cli interface for get the wanted graph """

        size = int(input('enter number of seosons: '))
        weight_list = [int(input(f'pages of {i+1}th season: ')) for i in range(size)]

        self.constract_with(size, weight_list)
        return self
        
    def constract_with(self, seasons_len, weight_list):
        """ constract the special graph """

        G = nx.DiGraph()

        node_numbers = list(map(lambda n: n+1, range(seasons_len))) + ['done']
        G.add_nodes_from(node_numbers)

        for i, node_number in enumerate(node_numbers[:-1]):
            G.add_edge(node_numbers[i], node_numbers[i + 1], weight=weight_list[i])

        self.graph = G
        return self

    def show(self):
        """ showing the graph in the screen """

        G = self.graph
        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size=1000)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=6)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

        edge_labels=dict([((u, v), d['weight']) for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_family='sans-serif')

        plt.axis('off')
        plt.show()
        
    def constract_by_edgelist(self, edgelist):
        """ constract a graph by it's edge list """
        
        G = nx.DiGraph()
        G.add_edges_from(edgelist)
        
        self.graph = G
        return self

    def get_weight_list(self):
        """ get the wights of path edges as a list """

        return [edge[2]['weight'] for edge in list(self.graph.edges(data=True))]


    def limit_read_to_days(self, wanted_days):
        """ the answer for the problem """
        
        page_per_days = self.get_weight_list()
        season_per_day = [1 for i in page_per_days]

        while len(season_per_day) > wanted_days:
            
            indexes = [page_per_days[i] + page_per_days[i+1] for i in range(len(page_per_days) - 1)]
            replace_index = np.argmin(indexes)
            del_index = replace_index + 1
            
            page_per_days[replace_index] += page_per_days[del_index]; page_per_days.pop(del_index)
            season_per_day[replace_index] += season_per_day[del_index]; season_per_day.pop(del_index)
        
        return season_per_day


if __name__ == "__main__":

    input_graph = Graph().input_cli()
    wanted_days = int(input('how many days you want to spend on this book: '))

    season_per_days = input_graph.limit_read_to_days(wanted_days)
    
    for i, season in enumerate(season_per_days):
        print(f'in day number {i+1} you must read {season} {"season" if season == 1 else "seasons"}')

    Graph().constract_with(len(season_per_days), season_per_days).show()
    