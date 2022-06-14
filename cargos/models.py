from django.db import models


class Cargo(models.Model):


	cargo = models.CharField(
		verbose_name = "Nome do Cargo",
		max_length = 60,
		)

	nivel_report = models.CharField(
		verbose_name = "Nivel de Report",
		max_length = 2,
		)
	class Meta:
		verbose_name = "Cargo"
		verbose_name_plural = "Cargos"
		db_table = "cargos"

	def __str__(self):
		return self.cargo