from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        self.activity = Activity.objects.create(user=self.user, type='Cardio', duration=30, date='2025-12-23')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100, rank=1)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertTrue(self.user.is_superhero)

    def test_team_membership(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Cardio')
        self.assertEqual(self.activity.duration, 30)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Web Swing')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
        self.assertEqual(self.leaderboard.rank, 1)
