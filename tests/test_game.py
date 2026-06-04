"""Test cases for cricket game"""

import unittest
from game.player import Batsman, Bowler, Stats
from game.utils import Delivery, Shot, get_delivery_effectiveness, calculate_runs


class TestBatsman(unittest.TestCase):
    """Test cases for Batsman class"""
    
    def setUp(self):
        self.batsman = Batsman("Test Batsman")
    
    def test_batsman_initialization(self):
        """Test batsman is initialized correctly"""
        self.assertEqual(self.batsman.name, "Test Batsman")
        self.assertEqual(self.batsman.stats.runs, 0)
        self.assertFalse(self.batsman.is_out)
    
    def test_score_runs(self):
        """Test scoring runs"""
        self.batsman.score_runs(4)
        self.assertEqual(self.batsman.stats.runs, 4)
        self.assertEqual(self.batsman.stats.balls_faced, 1)
        self.assertEqual(self.batsman.stats.fours, 1)
    
    def test_score_six(self):
        """Test scoring a six"""
        self.batsman.score_runs(6)
        self.assertEqual(self.batsman.stats.sixes, 1)
        self.assertEqual(self.batsman.stats.runs, 6)
    
    def test_get_out(self):
        """Test batsman gets out"""
        self.batsman.get_out()
        self.assertTrue(self.batsman.is_out)
        self.assertEqual(self.batsman.stats.outs, 1)
    
    def test_consecutive_failures(self):
        """Test tracking consecutive failures"""
        self.batsman.add_failure()
        self.batsman.add_failure()
        self.assertEqual(self.batsman.consecutive_failures, 2)
        
        # Reset on scoring
        self.batsman.score_runs(2)
        self.assertEqual(self.batsman.consecutive_failures, 0)


class TestBowler(unittest.TestCase):
    """Test cases for Bowler class"""
    
    def setUp(self):
        self.bowler = Bowler("Test Bowler")
    
    def test_bowler_initialization(self):
        """Test bowler is initialized correctly"""
        self.assertEqual(self.bowler.name, "Test Bowler")
        self.assertEqual(self.bowler.stats.wickets, 0)
    
    def test_take_wicket(self):
        """Test taking a wicket"""
        self.bowler.take_wicket()
        self.assertEqual(self.bowler.stats.wickets, 1)
    
    def test_bowl_ball(self):
        """Test bowling a ball"""
        self.bowler.bowl_ball()
        self.assertEqual(self.bowler.stats.balls_bowled, 1)
        self.assertEqual(self.bowler.balls_bowled_count, 1)


class TestGameMechanics(unittest.TestCase):
    """Test game mechanics"""
    
    def test_delivery_effectiveness_returns_tuple(self):
        """Test delivery effectiveness returns correct tuple"""
        result = get_delivery_effectiveness(Delivery.FAST_BALL, Shot.DEFENSIVE)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], bool)
        self.assertIsInstance(result[1], str)
    
    def test_calculate_runs_for_duck(self):
        """Test no runs on duck"""
        runs = calculate_runs(Delivery.FAST_BALL, Shot.DUCK, True)
        self.assertEqual(runs, 0)
    
    def test_calculate_runs_unsuccessful(self):
        """Test no runs on unsuccessful shot"""
        runs = calculate_runs(Delivery.FAST_BALL, Shot.DEFENSIVE, False)
        self.assertEqual(runs, 0)
    
    def test_calculate_runs_defensive_successful(self):
        """Test runs on successful defensive shot"""
        runs = calculate_runs(Delivery.FAST_BALL, Shot.DEFENSIVE, True)
        self.assertIn(runs, [1, 2])


class TestStats(unittest.TestCase):
    """Test statistics tracking"""
    
    def test_stats_initialization(self):
        """Test stats are initialized correctly"""
        stats = Stats()
        self.assertEqual(stats.runs, 0)
        self.assertEqual(stats.wickets, 0)
        self.assertEqual(stats.balls_faced, 0)


if __name__ == '__main__':
    unittest.main()
