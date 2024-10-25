from django.db import models

class Generos(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.nombre

class Peliculas(models.Model):
    codigo = models.CharField(max_length=9)
    titulo = models.CharField(max_length=50)
    protagonista= models.CharField(max_length=50)
    duracion = models.IntegerField()
    resumen = models.CharField(max_length=2000)
    foto = models.ImageField(upload_to=f"fotos/", null=True, blank=True)
    idGenero = models.ForeignKey(Generos, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.titulo