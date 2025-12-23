from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)
        users = list(User.objects.all())

        # Create workouts
        workout1 = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        workout2 = Workout.objects.create(name='Flight', description='Flying workout')
        workout1.suggested_for.set(users)
        workout2.suggested_for.set(users)

        # Create activities
        for user in users:
            Activity.objects.create(user=user, type='Cardio', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, type='Strength', duration=45, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=200, rank=1)
        Leaderboard.objects.create(team=dc, points=150, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
