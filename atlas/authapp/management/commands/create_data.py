from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from mainapp.models import Obj1Ai, Obj2Ai, Obj1Cmn, Obj2Cmn
from random import randrange, uniform, choice
import datetime as DT



def get_random():
    return randrange(1, 100)


def get_random_mode():
    return randrange(0, 1)


def get_random_ai():
    dict_ai = {
        111: 'Температура в помещении секция 1',
        112: "Температура в помещении секция 2",
        121: "Датчик вибрации площадки",
        131: "Датчик уровня шума",
        211: "Температура раствора в емкости №1",
        311: "Температура раствора в емкости №1",
        411: "Температура раствора в емкости №1",
        511: "Температура раствора в емкости №1",
        611: "Температура раствора в емкости №1",
        711: "Температура раствора в емкости №1",
        811: "Температура раствора в емкости №1",
        212: "Температура раствора в емкости №2",
        312: "Температура раствора в емкости №2",
        412: "Температура раствора в емкости №2",
        512: "Температура раствора в емкости №2",
        612: "Температура раствора в емкости №2",
        712: "Температура раствора в емкости №2",
        812: "Температура раствора в емкости №2",
        213: "Температура раствора в емкости №3",
        313: "Температура раствора в емкости №3",
        413: "Температура раствора в емкости №3",
        513: "Температура раствора в емкости №3",
        613: "Температура раствора в емкости №3",
        713: "Температура раствора в емкости №3",
        813: "Температура раствора в емкости №3",
        911: "Температура двигателя №1",
        912: "Температура двигателя №2",
        913: "Температура двигателя №3",
        914: "Температура двигателя №4",
        915: "Температура двигателя №5",
        916: "Температура двигателя №6",
        921: "Вибрация двигателя №1",
        922: "Вибрация двигателя №2",
        923: "Вибрация двигателя №3",
        924: "Вибрация двигателя №4",
        925: "Вибрация двигателя №5",
        926: "Вибрация двигателя №6",
        931: "Уровень шума"
    }
    ai_id, ai_name = choice(list(dict_ai.items()))
    return ai_id


def get_random_id_object():
    dict_obj = {
        1: 'Склад реагентов',
        2: "Фл камера Тюмень 1",
        3: "Фл камера Тюмень 3",
        4: "Фл камера ЯНАО 1",
        5: "Фл камера ЯНАО 2",
        6: "Фл камера Челябинск 1",
        7: "Фл камера Челябинск 2",
        8: "Фл камера Челябинск 3",
        9: "Двигатели подъемного механизма",
    }
    obj_id, obj_name = choice(list(dict_obj.items()))
    return obj_id


def get_random_err():
    dict_err = {
        0: "Система в норме",
        1: "Аварийная нижняя граница",
        2: "Предупредительная нижняя граница",
        3: "Предупредительная верхняя граница",
        4: "Аварийная верхняя граница"
    }
    err_id, err_name = choice(list(dict_err.items()))
    return err_id

def get_random_sts():
    dict_sts = {
        0: "Система в норме",
        1: "Не подтвержден",
        2: "Подтвержден"
    }
    sts_id, sts_name = choice(list(dict_sts.items()))
    return sts_id

