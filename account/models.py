from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

#스터디에 사용했던 AbstractUser 은 필드가 너무 과한 면이 있습니다. (first name, last name 과 같은 정보를 받기 때문에) 
#그래서 어떤 모델을 사용할지 찾아보다가 AbstractBaseUser라는 모델을 사용하게 되었습니다. 

#이는 아래 grade 필드에서 사용되는 초이스 입니다. 우리가 흔히 웹사이트에서 무언가를 선택할 때 사용되는 select 안에 들어간다고 생각하시면 됩니다. 


'''학년 정보 선택 상자'''
GRADE_CHOICES = (
    ("1","1학년"),
    ("2","2학년"),
    ("3","3학년"),
    ("4","4학년"),
)


#AbstractBaseUser 에는 objects = UserManager() 이 있습니다. (이가 꼭 필요한 것 같습니다. 없으면 오류가 나더라고요)
#User 로 가입하고자 할 때 유효한 정보를 넘기는지 아닌지 검사하는 것이라고 생각하시면 될 것 같습니다. 
#이걸 헬퍼 클래스 라고 한다고 합니다..

class UserManager(BaseUserManager):
    # 유저를 생성할 때 이메일이 없다면 이메일이 있어야 한다는 오류를 발생시킵니다. 
    def create_user(self, email, password, name, student_num, phone_num, first_major):
        if not email:
            raise ValueError(("Users must have an email address"))
        # 유저 객체를 생성합니다.
        user = self.model(
            #normalize_email 이메일 정규화라고 하는데 예를 들어 이메일을 대문자로 입력했다면 소문자로 바꿔서 저장해주는 역할을 한다고 합니다. (확실하지는 않음..)
            email=self.normalize_email(email),
            name=name, 
            student_num=student_num, 
            phone_num=phone_num, 
            first_major=first_major,
        )
        #비밀번호 해시함수입니다.
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    #슈퍼유저를 생성하는 것이라면 이 함수를 실행시킵니다. 
    def create_superuser(self, email, password, name, student_num, phone_num, first_major):
        #유저의 email이라는 필드에 입력받은 email을, username이라는 필드에 username을, .. 넣어 저장합니다. 
        user = self.create_user(
            email=email,
            password=password,
            name=name, 
            student_num=student_num, 
            phone_num=phone_num, 
            first_major=first_major,

        )
        
        #슈퍼유저인지 아닌지에 대한 정보를 담습니다.
        user.is_superuser = True
        user.save()

        return user
    
#공통적으로 등장하는 verbose_name 은 db에서 보다 간편하게 필드가 무엇을 의미하는지 알 수 있도록 해주는 역할이라고 생각하시면 될 것 같습니다.
class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    #메인 유저의 아이디를 결정하는 부분입니다. 이메일 필드와 유저네임 필드의 역할이 겹치는 것 같아 이메일을 메인으로 설정하였습니다. 필요시 수정하겠습니다.
    USERNAME_FIELD = "email"

    #슈퍼유저 생성시 필수로 입력받고 싶은 값을 받는 부분입니다. NULL|BRANK 값이 FALSE값을 반드시 넣어주어야 합니다.
    REQUIRED_FIELDS = ['name','student_num','phone_num','first_major']

    objects = UserManager()

    email = models.EmailField(
        verbose_name=("email"),
        max_length=200,
        unique=True,
    )  

    name = models.CharField(
        max_length=20,
        verbose_name="이름",
    )

    student_num = models.CharField(
        verbose_name="학번",
        max_length=30,
    )

    grade = models.CharField(
        max_length=10,
        choices = GRADE_CHOICES,
        default="1",
        verbose_name="학년",
    )
    phone_num = models.CharField(
        max_length=20,
        verbose_name="휴대폰 번호",
    )

    first_major = models.CharField(
        max_length=30,
        verbose_name="본전공",
    )

    second_major = models.CharField(
        max_length=30,
        verbose_name="이중전공",
        null=True,
        blank=True,
    )

    is_accepted = models.BooleanField(
        default = False,
        verbose_name="합격 여부",
    )

    is_active = models.BooleanField(
        verbose_name=("Is active"),
        default=True,
    )

    # email field와 역할이 겹치는 면이 있는 것 같아 임시로 주석처리 하였습니다.
    # 기능상으로는 username이나 email중 어느 쪽을 사용해도 동일하니, 혹시라도 username이 꼭 필요한 것 같다는 의견이 있을시 수정하겠습니다.

    # username = models.CharField(
    #     verbose_name=("username"),
    #     max_length=50,
    #     unique=True,
    # ) 

    #class User(AbstractBaseUser, PermissionsMixin) 에서의 permissionmixin 에서 가져온 것입니다.
    # 이 부분은 그냥 넘기는게 나을 것 같습니다.
    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        managed = True
        db_table = 'user'