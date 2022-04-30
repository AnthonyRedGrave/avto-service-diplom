from django.core.management.base import BaseCommand
from services.services import csv_export


class Command(BaseCommand):
    help = "CSV-export for thing objects"

    def add_arguments(self, parser):
        parser.add_argument("--f", "--filename",type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['f']
        if filename is None:
            filename = 'export.csv'
        csv_export(filename)