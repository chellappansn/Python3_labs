fuel_per_lap = 2.25
laps = 45
fuel_requirement = laps * fuel_per_lap


fuel = fuel_requirement * 1.5
print("Full fuel load:", fuel, "kg")

q_lap_time = 80.45

t_lap_time = q_lap_time - (0.35/10) * 5
print("Theoretical initial lap time:", t_lap_time)

lap_one_time = t_lap_time + ((fuel/10) * 0.35)
print("Lap one time", lap_one_time, "secs")
