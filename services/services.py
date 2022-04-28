import csv
from .models import ServiceType, ServiceSuggestion, ServiceGallery, ServicePhoto
from django.contrib.auth import authenticate

READ_ONLY = "r"

WRITE_ONLY = "w"

DELIMETER_SEMICOLON = ";"

CSV_FOLDER = "csv_media/csv/"

PATH_IMAGE = 'http://localhost:8000/media/'


def _get_csv_path(filename):
    return f"{CSV_FOLDER}{filename}"

def service_save(row):
    service_data = {}
    suggestions_data = []
    if row['suggestions']:
        for sug in row['suggestions'].split(','):
            new_sug = ServiceSuggestion.objects.filter(title=sug).last()
            if new_sug:
                suggestions_data.append(new_sug)
            else:
                new_sug = ServiceSuggestion.objects.create(title=sug)
                suggestions_data.append(new_sug)
    
    # if row['contacts']:
    #     for contact in row['contacts']:
    #         new_user = authenticate(username=contact[0], first_name=contact[0], last_name=contact[1], phone=contact[2])
            
    if row['type']:
        pass


    new_service = ServiceType.objects.create(title=row[''])
    gallery = ServiceGallery.objects.filter(service=new_service).last()
    # PATH_IMAGE


def csv_import(filename):
    with open(_get_csv_path(filename), READ_ONLY, encoding="utf-8") as f:
        fieldnames = [
            "title",
            "contacts",
            "time",
            "price",
            "warranty",
            "text",
            "suggestions",
            "type",
            "images"
        ]
        reader = csv.DictReader(
            f, fieldnames=fieldnames, delimiter=DELIMETER_SEMICOLON
        )
        for i, row in enumerate(reader):
            if i != 0:
                service_save(row)


def _get_contacts_value(service):
    return [t for t in service.contacts.all().values_list('first_name', 'last_name', 'phone')]

def _get_images_value(service):
    return ",".join(service.gallery.images.all().values_list('image', flat=True))

def _get_suggestions_value(service):
    return ",".join(service.suggestions.all().values_list('title', flat=True))

field_managers = {
    "contacts": _get_contacts_value,
    "images": _get_images_value,
    "suggestions": _get_suggestions_value,
}

def _get_service_field_values(service, service_fields):
    field_values = {}
    for field in service_fields:
        if field in field_managers.keys():
            value = field_managers[field](service)
            field_values[field] = value
        else:
            value = getattr(service, field)
            field_values[field] = value
    return field_values





def writer(file, services, service_fields):
    fields = ["#"] + service_fields
    writer = csv.DictWriter(file, delimiter=DELIMETER_SEMICOLON, fieldnames=fields)
    writer.writeheader()
    for row_number, service in enumerate(services):
        field_values_dict = {'#': row_number}
        field_values_dict.update(_get_service_field_values(service, service_fields))
        writer.writerow(field_values_dict)
    return file

def csv_export(filename):
    services = ServiceType.objects.all()
    fields = [
        "title",
        "contacts",
        "time",
        "price",
        "warranty",
        "text",
        "suggestions",
        "type",
        "images"
    ]
    with open(_get_csv_path(filename), WRITE_ONLY, encoding="utf-8") as file:
        file = writer(file, services, fields)
        return file