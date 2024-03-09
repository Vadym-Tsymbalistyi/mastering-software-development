from unittest import TestCase, main
from Dijkstra import dijkstra


class TestDijkstra(TestCase):
    def test_short_path_found(self):
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

    def test_short_path_not_found(self):
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
