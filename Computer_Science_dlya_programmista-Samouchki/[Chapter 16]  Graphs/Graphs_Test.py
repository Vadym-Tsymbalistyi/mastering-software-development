from unittest import TestCase, main
from Chapter_16_Graphs import dijkstra


class TestGraphs(TestCase):
    def test_short_path(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2},
            'C': {'A': 4, 'B': 2},
            'D': {}
        }
        start_vertex = ('A')
        end_vertex = ('C')
        result_path = dijkstra(graph, start_vertex, end_vertex)
        self.assertEqual(result_path, ['A', 'B', 'C'])

    def test_short_not_path(self):
        my_network = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2},
            'C': {'A': 4, 'B': 2},
            'D': {'E': 3},
            'E': {'D': 3}
        }
        start_vertex = 'A'
        end_vertex = 'E'
        result_path = dijkstra(my_network, start_vertex, end_vertex)
        self.assertEqual(result_path, "There is no path from A to E.")


if __name__ == '__main__':
    main()
