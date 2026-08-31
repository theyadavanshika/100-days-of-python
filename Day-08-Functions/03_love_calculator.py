print("Welcome to love Calculator!")

def calculate_love_score(name_one, name_two):
    combined_names = (name_one + name_two).lower()

    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")

    first_digit = t + r + u + e

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")

    second_digit = l + o + v + e

    score = (str(first_digit) + str(second_digit))
    print(score)

calculate_love_score("Kanye West", "Kim Kardashian")