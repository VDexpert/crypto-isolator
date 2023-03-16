

def parsing_last_hour():
    '''
    The function every hour checks the file with name-pattern "result_analyzer_alt_id_object_analyzerALT",
    checks if the value of "dependenceOFF-price" has changed by more than 1%, and if the condition is met,
    the function assigns a notification string about this in the "alert" field of the model object AnalyzerALT
    '''

    id_obj = "A value the model object AnalyzerALT that is automatically assigned when a command " \
             "is created in the management/command package. To get or set object field values"

    with open('result_analyzer_alt', encoding='utf-8') as f:
        damp = []
        for i in range(1, 12):
            '''
            360 - this is the number of lines the scraper writes 
            in one hour, taking into account the 10 second delay
            '''
            damp.append(float(f.readline().split(',')[1].split(' ')[2]))

        min_cleaned_price = min(damp)
        max_cleaned_price = max(damp)
        changing_value = max_cleaned_price/min_cleaned_price

        if changing_value > 1:
            print(f'The price value has changed over the past hour by {changing_value}%')
        else:
            print("")


if __name__ == '__main__':
    parsing_last_hour()
