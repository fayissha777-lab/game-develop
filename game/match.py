"""Match logic for cricket game"""

from game.player import Batsman, Bowler
from game.utils import Delivery, Shot, get_user_choice, get_delivery_effectiveness, calculate_runs, get_out_probability


class Match:
    """Cricket match handler"""
    
    def __init__(self, batsman_name: str, bowler_name: str, overs: int = 1):
        """
        Initialize a match
        
        Args:
            batsman_name: Name of batsman
            bowler_name: Name of bowler
            overs: Number of overs (default 1 over = 6 balls)
        """
        self.batsman = Batsman(batsman_name)
        self.bowler = Bowler(bowler_name)
        self.total_balls = overs * 6
        self.balls_bowled = 0
        self.match_active = True
        
    def display_scorecard(self):
        """Display current match scorecard"""
        print("\n" + "="*50)
        print(f"{'SCORECARD':^50}")
        print("="*50)
        print(f"{self.batsman.name}: {self.batsman.stats.runs} runs ({self.batsman.stats.balls_faced} balls)")
        print(f"  Fours: {self.batsman.stats.fours} | Sixes: {self.batsman.stats.sixes}")
        print(f"{self.bowler.name}: {self.bowler.stats.wickets} wickets ({self.bowler.stats.balls_bowled} balls)")
        print(f"Balls remaining: {self.total_balls - self.balls_bowled}")
        print("="*50)
        
    def play_ball(self) -> bool:
        """
        Play a single ball
        
        Returns:
            True if match continues, False if match ends
        """
        self.balls_bowled += 1
        print(f"\n--- Ball {self.balls_bowled} ---")
        
        # Bowler chooses delivery
        delivery_choice = get_user_choice(
            {
                "1": "Fast Ball",
                "2": "Spin",
                "3": "Yorker",
                "4": "Bouncer"
            },
            f"{self.bowler.name}, what will you bowl?"
        )
        
        delivery_map = {
            "1": Delivery.FAST_BALL,
            "2": Delivery.SPIN,
            "3": Delivery.YORKER,
            "4": Delivery.BOUNCER
        }
        delivery = delivery_map[delivery_choice]
        print(f"🎳 {self.bowler.name} bowls a {delivery.value}!")
        
        # Batsman chooses shot
        shot_choice = get_user_choice(
            {
                "1": "Defensive Shot (Safe but low runs)",
                "2": "Aggressive Shot (Risky but high runs)",
                "3": "Duck (Avoid the ball)"
            },
            f"{self.batsman.name}, how will you respond?"
        )
        
        shot_map = {
            "1": Shot.DEFENSIVE,
            "2": Shot.AGGRESSIVE,
            "3": Shot.DUCK
        }
        shot = shot_map[shot_choice]
        print(f"🏏 {self.batsman.name} plays a {shot.value}!")
        
        # Determine outcome
        is_successful, message = get_delivery_effectiveness(delivery, shot)
        print(f"\n➜ {message}")
        
        # Calculate runs or out
        if is_successful:
            runs = calculate_runs(delivery, shot, is_successful)
            if runs > 0:
                self.batsman.score_runs(runs)
                print(f"✓ {runs} runs! Total: {self.batsman.stats.runs} runs")
            else:
                self.batsman.add_failure()
                print(f"• Dot ball! Total: {self.batsman.stats.runs} runs")
                self.bowler.add_dot()
        else:
            # Check if batsman gets out
            if get_out_probability(delivery, shot, is_successful):
                self.batsman.get_out()
                self.bowler.take_wicket()
                print(f"\n🔴 WICKET! {self.batsman.name} is OUT!")
                print(f"   Bowled by: {self.bowler.name}")
                return False
            else:
                self.batsman.add_failure()
                print(f"• Missed it but survived!")
                
                # Check if 3 consecutive failures
                if self.batsman.consecutive_failures >= 3:
                    print(f"\n⚠️  Three consecutive failures! {self.batsman.name} is OUT!")
                    self.bowler.take_wicket()
                    return False
        
        # Check if match ends
        if self.balls_bowled >= self.total_balls:
            return False
            
        return True
    
    def play_match(self):
        """Play the complete match"""
        print("\n" + "🏏 "*20)
        print(f"{'CRICKET GAME STARTED':^40}")
        print(f"Match: {self.batsman.name} vs {self.bowler.name}")
        print(f"Overs: {self.total_balls // 6}")
        print("🏏 "*20 + "\n")
        
        while self.match_active and self.balls_bowled < self.total_balls:
            self.display_scorecard()
            self.match_active = self.play_ball()
        
        # Display final scorecard
        self.display_final_scorecard()
    
    def display_final_scorecard(self):
        """Display final match statistics"""
        print("\n" + "="*50)
        print(f"{'MATCH SUMMARY':^50}")
        print("="*50)
        
        if self.batsman.is_out:
            print(f"❌ {self.batsman.name} is OUT")
        else:
            print(f"✅ {self.batsman.name} remains NOT OUT")
        
        print(f"\n📊 BATTING STATISTICS:")
        print(f"  Total Runs: {self.batsman.stats.runs}")
        print(f"  Balls Faced: {self.batsman.stats.balls_faced}")
        print(f"  Fours: {self.batsman.stats.fours}")
        print(f"  Sixes: {self.batsman.stats.sixes}")
        if self.batsman.stats.balls_faced > 0:
            strike_rate = (self.batsman.stats.runs / self.batsman.stats.balls_faced) * 100
            print(f"  Strike Rate: {strike_rate:.2f}")
        
        print(f"\n🎳 BOWLING STATISTICS:")
        print(f"  Wickets: {self.bowler.stats.wickets}")
        print(f"  Balls Bowled: {self.bowler.stats.balls_bowled}")
        print(f"  Economy: {(self.bowler.stats.balls_bowled / self.bowler.stats.wickets) if self.bowler.stats.wickets > 0 else 'N/A'}")
        
        if self.batsman.is_out:
            print(f"\n🏆 RESULT: {self.bowler.name} wins!")
        else:
            if self.batsman.stats.runs > 12:
                print(f"\n🏆 RESULT: {self.batsman.name} wins!")
            else:
                print(f"\n🏆 RESULT: Close match!")
        
        print("="*50 + "\n")
