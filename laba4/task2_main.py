from task2_simpleClass import Vector

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)  # Vector(3, 4)
print(v2)  # Vector(1, 2)

print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(2, 2)
print(v1 * 2)  # Vector(6, 8)
print(v1 / 2)  # Vector(1.5, 2.0)

print("Magnitude:", v1.magnitude())  # 5.0
print("Normalized:", v1.normalize())  # Vector(0.6, 0.8)

print("Dot product:", v1.dot_product(v2))  # 11

v1.save("vector.json")
v3 = Vector.load("vector.json")
print("Loaded vector:", v3)  # Vector(3, 4)

v4 = Vector.from_string("Vector(5, 6)")
print(v4)  # Vector(5, 6)
