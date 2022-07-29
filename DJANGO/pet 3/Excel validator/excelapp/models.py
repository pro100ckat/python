from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import FileExtensionValidator
from django.core.files.storage import FileSystemStorage
import os
from untitled import settings


#Модель направление
class Napravlenie(models.Model):
    napravlenie_id = models.AutoField(primary_key=models.ProtectedError)
    napravlenie_shifr = models.CharField(max_length=50, default=0)
    napravlenie_name = models.CharField(max_length=50)
    profil = models.CharField(max_length=100)
    kvalification = models.CharField(max_length=50)
    nomer_fgos = models.IntegerField(validators=[MinValueValidator(1)])
    napravlenie_date = models.DateField()

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направление"

    def __str__(self):
        return self.napravlenie_name

#Модель учебные планы
class UchPlan(models.Model):
    uchPlan_id = models.AutoField(primary_key=models.ProtectedError)
    uchPlan_shifr = models.CharField(max_length=50, default=0)
    god_start = models.DateField()
    protocol = models.IntegerField(validators=[MinValueValidator(1)])
    date_protocol = models.DateField()
    uchPlan_kafedra = models.CharField(max_length=50)
    uchplan_profil = models.CharField(max_length=50)
    facultet = models.CharField(max_length=50)
    id_napravlenie = models.ForeignKey(Napravlenie, on_delete=models.PROTECT,  related_name="napravlenie")

    class Meta:
        verbose_name = "Учебный план"
        verbose_name_plural = "Учебныеt планы"

    def __str__(self):
        return self.uchPlan_shifr

#Модель виды деятельности
class Vidy_deyt(models.Model):
    Vidy_deyt_id = models.AutoField(primary_key=models.ProtectedError)
    Vidy_deyt_name = models.CharField(max_length=50)
    id_napravlenie = models.ForeignKey(Napravlenie, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Вид деятельности"
        verbose_name_plural = "Виды деятельности"
    def __str__(self):
        return self.Vidy_deyt_name

#Модель виды деятельности-учпланы
class UchPlanVidydeyt(models.Model):
    UchPlanVidydeyt_id = models.AutoField(primary_key=models.ProtectedError)
    UchPlanVidydeyt_shifr = models.ForeignKey(UchPlan, on_delete=models.PROTECT)
    UchPlanVidydeyt_vidydeyt = models.ForeignKey(Vidy_deyt, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Уч.пдан-Виды деят"
        verbose_name_plural = "Уч.План-Виды деят"

#Модель Практики
class Praktiki(models.Model):
    praktiki_id = models.AutoField(primary_key=models.ProtectedError)
    praktiki_name = models.CharField(max_length=50)
    praktiki_id_uchPlan = models.ForeignKey(UchPlan, on_delete=models.PROTECT, default="",  related_name="prictiki_uchplan")
    date_start = models.DateField()
    date_finish = models.DateField()

    class Meta:
        verbose_name = "Практика"
        verbose_name_plural = "Практики"
    def __str__(self):
        return self.praktiki_name

#Модель cроки прохождения практики
class Sroki(models.Model):
    sroki_id = models.AutoField(primary_key=models.ProtectedError)
    sroki_semestr = models.IntegerField(validators=[MinValueValidator(1)])
    id_praktiki = models.ForeignKey(Praktiki, on_delete=models.PROTECT, default="")


    class Meta:
        verbose_name = "Сроки"
        verbose_name_plural = "Сроки"

#Модель Компетенции
class Compititions(models.Model):
    compititions_id = models.AutoField(primary_key=models.ProtectedError)
    compititions_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Компетенции"
        verbose_name_plural = "Компетенции"
    def __str__(self):
        return self.compititions_name

#Модель Кафедра
class Kafedra(models.Model):
    kafedra_id = models.AutoField(primary_key=models.ProtectedError)
    kafedra_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедра"

    def __str__(self):
        return self.kafedra_name

#Модель Вид контроля
class Vid_control(models.Model):
    vid_control_id = models.AutoField(primary_key=models.ProtectedError)
    vid_control_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Вид контроля"
        verbose_name_plural = "Вид контроля"
    def __str__(self):
        return self.vid_control_name

#Модель Преподаватель
class Prepod(models.Model):
    prepod_id = models.AutoField(primary_key=models.ProtectedError)
    fam = models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    otchestvo= models.CharField(max_length=50)
    zvanie= models.CharField(max_length=50)
    uch_step= models.CharField(max_length=50)
    doljnost= models.CharField(max_length=50)
    date_izbran= models.DateField()
    prepod_kafedra= models.CharField(max_length=50)
    facultet= models.CharField(max_length=50)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватель"
    def __str__(self):
        return self.fam

#Модель Дисциплины
class Discipline(models.Model):
    discipline_id = models.AutoField(primary_key=models.ProtectedError)
    discipline_shifr = models.IntegerField(validators=[MinValueValidator(1)])
    disc_index = models.CharField(max_length=50)
    ZET = models.IntegerField(validators=[MinValueValidator(1)])
    id_kafedra = models.ForeignKey(Kafedra, on_delete=models.PROTECT,  related_name="kafedra")
    id_uchPlan = models.ForeignKey(UchPlan, on_delete=models.PROTECT, related_name="uchPlan")
    id_prepod = models.ForeignKey(Prepod, on_delete=models.PROTECT,  related_name="prepod")
    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
    def __str__(self):
        return str(self.discipline_shifr)

#Модель Формы контроля
class Form_cotrol(models.Model):
    form_cotrol_id = models.AutoField(primary_key=models.ProtectedError)
    form_cotrol_semestr = models.IntegerField(validators=[MinValueValidator(1)])
    id_discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT,   related_name="discipline")
    id_vid_control = models.ForeignKey(Vid_control, on_delete=models.PROTECT,  related_name="vid_control")
    class Meta:
        verbose_name = "Формы контроля"
        verbose_name_plural = "Формы контроля"

    def __str__(self):
        return self.form_cotrol_id
#Модель Часы
class Clocks(models.Model):
    clocks_id = models.AutoField(primary_key=models.ProtectedError)
    clocks_id_discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT, related_name="discipline_clocks")
    lections = models.IntegerField(validators=[MinValueValidator(1)])
    lab = models.IntegerField(validators=[MinValueValidator(1)])
    practics = models.IntegerField(validators=[MinValueValidator(1)])
    ksr = models.IntegerField(validators=[MinValueValidator(1)])
    srs = models.IntegerField(validators=[MinValueValidator(1)])
    control = models.IntegerField(validators=[MinValueValidator(1)])
    class Meta:
        verbose_name = "Часы"
        verbose_name_plural = "Часы"
    def __str__(self):
        return self.clocks_id
