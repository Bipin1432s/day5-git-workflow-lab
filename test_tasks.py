
import unittest
from src.tasks import tasks, add_task, delete_task


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        tasks.clear()
        tasks.extend([
            "Learn Python",
            "Learn Git",
            "Build an AI app"
        ])

    def test_delete_valid_task(self):
        result = delete_task(2)

        self.assertTrue(result)
        self.assertEqual(
            tasks,
            ["Learn Python", "Build an AI app"]
        )

    def test_delete_first_task(self):
        result = delete_task(1)

        self.assertTrue(result)
        self.assertEqual(
            tasks,
            ["Learn Git", "Build an AI app"]
        )

    def test_delete_invalid_task(self):
        result = delete_task(10)

        self.assertFalse(result)
        self.assertEqual(len(tasks), 3)

    def test_delete_zero(self):
        result = delete_task(0)

        self.assertFalse(result)
        self.assertEqual(len(tasks), 3)

    def test_delete_non_integer(self):
        result = delete_task("two")

        self.assertFalse(result)
        self.assertEqual(len(tasks), 3)

    def test_delete_from_empty_list(self):
        tasks.clear()

        result = delete_task(1)

        self.assertFalse(result)
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
