import factory


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for generating example user models.
    """
    class Meta:
        model = "user.BaseUser"

    # Default password for all users
    username = factory.Sequence(lambda idx: f'user{idx}')
    password = factory.PostGenerationMethodCall('set_password', "h6S8f2dW")
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')


class AdminUserFactory(UserFactory):
    """
    Factory for generating example admin user
    """
    username = factory.Sequence(lambda idx: f'admin{idx}')
    staff = True
    admin = True
