from unittest import TestCase, main
from Chapter_16_Graphs import dijkstra


class TestGraphs(TestCase):
    def test_short_path_graph1(self):
        graph1 = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2},
            'C': {'A': 4, 'B': 2},
            'D': {}
        }
        start_vertex = ('A')
        end_vertex = ('C')
        result_path = dijkstra(graph1, start_vertex, end_vertex)
        self.assertEqual(result_path, ['A', 'B', 'C'])

    def test_short_path(self):
        graph2 = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2},
            'C': {'A': 4, 'B': 2},
            'D': {'E': 3},
            'E': {'D': 3}
        }
        start_vertex = 'A'
        end_vertex = 'E'
        result_path = dijkstra(graph2, start_vertex, end_vertex)
        self.assertEqual(result_path, "Нет пути из A в E")


if __name__ == '__main__':
    main()
