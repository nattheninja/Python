import math

total_time = 157788000  # total time of simulation
delta_time = 25000  # time delta
elapsed = 0.0  # time elapsed
body = [
    [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24],  # earth
    [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23],  # mars
    [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23],  # mercury
    [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24],  # venus
]

sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
BODIES = 5
GRAVITY = 6.67E-11

while elapsed < total_time:
    for i in range(BODIES - 1):
        # radius calculation
        delta_x = sun[0] - body[i][0]
        delta_y = sun[1] - body[i][1]
        radius = math.sqrt((delta_x ** 2 + delta_y ** 2))

        # force calculation
        pairwise_force = (GRAVITY * body[i][4] * sun[4]) / radius ** 2
        force_x = pairwise_force * (delta_x/radius)
        force_y = pairwise_force * (delta_y/radius)

        # acceleration calculation
        accel_x = force_x/body[i][4]
        accel_y = force_y/body[i][4]

        # velocity calculation and body list update
        vel_x = body[i][2] = body[i][2] + accel_x * delta_time
        vel_y = body[i][3] = body[i][3] + accel_y * delta_time

        # position calculation and body list update
        body[i][0] = body[i][0] + vel_x * delta_time
        body[i][1] = body[i][1] + vel_y * delta_time
    elapsed += delta_time

body.insert(3, sun)

# printing formatted output for each planet
for i in range(BODIES):
    for j in range(5):
        print(f"{body[i][j]:.4e} ", end="")
    print()
