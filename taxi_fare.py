def calculate_fares(trips, base_fare=50, distance_fare=10):
    total_fare = 0
    for i, distance in enumerate(trips, start=1):
        fare = base_fare + (distance * distance_fare)
        total_fare += fare
        print(f"Trip {i}: ${fare}")
    print(f"Total Fare: ${total_fare}")

trips = [5, 10, 3]  
calculate_fares(trips)
