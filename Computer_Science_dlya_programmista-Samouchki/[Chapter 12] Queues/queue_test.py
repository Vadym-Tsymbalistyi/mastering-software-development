from unittest import TestCase, main
from Chapter_12_Queues import Queue


class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_dequeue(self):
        result = self.queue.dequeue()
        self.assertEqual(result, 1)

    def test_dequeue_empty(self):
        self.queue = Queue()
        with self.assertRaises(Exception) as context:
            self.queue.dequeue()
        self.assertEqual(str(context.exception), "Cannot pop from empty queue")


if __name__ == '__main__':
    main()
