import csv


def load_dataset(file_name=''):
    df = []
    #with open('bike_sales_100k.csv', newline='',encoding='utf-8') as fp:
    with open(file_name, newline='',encoding='utf-8') as fp:    
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            df.append(row)
    return df


def define_sales_cities(city=None,bike=None,lst=[]):
    city_lst = []
    for el in lst:
        city_lst.append(el[6])
    return set(city_lst)
    
    
def calculate_sum(city=None, lst=[]):
    df = list(filter(lambda x: x[6] == city, lst))
    sum = 0
    for el in df:
        sum += int(el[4]) * int(el[5])        
    return sum
    