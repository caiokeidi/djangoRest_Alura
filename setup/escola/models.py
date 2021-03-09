from django.db import models

class Aluno(models.Model):
    objects = models.Manager() ##Tive que colocar isso por conta de um erro no VSCODE
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    objects = models.Manager() ##Tive que colocar isso por conta de um erro no VSCODE
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao
