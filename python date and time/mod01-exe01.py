
# 1. Create a program that calculates the estimated duration
# of a trip in hours and minutes. This should include an
# estimated date/time of departure and an estimated date/time
# of arrival:
#
#         For the date/time of departure and arrival, the program should use the YYYY-MM-DD.
#         Format for dates and the HH:MM AM/PM format for times.
#         For the miles and miles per hour, the program should only accept integer entries like 200 and 65.
#         Assume that the user will enter valid data.

from datetime import datetime, timedelta

def get_invoice_data():
    input_depp_date = input("Estimated date of departure (YYYY-MM-DD): ")
    date_depparture = datetime.strptime(input_depp_date, '%Y-%m-%d')

    input_depp_time = input("Estimated time of departure (HH:MM AM/PM): ")
    time_depparture = datetime.strptime(input_depp_time, '%I:%M %p')

    input_miles = int(input("Enter miles: "))
    input_miles_hrs = int(input("Enter miles per hour: "))

    print()

    hours = int(input_miles/input_miles_hrs)
    minutes = int(((input_miles/input_miles_hrs)-hours)*60)

    date_arrival = date_depparture + timedelta(hours= time_depparture.hour,minutes=time_depparture.minute) + timedelta(hours=hours, minutes=minutes)
    time_arrival = time_depparture + timedelta(hours=hours, minutes=minutes)
    print("Estimated travel time")
    print("Hours:",hours)
    print("Minutes:",minutes)
    print("Estimated date of arrival:",datetime.strftime(date_arrival, '%Y-%m-%d'))
    print("Estimated time of arrival:",datetime.strftime(time_arrival, '%I:%M %p'))

def main():
    print("Arrival Time Estimator")
    while True:
        date_depparture = get_invoice_data()
        print()
        result = input("Continue? (y/n): ")
        print()
        if result.lower()!= 'y':
            print('Bye!')
            break
if __name__ == '__main__':
        main()
