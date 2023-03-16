from django.db import models


NULLABLE = {'blank': True, 'null': True}


class AnalyzerBTC(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите название парсера', unique=False, db_index=True)
    stock_market = models.CharField(verbose_name='Ссылка на главную страницу биржи', max_length=500)
    url = models.CharField(verbose_name='Ссылка на динамику актива BTC', max_length=2000, unique=False)
    comment = models.CharField(max_length=300, verbose_name='Комментарий')
    time_scraping = models.SmallIntegerField(verbose_name='Время работы анализатора в сутках')
    div_class = models.CharField(verbose_name='div class', max_length=300, help_text='Укажите div, из которого необходимо получить данные', **NULLABLE)

    class Meta:
        verbose_name = 'Анализатор bitcoin'
        verbose_name_plural = 'Анализаторы bitcoin'


class AnalyzerALT(models.Model):
    analyzer_btc = models.ForeignKey('AnalyzerBTC', on_delete=models.PROTECT, verbose_name='Прикреплен к анализатору bitcoin')
    url = models.CharField(verbose_name='Ссылка на динамику актива альткоина', max_length=2000, unique=False)
    div_class = models.CharField(verbose_name='div class', max_length=300, help_text='Укажите div, из которого необходимо получить данные', **NULLABLE)
    alert = models.CharField(max_length=100, verbose_name='Поле для оповещения пользователя об изменении цены более, чем на 1%', **NULLABLE)
    dependence = models.SmallIntegerField(verbose_name='Зависимость от цены bitcoin', **NULLABLE)

    class Meta:
        verbose_name = 'Анализатор-корректор altcoin'
        verbose_name_plural = 'Анализаторы-корректоры altcoin'
