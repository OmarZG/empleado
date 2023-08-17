from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    """Model definition for Habilidades."""

    # TODO: Define fields here
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        """Meta definition for Habilidades."""

        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        """Unicode representation of Habilidades."""
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    """ Modelo para tabla empleado  """

    # TODO: Define fields here
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Facturacón'),
        ('4', 'Recaudación'),
        ('5', 'Sistemas'),
        ('6', 'Mantenimiento'),
        ('7', 'Otro'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres Completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        """Meta definition for Empleado"""

        verbose_name = 'Mi Empledado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name', 'last_name']
        unique_together = ('first_name', 'departamento')


    def __str__(self):
        return self.first_name + '-' + self.last_name