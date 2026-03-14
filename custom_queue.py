import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # TODO: Add an item to the end of the queue
        print(f"Enqueue count...")
        self.items.append(item)
        print(f"Queue contains {len(self.items)} customers")

    def dequeue(self):
        # TODO: Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        # TODO: Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")

    def is_empty(self):
        # TODO: Return True if the queue is empty
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        # TODO: Implement winner selection and dequeue process
        if self.is_empty():
            raise IndexError("No customers in the queue")

        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]

        for _ in range(winner_index + 1):
            self.dequeue()

        return winner