class Command(BaseCommand):

    def handle(self, *args, **options):
        Obj1Ai.objects.all().delete()
        Obj2Ai.objects.all().delete()
        Obj1Cmn.objects.all().delete()
        Obj2Cmn.objects.all().delete()
        User.objects.all().delete()
        User.objects.all()
        Obj1Ai.objects.all()
        Obj2Ai.objects.all()
        Obj1Cmn.objects.all()
        Obj2Cmn.objects.all()

        start = DT.datetime(2021, 3, 25, 0, 0)
        end = DT.datetime.now()
        step = DT.timedelta(minutes=30)

        date = start

        users = [
            {'username': 'Atl', 'email': 'atl@gmail.com', 'password': 'PassWord11'},
            {'username': 'Cm001', 'email': 'Cm001@gmail.com', 'password': 'Pass12'},
            {'username': 'Cm002', 'email': 'Cm002@gmail.com', 'password': 'Pass13'},
        ]

        obj1Cmn = []
        for i in range(1, 600):
            obj1Cmn.append(
                {'idobj': get_random_id_object(),'user':'Cm001','user':'Atl', 'amount': 10, 'data': '10/05/2022', 'mode': 1, 'ai1': get_random(),
                 'ai2': get_random(),
                 'ai3': get_random(), 'ai4': get_random(), 'ai5': get_random(), 'ai6': get_random(),
                 'ai7': get_random(),
                 'ai8': get_random(), 'ai9': get_random(), 'ai10': get_random()}, )
        obj2Cmn = []
        for i in range(1, 600):
            obj2Cmn.append(
                {'idobj': get_random_id_object(),'user':'Cm002','user':'Atl', 'amount': 10, 'data': '10/05/2022', 'mode': 1, 'ai1': get_random(),
                 'ai2': get_random(),
                 'ai3': get_random(), 'ai4': get_random(), 'ai5': get_random(), 'ai6': get_random(),
                 'ai7': get_random(),
                 'ai8': get_random(), 'ai9': get_random(), 'ai10': get_random()}, )


        obj1Ai = []
        while date <= end:
            for i in range(1, 3):
                obj1Ai.append(
                    {'idobj': get_random_id_object(), 'idai': get_random_ai(), 'datain': str(date),
                     'mode': get_random_mode(),
                     'aimax': round(uniform(1.00, 100.00),2), 'aimean': round(uniform(1.00, 100.00),2), 'aimin': round(uniform(1.00, 100.00),2),
                     'statmin': round(uniform(1.00, 100.00),2),
                     'statmax': round(uniform(1.00, 100.00),2), 'mlmin': round(uniform(1.00, 100.00),2), 'mlmax': round(uniform(1.00, 100.00),2),
                     'err': get_random_err(),
                     'sts': get_random_sts(), 'dataout': '01/05/2023', 'datacheck': '10/05/2022', 'cmnt': 'test'}
                )
            date += step

        obj2Ai = []
        for l in range(1, 50):
            obj2Ai.append(
                {'idobj': get_random_id_object(), 'idai': get_random_ai(), 'datain': date,
                 'mode': get_random_mode(), 'aimax': round(uniform(1.00, 100.00),2),
                 'aimean': round(uniform(1, 100),2), 'aimin': round(uniform(1, 100),2), 'statmin': round(uniform(1, 100),2),
                 'statmax': round(uniform(1, 100),2), 'mlmin': round(uniform(1, 100),2),
                 'mlmax': round(uniform(1, 100),2), 'err': get_random_err(), 'sts': get_random_sts(), 'dataout': '01/05/2023',
                 'datacheck': '10/05/2022', 'cmnt': 'test'}
                )

        for item in users:
            User.objects.create_user(**item)

        for item in obj1Cmn:
            item['user'] = User.objects.get(username=item['user'])
            Obj1Cmn.objects.create(**item)

        for item in obj2Cmn:
            item['user'] = User.objects.get(username=item['user'])
            Obj2Cmn.objects.create(**item)

        for item in obj1Ai:
            Obj1Ai.objects.create(**item)

        for item in obj2Ai:
            Obj2Ai.objects.create(**item)

        # for item in projects:
        #     item['user'] = User_test.objects.get(username=item['user'])
        #     Project.objects.create(**item)

        # Group.objects.all().delete()

        # add_project = Permission.objects.get(codename='add_project')
        # change_project = Permission.objects.get(codename='change_project')
        # delete_project = Permission.objects.get(codename='delete_project')

        # add_user = Permission.objects.get(codename='add_user')
        # change_user = Permission.objects.get(codename='change_user')
        # delete_user = Permission.objects.get(codename='delete_user')

        # little_staff = Group.objects.create(name='Младшие сотрудники')

        # little_staff.permissions.add(add_project)
        # little_staff.permissions.add(change_project)
        # little_staff.permissions.add(delete_project)

        # big_staff = Group.objects.create(name='Старшие сотрудники')

        # big_staff.permissions.add(add_project)
        # big_staff.permissions.add(change_project)
        # big_staff.permissions.add(delete_project)

        # big_staff.permissions.add(add_user)
        # big_staff.permissions.add(change_user)
        # big_staff.permissions.add(delete_user)

        # little = User.objects.create_user('little','little@little.com','little12345')
        # little.groups.add(little_staff)
        # little.save()

        # big = User.objects.create_user('big','big@big.com','big123456')
        # big.groups.add(big_staff)
        # big.save()

        print('done')
