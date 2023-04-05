from django.http import HttpResponse 


def saludo(self):
    return HttpResponse('holaaaaaaaaaaaaa')



# class Nombre(models.Model):
#     Nombre = models.CharField(max_length=40)
#     dni = models.IntegerField()
