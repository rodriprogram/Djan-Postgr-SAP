from django.db import models

# Create your models here.
#debemos extender de models.Model para ser reconocida como modelo
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio: {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona(models.Model):
    #son atrib estáticos (fuera del init)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # para domicilio definimos una llave foránea (un dato que refiere a otra tabla)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    #debemos indicar que hace si se elimina el registro al cual refiere,
    #en este caso va a asignar null, pero para eso debemos aclarar que
    #este campo puede recibir null comom valor) si ponemos CASCADE en vez
    #de SET_NULL se eliminan los regitros que usaban el registro eliminado


    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'