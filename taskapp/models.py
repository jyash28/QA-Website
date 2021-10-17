from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Question(TimeStampedModel):
    title = models.TextField()
    name = models.ForeignKey('User', on_delete=models.CASCADE, related_name='User')
    question_type = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='Question', null=True, blank=True)

    # ans = models.TextField()

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Question'

    def __str__(self):
        return self.title

    @property
    def related_ques(self):
        return Question.objects.filter(question_type=self.question_type).exclude(id=self.id)[:4]

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        # verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Answer(TimeStampedModel):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, blank=False, null=True, related_name="answer")
    name = models.ForeignKey('User', on_delete=models.CASCADE)
    ans = models.TextField()

    def __str__(self):
        return self.ans


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, firstname, lastname):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.admin = True
        user.firstname = firstname
        user.lastname = lastname
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(
        verbose_name='email address ',
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics', null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def get_full_name(self):
        full_name = "{} {}".format(self.firstname, self.lastname)
        return full_name.strip()

    def __str__(self):
        return self.email
