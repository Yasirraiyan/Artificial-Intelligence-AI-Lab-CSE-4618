from itertools import permutations

countries = [
    "FSC", "Zhonghua", "Vostok", "Albion",
    "Lurette", "Sundhara", "Verde", "Zayrad"
]

GHS = {"FSC", "Zhonghua", "Vostok", "Albion", "Lurette"}
communicators = {"FSC", "Lurette", "Sundhara", "Zayrad"}

def is_valid(seating):
    # Convert to circular indices
    def left(i): return (i - 1) % 8
    def right(i): return (i + 1) % 8

    # Constraint 1: FSC at seat 0
    if seating[0] != "FSC":
        return False

    # Constraint 2: FSC not adjacent to Vostok, Zhonghua, Zayrad
    for bad in ["Vostok", "Zhonghua", "Zayrad"]:
        if seating[1] == bad or seating[7] == bad:
            return False

    # Constraint 3: FSC must sit next to Albion or Lurette
    if seating[1] not in ["Albion", "Lurette"] and seating[7] not in ["Albion", "Lurette"]:
        return False

    # Constraint 4: Sundhara not next to Zhonghua
    for i in range(8):
        if seating[i] == "Sundhara":
            if seating[left(i)] == "Zhonghua" or seating[right(i)] == "Zhonghua":
                return False

    # Constraint 5: Verde next to at least one communicator
    for i in range(8):
        if seating[i] == "Verde":
            if seating[left(i)] not in communicators and seating[right(i)] not in communicators:
                return False

    # Constraint 6: No more than 2 GHS members in any 3 consecutive seats
    for i in range(8):
        count = 0
        for j in range(3):
            if seating[(i + j) % 8] in GHS:
                count += 1
        if count > 2:
            return False

    return True

# Fix FSC at position 0, permute the rest
others = [c for c in countries if c != "FSC"]

for perm in permutations(others):
    seating = ["FSC"] + list(perm)
    if is_valid(seating):
        print("✅ Valid Seating Arrangement Found:")
        for i, seat in enumerate(seating):
            print(f"S{i+1}: {seat}")
        break
