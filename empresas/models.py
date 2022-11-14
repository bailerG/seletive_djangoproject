from django.db import models

class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tecnologia


class Empresa(models.Model):
    choices_nicho = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
        ('T', 'Tecnologia'),
        ('R', 'Restaurante'),
    )
    
    logo = models.ImageField(upload_to="logo_empresas")
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    tecnologias = models.ManyToManyField(Tecnologias)
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    caracteristicas_empresa = models.TextField()
    nicho_empresa = models.CharField(max_length=3, choices=choices_nicho)
    
    def __str__(self):
        return self.nome
    
    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()
    
class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    email = models.EmailField(null=True)
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')

    def progresso(self):
        x = [((i+1)*20,j[0]) for i, j in enumerate(self.choices_status)]
        x = list(filter(lambda x: x[1] == self.status, x))[0][0]
        return x

    def __str__(self):
        return self.titulo
