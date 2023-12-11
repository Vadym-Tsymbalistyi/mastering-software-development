from unittest import TestCase, main
from Chapter_12_Queues import Queue


class TestQueue(TestCase):
    # def setUp(self):
    #    queue = Queue()
    #    queue.enqueue(1)
    #    queue.enqueue(2)
    #    queue.enqueue(3)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.s1, [1, 2, 3])

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        result = queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(queue.s1, [])
        self.assertEqual(queue.s2, [3, 2])


if __name__ == '__main__':
    main()
