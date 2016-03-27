import unittest
import localization
import math


class LocateFourAnchors(unittest.TestCase):

    def setUp(self):
        self.TARGET = (2, 2)
        self.POSITIONS = {
            'dev-0': (0, 0),  # Reference anchor
            'dev-1': (4, 1),
            'dev-2': (3, 2),
            'dev-3': (1, 3),
        }
        self.OBSERVATIONS = (
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

    def solve(self):
        P = localization.Project()

        # Add all the "anchors"
        for device, position in self.POSITIONS.items():
            P.add_anchor(device, position)

        # Add a target
        target, target_label = P.add_target()

        # Add the observations on the target
        for dev, mac, distance, tstamp in self.OBSERVATIONS:
            target.add_measure(dev, distance)

        # Run the solver
        P.solve()
        return target.loc.x, target.loc.y

    def check_result(self, x, y, tolerance=0.2):
        xx = abs(self.TARGET[0] - x)
        yy = abs(self.TARGET[1] - y)
        self.assertTrue(xx < tolerance * self.TARGET[0])
        self.assertTrue(yy < tolerance * self.TARGET[1])

    def test_solve(self):
        x, y = self.solve()
        self.check_result(x, y)
