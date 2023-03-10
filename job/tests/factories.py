from django.contrib.auth.models import User

import factory
from faker import Faker
from pytest_factoryboy import register

from ..models import Resume

fake = Faker()


@register
class ResumeFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda num: f'Resume #{num}')
    status = fake.random_choices([i[0] for i in Resume.STATUSES], length=1)[0]
    grade = fake.random_int(1, 10)
    specialty = fake.text(50)
    salary = fake.pydecimal(left_digits=8, right_digits=2, positive=True)
    education = fake.text(50)
    experience = fake.text(50)
    portfolio = fake.url()
    phone = fake.msisdn()
    email = fake.email()

    class Meta:
        model = Resume


@register
class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda num: f'User #{num}')
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        self.set_password('password')

    class Meta:
        model = User
