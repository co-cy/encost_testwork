from django.db import models


class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Equipment(models.Model):
    id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    name = models.TextField()


class Modes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Durations(models.Model):
    id = models.IntegerField(primary_key=True)

    # TODO think about on_delete
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    start = models.DateTimeField()
    stop = models.DateTimeField()

    mode_id = models.IntegerField()
    minutes = models.IntegerField()