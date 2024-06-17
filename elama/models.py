from django.db import models

class Autoevaluacion(models.Model):
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Autoevaluacion: {self.fecha}"


class Estrategia(models.Model): # Título principal
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Principio(models.Model): # Caso principal
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.titulo


class Descriptor(models.Model): # Texto sobre el dato
    principio = models.ForeignKey(Principio, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo


class Volcado(models.Model): # Texto sobre el dato
    autoevaluacion = models.ForeignKey(Autoevaluacion, on_delete=models.CASCADE)
    descriptor = models.ForeignKey(Descriptor, on_delete=models.CASCADE)
    valoracion = models.IntegerField(default=1)

    def __str__(self):
        return f"Descriptor: {self.descriptor} Valoracion: {self.valoracion}"
