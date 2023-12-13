def calculate_fried_chicken(days):
    fried_chicken = 20.00
    eaten_per_day = 1.00
    growth_rate = 0.05

    for day in range(1, days + 1):
        if day == 7:
            print(f"Fried chicken eaten on day {day} = 0.00")
            print(f"Fried chicken remaining: = {fried_chicken:.2f}")
            continue

        fried_chicken -= eaten_per_day
        print(f"Fried chicken eaten on day {day} = {eaten_per_day:.2f}")
        print(f"Fried chicken remaining: = {fried_chicken:.2f}")

        eaten_per_day += eaten_per_day * growth_rate

        if fried_chicken <= 0:
            print(f"\nIt took {day} days for the dinosaur to run out of fried chicken.")
            break

calculate_fried_chicken(30)  
