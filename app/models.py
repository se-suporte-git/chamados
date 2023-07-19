from django.db import models

class Anotacao(models.Model):
    DATA_SOLICITACAO_CHOICES = (
        ('Comercial', 'Comercial'),
        ('Sobreaviso', 'Sobreaviso'),
    )

    data_solicitacao = models.DateField()
    numero_chamado = models.CharField(max_length=50)
    problema_relatado = models.TextField()
    resolucao = models.TextField()
    data_solucao = models.DateField()
    tipo_atendimento = models.CharField(max_length=20, choices=DATA_SOLICITACAO_CHOICES)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()


class ChamadoAtendido(models.Model):
    numero_chamado = models.CharField(max_length=50)
    problema_relatado = models.TextField()
    resolucao = models.TextField()
    data_solucao = models.DateField()
    tipo_atendimento = models.CharField(max_length=20, choices=(
        ('Comercial', 'Comercial'),
        ('Sobreaviso', 'Sobreaviso'),
    ))
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f'Chamado {self.numero_chamado}'
