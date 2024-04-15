ANGLES = []

for angle in range(0, 360):
    if 0 <= angle <= 45:
        ANGLES.append(angle)
    elif 135 <= angle <= 225:
        ANGLES.append(angle)
    elif angle >= 315:
        ANGLES.append(angle)

print(ANGLES)