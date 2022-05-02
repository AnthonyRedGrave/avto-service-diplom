from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from services.models import ServiceType, ServiceSuggestion

User = get_user_model()

USER_CREDENTIALS = [
            ('Константин', 'Титов', '+37533123456'),
            ('Валентин', 'Валентинов', '+37533123455'),
            ('Георгий', 'Георгиев', '+37533123454'),
            ('Василий', 'Василь', '+37533123453'),
            ('Дмитрий', 'Дмитриев', '+37533123452'),
            ('Александр', 'Александров', '+37533123451'),
        ]

SERVICE_INFOS = [
    ('Диагностика и ремонт Webasto', 'repair', '60 минут', 60, '6 месяцев', 'Это оборудование максимально'
        ' надежно, оно имеет множество степеней защиты. А из строя выходит, как правило,'
        ' из-за неправильной эксплуатации или неисправности бортовой сети.',
     [
        'Диагностика Webasto',
        'Ремонт Webasto',
        'Консультации по управлению Webasto',
        'Установка Webasto на грузовые автомобили',
        'Ремонт и заправка автомобильных кондиционеров'
    ]),
    ('Автостекла для легковых и грузовых автомобилей', 'service', '55 минут', 38, '6 месяцев',
     'Наша компания является официальным дилером компании «КМК Glass» одного из лидеров в сфере'
     ' производства автомобильного стекла. Совершенно не обязательно переплачивать за оригинальное стекло для'
     ' Вашего автомобиля. Мы с радостью предложим Вам недорогое, качественное автомобильное стекло.',
     [
            'Установка автостекол',
            'Ремонт сколов',
            'Остановка трещин',
            'Установка мини-инжектора',
            'Полимеризация',
            'Очистка остатков полимера'
    ]),
    ('Автоэлектрика', 'electric', 'от 45 минут', 20, '6 месяцев', 'Электрооборудование автомобиля – группа'
      ' деталей, обеспечивающих электропитанием все узлы и агрегаты авто. В систему электрооборудования входят'
      ' стартер, система зажигания, генератор, системы впрыска и освещения. Эти и некоторые другие детали'
      ' потребляют электроэнергию, производимую аккумулятором и генератором. Если выходит из строя любой из'
      ' этих узлов или деталей, нарушается движение автомобиля, а иногда происходит'
      ' и полная остановка транспортного средства.',
     [
            'Компьютерная диагностика на дилерском оборудовании',
            'Сброс ошибок',
            'Исправление неполадок в системе наружного освещения и световой сигнализации',
            'Ремонт и замена блоков управления, комфорта и т.д',
            'Удаление сажевого фильтра FAP/DPF',
            'Удаление клапана ЕГР',
            'Ремонт генератора и стартера',
            'Ремонт и замена системы зажигания',
            'Чистка бензиновых форсунок на стенде',
            'Ремонт и замена иммобилайзеров'
    ])
]


def get_or_create_user(user_data):
    user, created = User.objects.get_or_create(username=user_data[0],
                                               first_name=user_data[0],
                                               last_name=user_data[1],
                                               phone=user_data[2])
    return user


def create_service(service_data, user_1, user_2):
    service = ServiceType.objects.create(title=service_data[0],
                                         type=service_data[1],
                                         time=service_data[2],
                                         price=f'{str(service_data[3])} б.р.',
                                         price_int=service_data[3],
                                         warranty=service_data[4])
    service.preview_text = service_data[5]
    service.save()
    for sug in service_data[6]:
        suggestion = ServiceSuggestion.objects.create(title=sug)
        service.suggestions.add(suggestion)
    service.save()
    service.contacts.add(user_1)
    service.contacts.add(user_2)
    service.save()


class Command(BaseCommand):
    help = "Populates db with data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Started database population process...'))
        users = []
        # Создание юзеров
        for user_data in USER_CREDENTIALS:
            users.append(get_or_create_user(user_data))

        # Создание сервисов и галерей к ним
        for index, service_data in enumerate(SERVICE_INFOS):
            create_service(service_data, users[index], users[index+1])

        self.stdout.write(self.style.SUCCESS('Database population process has been ended...'))
