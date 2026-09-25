from datetime import datetime, timedelta


def convert_time(time):
    time = time.lower().replace(" ", "").replace(":", "").replace(",", "")

    period = time[-2:]
    numbers = time[:-2]

    if period != "am" and period != "pm":
        print("INVALID TIME")
        return None

    if len(numbers) == 3:
        hour = numbers[0]
        minute = numbers[1:]

    elif len(numbers) == 4:
        hour = numbers[:2]
        minute = numbers[2:]

    elif len(numbers) == 1 or len(numbers) == 2:
        hour = numbers
        minute = "00"

    else:
        print("INVALID TIME")
        return None

    try:
        return datetime.strptime(
            hour + ":" + minute + " " + period,
            "%I:%M %p"
        )

    except ValueError:
        print("INVALID TIME")
        return None


# ---------------- USER INPUT ----------------

a = input("ENTER YOUR NAME: ")

print("Hello", a)

b = input("ENTER YOUR BREAKFAST: ")
c = input("ENTER YOUR LUNCH: ")
d = input("ENTER YOUR DINNER: ")
e = input("ENTER YOUR SNACKS: ")

f = int(input("ENTER YOUR AMOUNT OF WATER DRUNK: "))
g = int(input("ENTER HOURS SLEPT: "))


# ---------------- MEAL TIMES ----------------

breakfast = input("ENTER YOUR BREAKFAST TIME: ")
lunch = input("ENTER YOUR LUNCH TIME: ")
dinner = input("ENTER YOUR DINNER TIME: ")

breakfast = convert_time(breakfast)
lunch = convert_time(lunch)
dinner = convert_time(dinner)


# ---------------- MEAL GAPS ----------------

gap_breakfast_lunch = lunch - breakfast
gap_lunch_dinner = dinner - lunch

next_breakfast = breakfast + timedelta(days=1)

gap_dinner_breakfast = next_breakfast - dinner

total_gap = (
    gap_breakfast_lunch
    + gap_lunch_dinner
    + gap_dinner_breakfast
)

average_gap = total_gap / 3


# ---------------- DAILY REPORT ----------------

print("------ DAILY DIET REPORT ---------")
print("=" * 40)

print("NAME :", a)

print(f"{'BREAKFAST':<20}: {b}")
print(f"{'LUNCH':<20}: {c}")
print(f"{'DINNER':<20}: {d}")
print(f"{'SNACKS':<20}: {e}")

print(f"{'WATER IN GLASSES':<20}: {f}")


# ---------------- WATER CHECK ----------------

def check_water(water):
    if water >= 8:
        return "HYDRATED"
    else:
        return "DRINK MORE WATER"


result = check_water(f)

print(result)


# ---------------- SLEEP CHECK ----------------

print("SLEEP in Hrs:", g)

if g < 7:
    print("HAVE MORE REST")

elif g > 9:
    print("YOU ARE SLEEPING TOO MUCH")

else:
    print("YOU ARE HAVING A GOOD AMOUNT OF SLEEP")


# ---------------- MEAL GAP REPORT ----------------

print("=" * 40)

print("AVERAGE GAP BETWEEN MEALS:", average_gap)
print("BREAKFAST → LUNCH:", gap_breakfast_lunch)
print("LUNCH → DINNER:", gap_lunch_dinner)
print("DINNER → BREAKFAST:", gap_dinner_breakfast)

print("--- END OF REPORT ---")
