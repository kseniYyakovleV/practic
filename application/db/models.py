from django.db import models
import os



class Element(models.Model):
    #Номер
    number = models.IntegerField(primary_key=True)
    #Проиводитель
    manufacturer = models.TextField(null = True)
    #Оборудование
    equipment = models.TextField(null = True)
    #Тип Запасная часть\расходный материал\масла смазки
    SPARE_PART = 'sp'
    CONSEMABLES = 'c'
    LUBRICATING_OILS = 'lo'
    Types = [
        (SPARE_PART, 'Запасная часть'),
        (CONSEMABLES, 'Расходный материал'),
        (LUBRICATING_OILS, 'Масла смазки')
    ]

    type = models.TextField(choices = Types, 
                            default = SPARE_PART,
                            null = None)

    #Название
    name = models.TextField(null = True)
    #Аналог
    analog = models.TextField(null = True, default="Нет")
    #Номер SAP
    SAP_number = models.TextField(null = True)
    #Серийный номер
    serial_number = models.TextField(null = True)
    #Номер полки
    storage = models.TextField(null = True)
    #Единицы
    unit = models.TextField(null = True)
    #Время доставки
    delivery_time = models.FloatField(null = True)
    #Время использования
    using_time = models.FloatField(null = True)
    #Время простоя
    downtime = models.FloatField(null = True)
    #Время доставки и коэффициент
    delivery_time_and_coefficient = models.FloatField(null = True)
    #Используется в цеху
    using_in_workshop = models.FloatField(null = True)
    #Цена в рублях
    price_in_rubles = models.FloatField(null = True)
    #Количество
    count = models.FloatField(null = True)
    #Заказано
    ordered = models.FloatField(null = True, default = 0)
    #Минимаольное фактическое
    min_fact = models.FloatField(null = True)
    #Максимальное фактическое
    max_fact = models.FloatField(null = True)
    #Изображение
    image = models.TextField(null = True, default=None)

    


    def delete(self):
        image = self.image
        count_elements_with_this_image = Element.objects.filter(image=image).__len__()
        if count_elements_with_this_image<=1:
            os.remove(os.path.abspath("db/files/images/xl/media")+"/"+image)
        print(image,"was removed")
        super().delete()


    def get_all_data_of_one_element(self):
        try:
            delivery_time_coefficient = self.delivery_time*0.25
        except TypeError:
            delivery_time_coefficient = None

        try:
            using_time_coefficient = self.using_time*0.25
        except TypeError:
            using_time_coefficient = None

        try:
            downtime_coefficient = self.downtime*0.5
        except TypeError:
            downtime_coefficient = None

        try:
            min_cof = delivery_time_coefficient*using_time_coefficient*downtime_coefficient
        except TypeError:
            min_cof = None

        try:
            delivery_time_and_coefficient_coefficient = self.delivery_time_and_coefficient*0.3
        except TypeError:
            delivery_time_and_coefficient_coefficient = None

        try:
            using_in_workshop_coefficient = self.using_in_workshop*0.
        except TypeError:
            using_in_workshop_coefficient = None

        try:
            if self.price_in_rubles>=500000:
                price_coefficient = 1
            elif self.price_in_rubles>=100000:
                price_coefficient = 2
            elif self.price_in_rubles>=50000:
                price_coefficient = 3
            elif self.price_in_rubles>=10000:
                price_coefficient = 4
            elif self.price_in_rubles>=8000:
                price_coefficient = 5
            elif self.price_in_rubles>=5000:
                price_coefficient = 6
            elif self.price_in_rubles>=3000:
                price_coefficient = 7
            elif self.price_in_rubles>=1000:
                price_coefficient = 8
            elif self.price_in_rubles>=500:
                price_coefficient = 9
            elif self.price_in_rubles>=100:
                price_coefficient = 10
            else:
                price_coefficient = 0
        except TypeError:
            price_coefficient = None

        try:
            price_coefficient_coefficient = price_coefficient*0.6
        except TypeError:
            price_coefficient_coefficient = None

        try:
            max_cof = delivery_time_and_coefficient_coefficient*using_in_workshop_coefficient*price_coefficient_coefficient
        except TypeError:
            max_cof = None

        try:
            if min_cof>=28:
                min_calc = 8
            elif min_cof>=24:
                min_calc = 7
            elif min_cof>=20:
                min_calc = 6
            elif min_cof>=16:
                min_calc = 5
            elif min_cof>=12:
                min_calc = 4
            elif min_cof>=8:
                min_calc = 3
            elif min_cof>=4:
                min_calc = 2
            elif min_cof>=1:
                min_calc = 1
            else:
                min_calc = 0
        except TypeError:
            min_calc = None

        try:
            if max_cof>=18:
                max_calc = 20
            elif max_cof>=15:
                max_calc = 17
            elif max_cof>=11:
                max_calc = 15
            elif max_cof>=9:
                max_calc = 13
            elif max_cof>=7:
                max_calc = 11
            elif max_cof>=5:
                max_calc = 9
            elif max_cof>=3:
                max_calc = 7
            elif max_cof>=1:
                max_calc = 5
            else:
                max_calc = 3
        except TypeError:
            max_calc = None

        return {
            self.number: {
            "manufacturer": self.manufacturer, "equipment": self.equipment, "analog": self.analog,
            "type": self.type, "name": self.name, "SAP_number": self.SAP_number,
            "serial_number": self.serial_number, "storage": self.storage, "unit": self.unit,
            "delivery_time": self.delivery_time, "using_time": self.using_time,
            "downtime": self.downtime, "delivery_time_and_coefficient": self.delivery_time_and_coefficient,
            "using_in_workshop": self.using_in_workshop, "price_in_rubles": self.price_in_rubles,
            "count": self.count, "ordered": self.ordered, "min_fact": self.min_fact,
            "min_calc": min_calc, "max_fact": self.max_fact, "max_calc": max_calc, "image": self.image}
        }
    
    
    def is_valid(atr):
            if atr==0 or atr==None or atr=="":
                return False
            return True
    

    def is_valid_for_excel(self, name=True, image=True, type=True, 
                           manufacturer=True, analog=True, unit=True,
                           min=True, ordered=True, count=True, price_in_rubles=True):
        response = True
        is_valid = Element.is_valid
        
        response*=not (name and not is_valid(self.name))
        response*=not (image and not is_valid(self.image))
        response*=not (ordered and not is_valid(self.ordered))
        response*=not (type and not is_valid(self.type))
        response*=not (manufacturer and not is_valid(self.manufacturer))
        response*=not (analog and not is_valid(self.analog))
        response*=not (unit and not is_valid(self.unit))
        response*=not (min and not is_valid(self.min))
        response*=not (count and not is_valid(self.count))
        response*=not (price_in_rubles and not is_valid(self.price_in_rubles))
        return response


    def is_full_valid(self, manufacturer = True, equipment = True, analog = True, 
            type = True, name = True, SAP_number = True, serial_number = True, 
            storage = True, unit = True, delivery_time = True, using_time = True, 
            downtime = True, delivery_time_and_coefficient = True, 
            using_in_workshop = True, price_in_rubles = True, count = True, 
            ordered = True, min_fact = True, max_fact = True, image = True):
        
        response = self.is_valid_for_excel(name, image, type, manufacturer, analog, unit, 
                                           min, ordered, count, price_in_rubles)


        is_valid = Element.is_valid
        
        response*=not (equipment and not is_valid(self.equipment))
        response*=not (SAP_number and not is_valid(self.SAP_number))
        response*=not (serial_number and not is_valid(self.serial_number))
        response*=not (storage and not is_valid(self.storage))
        response*=not (delivery_time_and_coefficient and not is_valid(self.delivery_time_and_coefficient))
        response*=not (using_time and not is_valid(self.using_time))
        response*=not (downtime and not is_valid(self.downtime))
        response*=not (delivery_time and not is_valid(self.delivery_time))
        response*=not (using_in_workshop and not is_valid(self.using_in_workshop))
        response*=not (min_fact and not is_valid(self.min_fact))
        response*=not (max_fact and not is_valid(self.max_fact))
            
        return response


    def get_not_valid_for_excel_objects_data(name=True, image=True, type=True, manufacturer=True, 
                                        analog=True, unit=True, min=True, ordered=True, count=True):
        
        elements = Element.objects.all()
        list = [element for element in elements if not element.is_valid_for_excel(name, image, type, manufacturer, analog, unit, min, ordered, count)]
        response = dict()

        for element in list:
            response[element.number] = {"manufacturer": element.manufacturer, "equipment": element.equipment,
                    "analog": element.analog, "type": element.type, "name": element.name,
                    "SAP_number": element.SAP_number, "serial_number": element.serial_number,
                    "storage": element.storage, "unit": element.unit, "delivery_time": element.delivery_time,
                    "using_time": element.using_time, "downtime": element.downtime,
                    "delivery_time_and_coefficient": element.delivery_time_and_coefficient,
                    "using_in_workshop": element.using_in_workshop, "price_in_rubles": element.price_in_rubles,
                    "count": element.count, "ordered": element.ordered, "min_fact": element.min_fact,
                    "max_fact": element.max_fact, "image": element.image }
        
        return response
    

    def get_valid_for_excel_objects_data(name=True, image=True, type=True, manufacturer=True, 
                                    analog=True, unit=True, min=True, ordered=True, count=True):
        
        elements = Element.objects.all()
        list = [element for element in elements if element.is_valid_for_excel(name, image, type, manufacturer, analog, unit, min, ordered, count)]
        response = dict()

        for element in list:
            response[element.number] = {"manufacturer": element.manufacturer, "equipment": element.equipment,
            "analog": element.analog, "type": element.type, "name": element.name, "SAP_number": element.SAP_number,
            "serial_number": element.serial_number, "storage": element.storage, "unit": element.unit,
            "delivery_time": element.delivery_time, "using_time": element.using_time, "downtime": element.downtime,
            "delivery_time_and_coefficient": element.delivery_time_and_coefficient, "using_in_workshop": element.using_in_workshop,
            "price_in_rubles": element.price_in_rubles, "count": element.count, "ordered": element.ordered, "min_fact": element.min_fact,
            "max_fact": element.max_fact, "image": element.image}
        
        return response


    def get_all_data_of_all_elements(objects=None):
        if objects==None:
            objects = Element.objects.all()
        all_data = dict()

        for object in objects:
            object = object.get_all_data_of_one_element()
            all_data[list(object.keys())[0]] = list(object.values())[0]
        return all_data
    

    def get_free_number():
        objects = [int(*i) for i in sorted(Element.objects.values_list("number"))]

        for number in range(1, len(objects)+1):
            if number not in objects:
                return number
        return number+1
    


class User(models.Model):
    login = models.TextField(primary_key=True)
    password = models.TextField()
    #Тип Запасная часть\расходный материал\масла смазки
    USER = 'u'
    MASTER = 'm'
    Types = [
        (USER, 'Пользователь'),
        (MASTER, 'Руководитель')
    ]
    type = models.TextField(choices = Types, 
                            default = USER,
                            null = False)
    added_elements = models.ManyToManyField(
        Element,
        through="Addings",
        related_name="added_elements"
    )

    count_changing_elements = models.ManyToManyField(
        Element, 
        through="Count_changings",
        related_name="count_changing_elements"
    )


    def get_all_users():
        users = User.objects.all()
        response = dict()
        for user in users:
            response[user.id] = dict(login = user.login,
                                     password = user.password,
                                     type = user.type)
        return response
    


class Addings(models.Model):
    added_element = models.ForeignKey(Element, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField()


    
    def get_all_addings():
        all_added_elements = Addings.objects.all()
        response = dict()
        for element in all_added_elements:
            response[element.id] = dict(element = element.added_element, user = element.user, 
                                        datetime = element.datetime)
        return response
    


class Count_changings(models.Model):
    changed_element = models.ForeignKey(Element, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField()
    count_changing = models.FloatField()