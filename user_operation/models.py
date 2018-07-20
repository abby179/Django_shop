from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from user.models import UserProfile
from goods.models import Goods


User = get_user_model()


class UserFav(models.Model):
    """
    user's favorite goods
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    """
    addresses of user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100, default="")
    signer_name = models.CharField(max_length=100, default="")
    signer_mobile = models.CharField(max_length=11, default="")
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.address


class UserLeavingMessage(models.Model):
    """
    user message
    """
    MESSAGE_CHOICES = (
        (1, "leave message"),
        (2, "make complain"),
        (3, "raise question"),
        (4, "customer service"),
        (5, "purchase"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES,
                                       help_text=u'message type: 1(leave message), 2(make complain), '
                                                 u'3(raise question), 4(customer service), 5(purchase)')
    subject = models.CharField(max_length=100, default="")
    message = models.TextField(default="", help_text="message_content")
    file = models.FileField(upload_to="message/images/", help_text="uploaded_file")
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.subject
