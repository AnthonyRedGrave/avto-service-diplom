from django.core.management.base import BaseCommand
from services.services import csv_import
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "CSV-import for thing objects"

    def add_arguments(self, parser):
        parser.add_argument("--f", "--filename",type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['f']
        if filename is None:
            filename = 'import.csv'
        logger.info("Импорт записей как management комманда в файл", {'filename': filename})
        csv_import(filename)