#Модель Норму времени учебной работы
class Normi(models.Model):
    normi_id = models.AutoField(primary_key=models.ProtectedError)
    vid_rabot = models.CharField(max_length=50)
    normi_chas = models.FloatField(validators=[MinValueValidator(1)])
    primechanie = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Нормы времени учебной работы"
        verbose_name_plural = "Нормы времени учебной работы"

    def __str__(self):
        return self.normi_id
 #Модель группа
class Group(models.Model):
    group_id = models.AutoField(primary_key=models.ProtectedError)
    group_number = models.CharField(max_length=50, default=1)
    institut = models.IntegerField(validators=[MinValueValidator(1)])
    forma_obuch = models.CharField(max_length=10)
    kolvochel = models.IntegerField(validators=[MinValueValidator(1)])
    yslovie = models.CharField(max_length=50)
    normativy = models.CharField(max_length=50)
    group_id_napravlenie = models.ForeignKey(Napravlenie, on_delete=models.PROTECT, related_name="group_napravlenie")
    group_id_uchPlan = models.ForeignKey(UchPlan, on_delete=models.PROTECT, related_name="group_uchPlan")
    # discipline = models.ManyToManyField(Discipline, related_name="discipline_group",)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группа"

    def __str__(self):
        return self.group_number

#Модель УМК
class Ymk(models.Model):
    ymk_id = models.AutoField(primary_key=models.ProtectedError)
    ymk_shifr = models.IntegerField(validators=[MinValueValidator(1)])
    ymk_id_prepod = models.ForeignKey(Prepod, on_delete=models.PROTECT, related_name="ymk_prepod")
    ymk_id_discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT, related_name="ymk_discipline")
    ymk_id_uchPlan = models.ForeignKey(UchPlan, on_delete=models.PROTECT, related_name="ymk_uchPlan")

    class Meta:
        verbose_name = "УМК"
        verbose_name_plural = "УМК"
    def __str__(self):
        return self.ymk_shifr
#Модель Отчет о работе преподавателя
class Otchet(models.Model):
    otchet_id = models.AutoField(primary_key=models.ProtectedError)
    otchet_id_prepod = models.ForeignKey(Prepod, on_delete=models.PROTECT, related_name="otchet_prepod")
    god = models.DateField()
    pokazatel = models.CharField(max_length=50)
    svedeniya = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Отчет о работе преподавателя"
        verbose_name_plural = "Отчет о работе преподавателя"

#Модель Индивидуальный учебный план
class Individ(models.Model):
    individ_id = models.AutoField(primary_key=models.ProtectedError)
    tip = models.CharField(max_length=50)
    name_rabot = models.CharField(max_length=50)
    tredoem = models.CharField(max_length=50)
    forma_finish = models.CharField(max_length=50)
    srok_vip = models.CharField(max_length=50)
    individ_id_prepod = models.ForeignKey(Prepod, on_delete=models.PROTECT, related_name="individ_prepod")
    id_mormi = models.ForeignKey(Normi, on_delete=models.PROTECT, related_name="individ_normi")

    class Meta:
        verbose_name = "Индивидуальный учебный план"
        verbose_name_plural = "Индивидуальный учебный план"

