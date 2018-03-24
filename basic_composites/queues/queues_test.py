import unittest
from queues import *


class QueueTest(unittest.TestCase):
    def test_queue_create(self):
        queue = Queue()
        self.assertIsInstance(
            queue,
            Queue
        )

    def test_queue_enqueue(self):
        queue = Queue()
        item = "tacos"
        queue.enqueue(item)
        self.assertTrue(
            item in queue
        )

    def test_queue_dequeue(self):
        queue = Queue()
        item = "tacos"
        queue.enqueue(item)
        self.assertEqual(
            queue.dequeue(),
            item
        )

    def test_queue_dequeue_order(self):
        queue = Queue()
        first_item = "tacos"
        second_item = "tequila"
        queue.enqueue(first_item)
        queue.enqueue(second_item)
        self.assertEqual(
            queue.dequeue(),
            first_item
        )

    def test_queue_is_empty(self):
        queue = Queue()
        self.assertTrue(
            queue.is_empty()
        )

        item = "tacos"
        queue.enqueue(item)
        self.assertFalse(
            queue.is_empty()
        )

    def test_queue_peek(self):
        queue = Queue()
        item = "tacos"
        queue.enqueue(item)
        self.assertEqual(
            queue.peek(),
            item
        )

        self.assertFalse(
            queue.is_empty()
        )

if __name__ == "__main__":
    unittest.main()
