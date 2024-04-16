import peewee
from datetime import datetime
import main


class BaseModel(peewee.Model):
    """My base class"""
    created_date = peewee.DateTimeField(default=datetime.now())

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Str method should be overridden!')


class Trip(BaseModel):
    """A class for trips information"""
    title = peewee.CharField(max_length=255, null=False, verbose_name='Title')
    continent = peewee.CharField(max_length=255, null=False, verbose_name='Continent')
    days = peewee.IntegerField(verbose_name='Days')
    nights = peewee.IntegerField(verbose_name='Nights')
    group_size = peewee.IntegerField(verbose_name='Group Size')
    activity = peewee.CharField(max_length=255, null=False, verbose_name='Activity')
    interest = peewee.CharField(max_length=255, null=False, verbose_name='Interest')
    description = peewee.TextField(verbose_name='Description')

    class Meta:
        database = main.db_manager.db

    def __str__(self):
        return (f'Title: {self.title}\n'
                f'Continent: {self.continent}\n'
                f'Days: {self.days}\n'
                f'Nights: {self.nights}\n'
                f'Group size: {self.group_size}\n'
                f'Activity: {self.activity}\n'
                f'Interest: {self.interest}\n'
                f'Description: {self.description}\n'
                f'Created Date: {self.created_date}')


class SearchKey(BaseModel):
    title = peewee.CharField(max_length=255, null=False, verbose_name='Title')
    continent = peewee.CharField(max_length=255, default='None', verbose_name='Continent')
    pages = peewee.IntegerField(default=1, verbose_name='Pages')

    class Meta:
        database = main.db_manager.db

    def __str__(self):
        return (f'Title: {self.title}\n'
                f'Continent: {self.continent}\n'
                f'Pages: {self.pages}')
