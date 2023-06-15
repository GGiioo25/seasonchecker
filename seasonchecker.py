def get_time_of_year(month):
    if month < 1 or month > 12:
        return "Invalid month number. Please enter a number from 1 to 12."
    elif month in [1, 2, 12]:
        return "Winter" "zamtari"  
    elif month in [3, 4, 5]:
        return "Spring"  "shemodgoma"
    elif month in [6, 7, 8]:
        return "Summer"  "zafxuli"
    else:
        return "Autumn" "gazafxuli"


month_number = int(input("Enter a month number (1-12): "))


time_of_year = get_time_of_year(month_number)
print("The time of year is:", time_of_year)
