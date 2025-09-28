## TERMINAL CALCULATOR PROGRAM ##

def main():
    choice = 0
    while choice != 1 and choice != 2 and choice != 3:
        print("=============================================================")
        print("What kind of operations would you like to compute?: ")
        print("1) Arithmetic")
        print("2) Data Measures")
        print("3) Conversions")
        print("=============================================================")
        choice = int(input())

    if choice == 1:
        arithmetic()

    if choice == 2:
        data_measures()

    if choice == 3:
        conversions()

def arithmetic():
    choice = 0
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("=============================================================")
        print("What arithmetic operation would you like to compute?")
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("=============================================================")
        choice = int(input())

    print("=============================================================")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    print("=============================================================")

    if choice == 1:
        print(f"Your answer is: {number1+number2}")
    elif choice == 2:
        print(f"Your answer is: {number1-number2}")
    elif choice == 3:
        print(f"Your answer is: {number1*number2}")
    elif choice == 4:
        print(f"Your answer is: {number1/number2}")
    else:
        print("Error")

def data_measures():
    choice = 0
    while choice != 1 and choice != 2 and choice != 3:
        print("=============================================================")
        print("Which data measure would you like to compute?")
        print("1) Mean")
        print("2) Median")
        print("3) Mode")
        print("=============================================================")
        choice = int(input())
        print("=============================================================")

    def find_mean():
        values = []
        total = 0
        keep_going = True
        print("Input values one by one that you wish to find the average of, press enter when done: ")
        while keep_going:
            try:
                number = int(input())
                values.append(number)
            except ValueError:
                keep_going = False

        for value in values:
            total += value

        mean = total/len(values)
        print(f"The mean is: %.2f" %mean)

    def find_median():
        values = []
        keep_going = True
        print("Input values one by one that you wish to find the median of, press enter when done: ")
        while keep_going:
            try:
                number = int(input())
                values.append(number)
            except ValueError:
                keep_going = False

        values.sort()
        count = len(values)

        if count % 2 == 0:
            median_index1 = int(count/2)
            median_index2 = int(count/2 + 1)
            median = (values[median_index1-1] + values[median_index2-1])/2
            print(f"Sorted values: {values}")
            print(f"The median is: {median}")
        elif count % 2 == 1:
            median_index = int((count+1) / 2)
            median = values[median_index-1]
            print(f"Sorted values: {values}")
            print(f"The median is: {median}")
        else:
            print("Error")

    def find_mode():
        values = []
        keep_going = True
        print("Input values one by one that you wish to find the mode of, press enter when done: ")
        while keep_going:
            try:
                number = int(input())
                values.append(number)
            except ValueError:
                keep_going = False

        values.sort()

        # I am creating a list that consists of individual copies of each number the user gave to the program
        numbers_in_list = []
        for value in values:

            if numbers_in_list.count(value) == 0:
                numbers_in_list.append(value)
            elif numbers_in_list.count(value) == 1:
                continue

        # Now this list will use the previous list to count how many of each number are present in the user given list
        # In doing so we can single out the largest number in this list, match it with the index of the "numbers_in_list" list, and find our mode
        counts_of_digits = []
        for num in numbers_in_list:
            counts_of_digits.append(values.count(num))


        mode_index = counts_of_digits.index(max(counts_of_digits))

        # Code to check if there are more than one mode (variable names are complicated sorry!)
        mode_count = max(counts_of_digits)
        counts_of_digits_copy = counts_of_digits.copy()
        counts_of_digits.remove(mode_count)
        if mode_count != max(counts_of_digits):
            print(f"Sorted values: {values}")
            print(f"The mode is: {numbers_in_list[mode_index]}")
        elif mode_count == max(counts_of_digits):
            number_of_modes = counts_of_digits_copy.count(mode_count)
            # Appending modes to a list
            modes = []

            message = "The modes in your data set are: "
            for i in range(number_of_modes):
                    modes.append(numbers_in_list[counts_of_digits_copy.index(mode_count)])
                    numbers_in_list.pop(counts_of_digits_copy.index(mode_count))
                    counts_of_digits_copy.remove(mode_count)
                    if number_of_modes == 2 and i == 0:
                        message += f"{modes[i]} "
                    elif i+1 == number_of_modes:
                        message += f"and {modes[i]}"
                    else:
                        message += f"{modes[i]}, "

            print(f"Sorted values: {values}")
            print(message)

    if choice == 1:
        find_mean()

    if choice == 2:
        find_median()

    if choice == 3:
        find_mode()

