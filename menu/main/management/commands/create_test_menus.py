from django.core.management.base import BaseCommand
from main.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Создание тестовый записей в БД'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        MenuItem.objects.all().delete()
        Menu.objects.all().delete()

        # Создаем первое меню
        menu1 = Menu.objects.create(name='Main Menu')

        # Создаем элементы первого меню
        main_item1 = MenuItem.objects.create(
            menu=menu1,
            name='Home',
            slug='home'
        )
        main_item2 = MenuItem.objects.create(
            menu=menu1,
            name='About',
            slug='about'
        )

        # Создаем подменю для первого меню
        sub_item1 = MenuItem.objects.create(
            menu=menu1,
            name='Team',
            slug='team',
            parent=main_item2
        )
        sub_item2 = MenuItem.objects.create(
            menu=menu1,
            name='History',
            slug='history',
            parent=main_item2
        )

        # Создаем вложенные пункты для подменю
        sub_sub_item1 = MenuItem.objects.create(
            menu=menu1,
            name='Member 1',
            slug='member1',
            parent=sub_item1
        )
        sub_sub_item2 = MenuItem.objects.create(
            menu=menu1,
            name='Member 2',
            slug='member2',
            parent=sub_item1
        )

        # Создаем второе меню
        menu2 = Menu.objects.create(name='Footer Menu')

        # Создаем элементы второго меню
        footer_item1 = MenuItem.objects.create(
            menu=menu2,
            name='Privacy Policy',
            slug='privacy-policy'
        )
        footer_item2 = MenuItem.objects.create(
            menu=menu2,
            name='Terms of Service',
            slug='terms-of-service'
        )

        # Создаем подменю для второго меню
        footer_sub_item1 = MenuItem.objects.create(
            menu=menu2,
            name='Contact Us',
            slug='contact-us',
            parent=footer_item2
        )
        footer_sub_item2 = MenuItem.objects.create(
            menu=menu2,
            name='FAQ',
            slug='faq',
            parent=footer_item2
        )

        # Создаем вложенные пункты для подменю второго меню
        footer_sub_sub_item1 = MenuItem.objects.create(
            menu=menu2,
            name='Email Us',
            slug='email',
            parent=footer_sub_item1
        )
        footer_sub_sub_item2 = MenuItem.objects.create(
            menu=menu2,
            name='Call Us',
            slug='call',
            parent=footer_sub_item1
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Пункты меню успешно создан'
            )
        )
