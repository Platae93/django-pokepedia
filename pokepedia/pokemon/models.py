from django.db import models
from django.core import validators

# Create your models here.
class Generation(models.Model):
    Name = models.CharField(max_length=10)

    def __str__(self):
        return self.Name

class Pokemon(models.Model):
    Index = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    JapaneseName = models.CharField(max_length=20)
    Transliteration = models.CharField(max_length=20)
    Romaji = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    HatchTime = models.PositiveIntegerField()
    ExperienceYield = models.PositiveIntegerField()
    CatchRate = models.PositiveIntegerField(validators=[validators.MaxValueValidator(255)])
    GenderCode = models.PositiveIntegerField(validators=[validators.MaxValueValidator(255)])
    BaseFriendship = models.PositiveIntegerField(validators=[validators.MaxValueValidator(255)])
    Generation = models.ForeignKey(Generation, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class VariationTypes(models.Model):
    Name = models.CharField(max_length=3)

    def __str__(self):
        return self.Name

class Type(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

class Ability(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class AbilityDescription(models.Model):
    AbilityID = models.ForeignKey(Ability, on_delete=models.CASCADE)
    GenerationName = models.ForeignKey(Generation, on_delete=models.CASCADE)
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.Description

class Variation(models.Model):
    PokemonIndex = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Image = models.ImageField()
    Height = models.IntegerField()
    Weight = models.IntegerField()
    Sprite = models.ImageField()
    VariationType = models.ForeignKey(VariationTypes, on_delete=models.CASCADE)
    Types = models.ManyToManyField(Type)
    Abilities = models.ManyToManyField(Ability)

    def __str__(self):
        return self.Name

