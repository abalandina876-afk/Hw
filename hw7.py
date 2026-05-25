import time
import unittest


def measure_time(func, *args, **kwargs):
    start_time = time.time()

    result = func(*args, **kwargs)

    end_time = time.time()

    execution_time = end_time - start_time

    return result, execution_time


def slow_function():
    time.sleep(1)
    return "Done"


class TestMeasureTime(unittest.TestCase):

    def test_result(self):
        result, exec_time = measure_time(slow_function)

        self.assertEqual(result, "Done")

    def test_time(self):
        result, exec_time = measure_time(slow_function)

        self.assertTrue(exec_time >= 1)

    def test_type(self):
        result, exec_time = measure_time(slow_function)

        self.assertIsInstance(exec_time, float)


if __name__ == "__main__":
    unittest.main()