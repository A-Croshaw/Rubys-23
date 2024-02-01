from django.db import models


#Choice fields
CONDITION = (
    ("new", "New"),
    ("used", "Used"),
)

CATEGORY = (
    ("non-fiction", "Non-Fiction"),
    ("fiction","Fiction"),
    ("childrens", "Childrens"),
    )


class Genre(models.Model):
    """ Creates Categories OF books """

    class Meta:
        """ Gives the plural name of the model"""
        verbose_name_plural = 'Genres'

    genre = models.CharField(max_length=254)
    view_genre = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.genre

    def get_view_genre(self):
        return self.view_genre


class Book(models.Model):
    """Creates an instance of a book"""
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=50, choices=CATEGORY, default="Non-Fiction")
    sku = models.CharField(max_length=254, null=True, blank=True)
    ISBN = models.CharField(max_length=254, null=True, blank=True)
    author = models.CharField(max_length=254)
    title = models.CharField(max_length=254 )
    link = models.CharField(max_length=254, null=True, blank=True)
    pages = models.PositiveIntegerField(null=True,blank=True)
    first_published = models.PositiveIntegerField(null=True,blank=True)
    this_publication_date = models.PositiveIntegerField(null=True,blank=True)
    condition = models.CharField(max_length=50, choices=CONDITION, default="new")
    description = models.TextField()
    language = models.CharField(max_length=254, null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
