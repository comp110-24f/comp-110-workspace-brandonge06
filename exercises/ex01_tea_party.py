"""
Planning a tea party by finding materials needed and total cost!
"""

__author__: str = "730757714"

"""amount of teabags needed for x amount of people"""


def tea_bags(people: int) -> int:
    return people * 2


"""amount of treats needed for x amount of people"""


def treats(people: int) -> int:
    return int(tea_bags(people=people) * 1.5)


"""finding total cost of the party"""


def cost(tea_count: int, treat_count: int) -> float:
    return tea_count * 0.5 + treat_count * 0.75


"""Entry point of the program"""


def main_planner(guests: int) -> None:
    """
    main function of the program, adds up all materials and costs
    """
    print("A Cozy Tea Party for " + str(guests) + " People!")
    teaCount = tea_bags(people=guests)
    print("Tea Bags: " + str(teaCount))
    treatCount = treats(people=guests)
    print("Treats: " + str(treatCount))
    totalCost = cost(tea_count=teaCount, treat_count=treatCount)
    print("Cost: $" + str(totalCost))


if __name__ == "__main__":
    """asking for user input"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
