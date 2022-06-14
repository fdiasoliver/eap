from django.db import models



class Gestor(models.Model):

	usuario = models.OneToOneField(
		"usuarios.Usuario",
		verbose_name = "Gestor",
		on_delete = models.PROTECT,
	)
	nome_completo = models.CharField(
		verbose_name = "Nome Completo",
		max_length = 194,
		)
	cargo = models.OneToOneField(
	 	"cargos.Cargo",
	 	verbose_name = "Cargo",
	 	on_delete = models.PROTECT,
	 	)


	class Meta:
		verbose_name = "Gestor"
		verbose_name_plural = "Gestores"
		db_table = "gestores"

	def __str__(self):
		return self.nome_completo


