import os

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = os.environ.get("FIXTURE_DIR")
    loaddata_command = "loaddata"
    filenames = [
        "users",
        "ad",
        "comments",
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            print(os.path.join(self.fixtures_dir))
            call_command(
                self.loaddata_command, os.path.join(self.fixtures_dir, f"{fixture_filename}.json")
            )
