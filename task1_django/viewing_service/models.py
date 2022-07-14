from django.db import models


class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        db_table = 'equipment'

    def __str__(self):
        return self.name


class Modes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = 'modes'

    def __str__(self):
        return self.name


class Durations(models.Model):
    id = models.IntegerField(primary_key=True)

    # TODO think about on_delete
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    mode = models.ForeignKey(Modes, on_delete=models.CASCADE)

    start = models.DateTimeField()
    stop = models.DateTimeField()

    minutes = models.IntegerField()

    class Meta:
        db_table = 'durations'