def conversions():
    choice = 0
    while choice != 1 and choice != 2 and choice != 3:
        print("=============================================================")
        print("Which conversions would you like to compute?")
        print("1) Distance")
        print("2) Temperature")
        print("3) Time")
        print("=============================================================")
        choice = int(input())
        print("=============================================================")


    def distance():
        distance_conversion_choice = 0
        while distance_conversion_choice != 1 and distance_conversion_choice != 2:
            print("Choose your desired conversion")
            print("1) Km to Miles")
            print("2) Miles to Km")
            print("=============================================================")
            distance_conversion_choice = int(input())
            print("=============================================================")


        if distance_conversion_choice == 1:
            print("How many Kilometers are you working with?")
            print("=============================================================")
            km = int(input())
            miles = km / 1.609
            print("=============================================================")
            print(f"{km}km is {miles} in miles")

        if distance_conversion_choice == 2:
            print("How many Miles are you working with?")
            print("=============================================================")
            miles = int(input())
            km =  miles * 1.609
            print("=============================================================")
            print(f"{miles} miles is {km}km")

    def temperature():
        temp_conversion_choice = 0
        while temp_conversion_choice != 1 and temp_conversion_choice != 2:
            print("Choose your desired conversion")
            print("1) Celsius to Fahrenheit")
            print("2) Fahrenheit to Celsius")
            print("=============================================================")
            temp_conversion_choice = int(input())

        if temp_conversion_choice == 1:
            print("=============================================================")
            print("Enter your temperature in Celsius: ")
            print("=============================================================")
            celsius = int(input())
            print("=============================================================")
            fahrenheit = (celsius*(9/5)) + 32
            fahrenheit = round(fahrenheit, 2)
            print(f"{celsius} degrees Celsius in Fahrenheit is {fahrenheit} degrees")
        elif temp_conversion_choice == 2:
            print("=============================================================")
            print("Enter your temperature in Fahrenheit: ")
            print("=============================================================")
            fahrenheit = int(input())
            print("=============================================================")
            celsius = (fahrenheit-32) * (5/9)
            celsius = round(celsius, 2)
            print(f"{fahrenheit} degrees Fahrenheit in Celsius is {celsius} degrees")



    def time():
        measurement_choice = 0
        while measurement_choice != 1 and measurement_choice != 2 and measurement_choice != 3 and measurement_choice != 4 and measurement_choice != 5 and measurement_choice != 6:
            print("What is the measurement of time you wish to convert?: ")
            print("1) Seconds")
            print("2) Minutes")
            print("3) Hours")
            print("4) Days")
            print("5) Months")
            print("6) Years")
            print("=============================================================")
            measurement_choice = int(input())
            print("=============================================================")

        if measurement_choice == 1:
            time_measurement = "Seconds"
        elif measurement_choice == 2:
            time_measurement = "Minutes"
        elif measurement_choice == 3:
            time_measurement = "Hours"
        elif measurement_choice == 4:
            time_measurement = "Days"
        elif measurement_choice == 5:
            time_measurement = "Months"
        elif measurement_choice == 6:
            time_measurement = "Years"
        else:
            time_measurement = "Error"

        time_measurement_list = ["Seconds", "Minutes", "Hours", "Days", "Months", "Years"]


        def convert_time(measurement_name):
            print(f"What is the amount of {measurement_name.lower()} you are working with?")
            time_amount = int(input())
            conversion_choice = 0
            while conversion_choice != 1 and conversion_choice != 2 and conversion_choice != 3 and conversion_choice != 4 and conversion_choice != 5:
                print("=============================================================")
                print(f"What are you converting {measurement_name.lower()} to?")
                count = 1
                time_measurement_options = []
                for measurement in time_measurement_list:
                    if measurement_name == measurement:
                        continue
                    else:
                        time_measurement_options.append(measurement)
                        print(f"{count}) {measurement}")
                        count += 1
                print("=============================================================")
                conversion_choice = int(input())
            if conversion_choice == 1:
                conversion_choice_name = time_measurement_options[0]
            elif conversion_choice == 2:
                conversion_choice_name = time_measurement_options[1]
            elif conversion_choice == 3:
                conversion_choice_name = time_measurement_options[2]
            elif conversion_choice == 4:
                conversion_choice_name = time_measurement_options[3]
            elif conversion_choice == 5:
                conversion_choice_name = time_measurement_options[4]
            elif conversion_choice == 6:
                conversion_choice_name = time_measurement_options[5]
            else:
                conversion_choice_name = "None"
                print("Error")



            ## Now we can identify our current measurement, our desired conversion and our measurement quantity, and calculate accordingly

            if measurement_name == "Seconds":
                if conversion_choice_name == "Minutes":
                    result = time_amount/60
                elif conversion_choice_name == "Hours":
                    result = time_amount/3600
                elif conversion_choice_name == "Days":
                    result = time_amount/86400
                elif conversion_choice_name == "Months":
                    result = ((time_amount/86400)/30.44)
                elif conversion_choice_name == "Years":
                    result = ((time_amount/86400)/365)
            elif measurement_name == "Minutes":
                if conversion_choice_name == "Seconds":
                    result = time_amount*60
                elif conversion_choice_name == "Hours":
                    result = time_amount/60
                elif conversion_choice_name == "Days":
                    result = time_amount/1440
                elif conversion_choice_name == "Months":
                    result = ((time_amount/1440)/30.44)
                elif conversion_choice_name == "Years":
                    result = ((time_amount/1440)/365)
            elif measurement_name == "Hours":
                if conversion_choice_name == "Seconds":
                    result = time_amount * 360
                elif conversion_choice_name == "Minutes":
                    result = time_amount * 60
                elif conversion_choice_name == "Days":
                    result = time_amount / 24
                elif conversion_choice_name == "Months":
                    result = ((time_amount / 24) / 30.44)
                elif conversion_choice_name == "Years":
                    result = ((time_amount / 24) / 365)
            elif measurement_name == "Days":
                if conversion_choice_name == "Seconds":
                    result = time_amount * 86400
                elif conversion_choice_name == "Minutes":
                    result = time_amount * 1440
                elif conversion_choice_name == "Hours":
                    result = time_amount * 24
                elif conversion_choice_name == "Months":
                    result = time_amount / 30.44
                elif conversion_choice_name == "Years":
                    result = time_amount / 365
            elif measurement_name == "Months":
                if conversion_choice_name == "Seconds":
                    result = time_amount * 2628288
                elif conversion_choice_name == "Minutes":
                    result = time_amount * 43800
                elif conversion_choice_name == "Hours":
                    result = time_amount * 730
                elif conversion_choice_name == "Days":
                    result = time_amount * 30.44
                elif conversion_choice_name == "Years":
                    result = time_amount / 12
            elif measurement_name == "Years":
                if conversion_choice_name == "Seconds":
                    result = time_amount * 31536000
                elif conversion_choice_name == "Minutes":
                    result = time_amount * 525600
                elif conversion_choice_name == "Hours":
                    result = time_amount * 8760
                elif conversion_choice_name == "Days":
                    result = time_amount * 365
                elif conversion_choice_name == "Months":
                    result = time_amount * 12
            else:
                print("Error")
                result = 0

            print("=============================================================")
            print(f"{time_amount} {measurement_name} is {round(result, 2)} {conversion_choice_name}")

        convert_time(time_measurement)


    if choice == 1:
        distance()
    elif choice == 2:
        temperature()
    elif choice == 3:
        time()




main()