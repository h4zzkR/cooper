from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, nick, first_name, last_name,  is_super):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан!')
        user = self.model(email=email, nickname=nick, first_name=first_name,
                          last_name=last_name, is_superuser=is_super)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, nick, first_name, last_name):
        return self._create_user(email, password, nick, first_name, last_name, False)

    def create_superuser(self, email, password, nick, first_name, last_name):
        return self._create_user(email, password, nick, first_name, last_name, True)
