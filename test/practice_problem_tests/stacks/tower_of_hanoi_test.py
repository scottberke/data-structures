import unittest

from data_structures.basic_composites.stacks.stack_array import *
from practice_problems.stacks.tower_of_hanoi import *

class TowerOfHanoiTest(unittest.TestCase):
    def setup_tower(self, tower, discs):
        # Add items to towers in decending order
        discs.sort(reverse=True)
        for disc in discs:
            tower.append(disc)

    def test_tower_of_hanoi_empty(self):
        # Create 'towers'
        start_tower = Stack("start")
        temp_tower = Stack("temp")
        end_tower = Stack("end")
        self.assertIsNone(
            solve_tower_of_hanoi(start_tower.size(), start_tower, temp_tower, end_tower)
        )

    def test_tower_of_hanoi_1(self):
        # Create 'towers'
        start_tower = Stack("start")
        temp_tower = Stack("temp")
        end_tower = Stack("end")
        self.setup_tower(start_tower, [1])
        self.assertIsNone(
            solve_tower_of_hanoi(start_tower.size(), start_tower, temp_tower, end_tower)
        )

        # We should go from start tower to end tower
        self.assertTrue(
            start_tower.is_empty() and end_tower.size() == 1
        )

        # End tower should pop in decending order ie first to last: 1 -> 2
        for i in range(1,2):
            self.assertEqual(
                i,
                end_tower.pop()
            )


    def test_tower_of_hanoi_2(self):
        # Create 'towers'
        start_tower = Stack("start")
        temp_tower = Stack("temp")
        end_tower = Stack("end")
        self.setup_tower(start_tower, [1, 2])

        solve_tower_of_hanoi(start_tower.size(), start_tower, temp_tower, end_tower)

        # We should go from start tower to end tower
        self.assertTrue(
            start_tower.is_empty() and end_tower.size() == 2
        )

        # End tower should pop in decending order ie first to last: 1 -> 2
        for i in range(1,3):
            self.assertEqual(
                i,
                end_tower.pop()
            )


    def test_tower_of_hanoi_3(self):
        # Create 'towers'
        start_tower = Stack("start")
        temp_tower = Stack("temp")
        end_tower = Stack("end")
        self.setup_tower(start_tower, [1, 2, 3])

        solve_tower_of_hanoi(start_tower.size(), start_tower, temp_tower, end_tower)

        # We should go from start tower to end tower
        self.assertTrue(
            start_tower.is_empty() and end_tower.size() == 3
        )

        # End tower should pop in decending order ie first to last: 1 -> 2 -> 3
        for i in range(1,4):
            self.assertEqual(
                i,
                end_tower.pop()
            )


    def test_tower_of_hanoi_4(self):
        # Create 'towers'
        start_tower = Stack("start")
        temp_tower = Stack("temp")
        end_tower = Stack("end")
        self.setup_tower(start_tower, [1, 2, 3, 4])

        solve_tower_of_hanoi(start_tower.size(), start_tower, temp_tower, end_tower)

        # We should go from start tower to end tower
        self.assertTrue(
            start_tower.is_empty() and end_tower.size() == 4
        )

        # End tower should pop in decending order ie first to last: 1 -> 2 -> 3 -> 4
        for i in range(1,5):
            self.assertEqual(
                i,
                end_tower.pop()
            )



if __name__ == "__main__":
    unittest.main()
