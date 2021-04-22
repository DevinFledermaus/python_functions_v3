# Functions Handout Task
def hotel_cost(nights):
    return nights * 140  # in rands


# define plane_ride_cost
def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return 2000
    elif city == "BFN":
        return 1800


# Define retail_car_cost
def retail_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif days >= 3 and days < 7:
        cost = cost - 30
    return cost


def new_sum(*numbers):
    return sum(numbers)


# define trip_cost
def trip_cost(city, days, spending_money):
    return new_sum(plane_ride_cost(city), retail_car_cost(days), hotel_cost(days), spending_money)


print("Your total cost will be: R" + str(trip_cost("Cape Town", 1, 0)))
