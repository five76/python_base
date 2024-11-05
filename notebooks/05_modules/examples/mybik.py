def define_sales_city(df=[]):
    city_list = []
    for row in df:
        city_list.append(row[6])
    city_set = set(city_list)
    return city_set

def calculate_sum_city(city,lst=[]):
    df = list(filter(lambda x: x[6] == city,lst))
    sum = (0.0)
    for row in df:
        sum += float(row[4]) * int(row[5])
    return sum
