from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Custom Account Manager
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User Model
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

# Movie Model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

# Ticket Model
class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    seat = models.CharField(max_length=10)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return f"Ticket for {self.movie.title}"

# Populate Movies on Migration
@receiver(post_migrate)
def populate_movies(sender, **kwargs):
    if sender.name == "movies":  # Ensures it runs only for the `movies` app
        movies = [
            {"title": "Inception", "genre": "Sci-Fi", "release_year": 2020, "price": 10.00},
            {"title": "Avengers: Endgame", "genre": "Action", "release_year": 2021, "price": 12.00},
            {"title": "Dune", "genre": "Sci-Fi", "release_year": 2021, "price": 15.00},
            {"title": "Top Gun: Maverick", "genre": "Action", "release_year": 2022, "price": 14.00},
            {"title": "Spider-Man: No Way Home", "genre": "Action", "release_year": 2023, "price": 13.00},
        ]

        for movie_data in movies:
            try:
                Movie.objects.get_or_create(**movie_data)
            except Exception as e:
                print(f"Error adding movie {movie_data['title']}: {e}")
