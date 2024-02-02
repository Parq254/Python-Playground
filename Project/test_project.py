import datetime
import unittest
from period_tracker import PeriodTracker

class TestPeriodTracker(unittest.TestCase):
    def test_period_tracker(self):
        tracker = PeriodTracker()
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 1, 28)
        tracker.add_cycle(start_date, end_date)

        # Test calculate_cycle_length
        expected_cycle_length = 27
        actual_cycle_length = tracker.calculate_cycle_length(start_date, end_date)
        self.assertEqual(actual_cycle_length, expected_cycle_length, "Cycle length calculation is incorrect.")

        # Test predict_next_period
        expected_next_period = datetime.date(2023, 1, 28) + datetime.timedelta(days=expected_cycle_length)
        actual_next_period = tracker.predict_next_period(end_date, actual_cycle_length)
        self.assertEqual(actual_next_period, expected_next_period, "Next period prediction is incorrect.")

if __name__ == "__main__":
    unittest.main()
