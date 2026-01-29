from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.username, 'testuser')

    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', activity_type='Run', duration=30, team='Test Team')
        self.assertEqual(activity.activity_type, 'Run')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user='testuser', team='Test Team', points=10)
        self.assertEqual(leaderboard.points, 10)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test Team')
        self.assertEqual(workout.name, 'Test Workout')