#Модель Индивидуальный учебный план по У.Р.
class IndividYr(models.Model):
    individyr_id = models.AutoField(primary_key=models.ProtectedError)
    kolvo_chasov = models.CharField(max_length=10)
    individ_god = models.IntegerField(validators=[MinValueValidator(1)])
    individyr_id_prepod = models.ForeignKey(Prepod, on_delete=models.PROTECT, related_name="individyr_prepod")
    individyr_id_discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT, related_name="individyr_discipline")
    indiviryr_id_normi = models.ForeignKey(Normi, on_delete=models.PROTECT, related_name="individyr_normi")


    class Meta:
        verbose_name = "Индивидуальный учебный план по У.Р."
        verbose_name_plural = "Индивидуальный учебный план по У.Р."

#Модель Элемент УМК
class Element_Ymk(models.Model):
    element_id = models.AutoField(primary_key=models.ProtectedError)
    element_shifr = models.IntegerField(validators=[MinValueValidator(1)])
    element_anme = models.CharField(max_length=50)
    id_ymk = models.ForeignKey(Ymk, on_delete=models.PROTECT, related_name="element_ymk")

    class Meta:
        verbose_name = "УМК элемент"
        verbose_name_plural = "УМК элемент"
    def __str__(self):
        return self.element_shifr

#Модель Сессия
class Session(models.Model):
    session_id = models.AutoField(primary_key=models.ProtectedError)
    session_semestr = models.IntegerField(validators=[MinValueValidator(1)])
    session_date_start = models.DateField()
    session_date_finish = models.DateField()
    session_id_uchPlan = models.ForeignKey(UchPlan, on_delete=models.PROTECT, related_name="session_uchplan")
    class Meta:
        verbose_name = "Сессия"
        verbose_name_plural = "Сессия"

class ReplacingFileStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

#Модель ФАйл
class Files(models.Model):
    file_id = models.AutoField(primary_key=models.ProtectedError)
    file = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['xlsx'])], storage=ReplacingFileStorage())
    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"

class GroupDiscipline(models.Model):
    groupdiscipline_group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="groupdiscipline_group")
    groupdiscipline_discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT, related_name="groupdiscipline_discipline")

    class Meta:
        verbose_name = "Группа-Дисциплина"
        verbose_name_plural = "Группы-Дисциплины"

class CompititionsDiscipline(models.Model):
    compititionsdiscipline_disc = models.ForeignKey(Compititions, on_delete=models.PROTECT, related_name="compititionsdiscipline_disc")
    compititionsdiscipline_comp = models.ForeignKey(Discipline, on_delete=models.PROTECT, related_name="compititionsdiscipline_comp")

    class Meta:
        verbose_name = "Компетенция-Дисциплина"
        verbose_name_plural = "Компетенции-Дисциплины"

class CompititionsPraktiki(models.Model):
    compititionsPraktiki_prakt = models.ForeignKey(Praktiki, on_delete=models.PROTECT, related_name="compititionsPraktiki_prakt")
    compititionsPraktiki_comp = models.ForeignKey(Compititions, on_delete=models.PROTECT, related_name="compititionsPraktiki_comp")

    class Meta:
        verbose_name = "Компетенция-Практика"
        verbose_name_plural = "Компетенции-Практики"

class ElementYmkUchPlan(models.Model):
    ElementYmkUchPlan_id = models.AutoField(primary_key=models.ProtectedError)
    ElementYmkUchPlan_uchplan = models.ForeignKey(UchPlan, on_delete=models.PROTECT, related_name="ElementYmkUchPlan_uchplan")
    ElementYmkUchPlan_ymk = models.ForeignKey(Element_Ymk, on_delete=models.PROTECT, related_name="ElementYmkUchPlan_ymk")


    class Meta:
        verbose_name = "Элемент УМК - Уч. План"
        verbose_name_plural = "Элементы УМК - Уч. Планы"

class Posobia(models.Model):
    posobia_id = models.AutoField(primary_key=models.ProtectedError)
    posobia_god = models.DateField()
    posobia_status = models.CharField(max_length=50)
    id_ElementYmkUchPlan = models.ForeignKey(ElementYmkUchPlan, on_delete=models.PROTECT,related_name="id_ElementYmkUchPlan")

    class Meta:
        verbose_name = "Пособие"
        verbose_name_plural = "Пособия"

# class UchPlanFiles(models.Model):
#     uchPlanFiles_id = models.AutoField(primary_key=models.ProtectedError)
#     uchplanfiles_plan = models.ForeignKey(UchPlan, on_delete=models.PROTECT,related_name='Ucheb_plan'
#     uchplanfiles_files = models.ForeignKey(Files, on_delete=models.PROTECT,related_name="File#
#     class Meta:
#         verbose_name = "Связь учебного плана с файлом"
#         verbose_name_plural = "Связь учебного плана с файлом"