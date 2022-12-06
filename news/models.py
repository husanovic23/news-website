from django.db import models

# Create your models here.
class Position(models.Model):
        title = models.CharField(verbose_name='Yangilik turi',max_length=100)
        manba = models.CharField(verbose_name='Manba',max_length=100)
        image = models.ImageField(upload_to='%Y-%m-%d')
        def __str__(self) -> str:
              return self.title
class New(models.Model):
    TIL = (
        ('O\'zbek','Uzbek'),
        ('Qozoq','Qozoq'),
        ('Rus','Rus'),
        ('Boshqa','Boshqa'),
        ('-','-----'),
    )
    name = models.CharField('Nomi ',max_length=255)
    # surname  = models.CharField('Familiyasi' ,max_length=255)
    # place = models.CharField('Manba ', max_length=255)
    # pol = models.CharField('Jinsi',choices=JINSI,default='-',max_length=255)
    sana = models.DateField('T_sanasi ',auto_created=True)
    lang = models.CharField('Tili ',choices=TIL,default='-',max_length=255)
    # group = models.IntegerField('Guruhi ')
    news = models.TextField('Yangilik matni',max_length=1024)
    img = models.ImageField('Yangilik rasmi ',max_length=255)
    position =  models.ForeignKey(Position,on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name}'


# class User(models.Model):
#         name = models.CharField(verbose_name='Ism',max_length=100)
#         lname = models.CharField('Familiya ' ,max_length=100)
#         position =  models.ForeignKey(Position,on_delete=models.CASCADE)
      

#         def __str__(self) -> str:
#               return self.name