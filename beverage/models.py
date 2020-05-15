from django.db import models


class Beverage(models.Model):
	name			= models.CharField(max_length = 50)
	description		= models.ForeignKey('Description', on_delete = models.SET_NULL, null =True)
	category		= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	sub_category	= models.ForeignKey('SubCategory', on_delete = models.SET_NULL, null=True)
	nutrition		= models.ForeignKey('Nutrition', on_delete = models.SET_NULL, null = True)
	allergy			= models.ManyToManyField('Allergy', through = 'BeverageAllergy')
	size			= models.ManyToManyField('Size', through = 'BeverageSize')


	class Meta:
		db_table	= 'beverages'


class Category(models.Model):
	name			= models.CharField(max_length=50)

	class Meta:
		db_table	= 'categories'


class SubCategory(models.Model):
	name			= models.CharField(max_length = 50)
	category		= models.ForeignKey('Category', on_delete = models.SET_NULL, null= True)
	
	class Meta:
		db_table	= 'sub_categories'


class Nutrition(models.Model):
	kcal_g			= models.DecimalField(max_digits=4, decimal_places=1)
	natrium_mg		= models.DecimalField(max_digits=4, decimal_places =1)
	saturated_fat_g = models.DecimalField(max_digits =4,decimal_places=1)
	sugars_g		= models.DecimalField(max_digits=4, decimal_places =1)
	protein_g       = models.DecimalField(max_digits=4, decimal_places=1)
	caffein_mg      = models.DecimalField(max_digits=4, decimal_places=1)

	class Meta:
		db_table = 'nutritions'

class Allergy(models.Model):
	name			= models.CharField(max_length = 50)

	class Meta:
		db_table	= 'allergies'


class Image(models.Model):
	img_url			= models.URLField(max_length=1000)
	Beverage		= models.ForeignKey('Beverage', on_delete = models.SET_NULL, null =True)

	class Meta:
		db_table	= 'images'


class Size(models.Model):
	name			= models.CharField(max_length = 50)

	class Meta:
		db_table	= 'sizes'

class BeverageSize(models.Model):
	size			= models.ForeignKey('Size', on_delete = models.SET_NULL, null=True)
	Beverage		= models.ForeignKey('Beverage',on_delete = models.SET_NULL, null=True)
	
	class Meta:
		db_table	= 'beverages_allegies'

class BeverageAllergy(models.Model):
	Allergy         = models.ForeignKey('Allergy', on_delete = models.SET_NULL, null=True)
	Beverage        = models.ForeignKey('Beverage',on_delete = models.SET_NULL, null=True)
	
	class Meta:
		db_table	= 'beverages_allergies'

class Description(models.Model):
	content			= models.CharField(max_length = 2000)

	class Meta:
		db_table = 'dscriptions'
