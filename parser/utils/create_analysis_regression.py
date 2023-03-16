from django.core.management import BaseCommand


def do():
    '''
    The function gets price values from files with name-patterns "result_analyzer_btc_id_object_analyzerBTC"
    and "result_analyzer_alt_id_object_analyzerALT" and returns the value of the influence of the bitcoin
    price on the altcoin price (from 0 to 1) and assigns this value
    to the "dependence" field of the model object AnalyzerALT
    '''
    pass