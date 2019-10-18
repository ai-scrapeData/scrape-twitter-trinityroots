
# author_time_string
author_time = "Sun, 02 Jun 2019 23:13:35 GMT"
author_day = author_time.split(" ")[0][:-1]
author_date = author_time.split(" ")[1]
author_month = author_time.split(" ")[2]
author_year = author_time.split(" ")[3]
author_hour = author_time.split(" ")[4]
print(author_day)
print(author_date)
print(author_month)
print(author_year)
print(author_hour)