import unittest
import localization
import math


class LocateFourAnchors(unittest.TestCase):

    GOOD_TOLERANCE = 0.1  # percentage
    BAD_TOLERANCE = 0.1  # percentage

    TARGET = (2, 2)
    POSITIONS = {
        'dev-0': (0, 0),  # Reference anchor
        'dev-1': (4, 1),
        'dev-2': (3, 2),
        'dev-3': (1, 3),
    }
    OBSERVATIONS = (
        ('dev-3', 'M1', math.sqrt(2) * 1.10, 0),
        ('dev-3', 'M1', math.sqrt(2) * 1.01, 0),
        ('dev-3', 'M1', math.sqrt(2) * 0.98, 0),

        ('dev-3', 'M1', math.sqrt(2) * 0.92, 0),
        ('dev-3', 'M1', math.sqrt(2) * 1.02, 0),
        ('dev-3', 'M1', math.sqrt(2) * 1.12, 0),

        ('dev-0', 'M1', 2 * math.sqrt(2) * 1.05, 0),
        ('dev-0', 'M1', 2 * math.sqrt(2) * 1.12, 0),

        ('dev-2', 'M1', 1 * 0.95, 0),
        ('dev-2', 'M1', 1 * 0.99, 0),
        ('dev-2', 'M1', 1 * 1.11, 0),
        ('dev-2', 'M1', 1 * 1.02, 0),
    )

    def solve(self, observations=OBSERVATIONS):
        P = localization.Project()

        # Add all the "anchors"
        for device, position in self.POSITIONS.items():
            P.add_anchor(device, position)

        # Add a target
        target, target_label = P.add_target()

        # Add the observations on the target
        for dev, mac, distance, tstamp in observations:
            target.add_measure(dev, distance)

        # Run the solver
        P.solve()
        return target.loc.x, target.loc.y

    def check_result(self, x, y, tolerance=0.1):
        xx = abs(self.TARGET[0] - x)
        yy = abs(self.TARGET[1] - y)
        self.assertTrue(xx < tolerance * self.TARGET[0])
        self.assertTrue(yy < tolerance * self.TARGET[1])

    def check_bad_result(self, x, y):
        xx = abs(self.TARGET[0] - x)
        yy = abs(self.TARGET[1] - y)
        self.assertLess(xx, 0.90 * self.TARGET[0])
        self.assertLess(yy, 0.90 * self.TARGET[1])
        self.assertGreater(xx, 0.1 * self.TARGET[0])
        self.assertGreater(yy, 0.1 * self.TARGET[1])

    def test_solve_full(self):
        x, y = self.solve(observations=self.OBSERVATIONS)
        self.check_result(x, y)

    def test_solve_partial(self):
        observations = [self.OBSERVATIONS[chosen] for chosen in [0, 3, 6, 8]]
        x, y = self.solve(observations=observations)
        self.check_result(x, y)

    def test_solve_insufficient(self):
        observations = [self.OBSERVATIONS[chosen] for chosen in [0, 8]]
        x, y = self.solve(observations=observations)
        self.check_bad_result(x, y)

    def test_solve_bad_estimation(self):
        observations = [self.OBSERVATIONS[chosen] for chosen in [8, 9]]
        x, y = self.solve(observations=observations)
        self.check_bad_result(x, y)

    def test_solve_single_observation_raises_ValueError(self):
        observations = [self.OBSERVATIONS[chosen] for chosen in [8]]
        self.assertRaises(ValueError, self.solve, observations=observations)
