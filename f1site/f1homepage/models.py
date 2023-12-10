from django.db import models

class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    birthplace = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    def __str__(self):
        return f'<Driver:id={self.id}, name={self.driver_name}, age={self.age}, birthplace={self.birthplace}, team={self.team}>'

class Qualifying(models.Model):
    GP_CHOICES = [
        ('default', 'バーレーンGP'),
        ('サウジアラビアGP', 'サウジアラビアGP'),
        ('オーストラリアGP', 'オーストラリアGP'),
        ('アゼルバイジャンGP', 'アゼルバイジャンGP'),
        ('マイアミGP', 'マイアミGP'),
        ('モナコGP', 'モナコGP'),
        ('スペインGP', 'スペインGP'),
        ('カナダGP', 'カナダGP'),
        ('オーストリアGP', 'オーストリアGP'),
        ('イギリスGP', 'イギリスGP'),
        ('ハンガリーGP', 'ハンガリーGP'),
        ('ベルギーGP', 'ベルギーGP'),
        ('オランダGP', 'オランダGP'),
        ('イタリアGP', 'イタリアGP'),
        ('シンガポールGP', 'シンガポールGP'),
        ('日本GP', '日本GP'),
        ('アメリカGP', 'アメリカGP'),
        ('メキシコシティGP', 'メキシコシティGP'),
        ('シンガポールGP', 'シンガポールGP'),
        ('日本GP', '日本GP'),
        ('アメリカGP', 'アメリカGP'),
        ('メキシコシティGP', 'メキシコシティGP'),
        ('サンパウロGP', 'サンパウロGP'),
        ('ラスベガスGP', 'ラスベガスGP'),
        ('アブダビGP', 'アブダビGP'),
        
    ]
    year = models.IntegerField(default=2023)
    gp = models.CharField(max_length=100,choices=GP_CHOICES, default='default')
    rank = models.IntegerField(default=1)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Qualifying:id={self.id}, year={self.year},gp={self.gp}, driver={self.driver.driver_name}, rank={self.rank}>'

