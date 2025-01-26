def likes(names):
    single = " likes this"
    plural = " like this"
    qty = len(names)

    if qty == 0:
        return f"no one{single}"
    if qty == 1:
        return f"{names[0]}{single}"
    if qty == 2:
        return f"{names[0]} and {names[1]}{plural}"
    if qty == 3:
        return f"{names[0]}, {names[1]} and {names[2]}{plural}"
    return f"{names[0]}, {names[1]} and {qty - 2} others{plural}"


def test_likes():
    assert likes([]) == "no one likes this"
    assert likes(["Peter"]) == "Peter likes this"
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
    assert (likes(["Alex", "Jacob", "Mark", "Max"]) ==
            "Alex, Jacob and 2 others like this")
    assert (likes(["Alex", "Jacob", "Mark", "Max", "Eve"]) ==
            "Alex, Jacob and 3 others like this")
