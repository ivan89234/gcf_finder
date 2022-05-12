def gcf(first : int, second : int):
    try:
        g = [a for a in [j for j in [i for i in range(second + 1) if i != 0] if second % j ==0]]
        c = [j for j in [i for i in range(first + 1) if i != 0] if first % j ==0]
        return f'{max([p for p in g if p in c])} is the greatest common factor between {first} and {second}'
    except ValueError:
        return "0 is not allowed"
#Be careful with high numbers other wise it may crash
#if one of the parameters is 0 it will raise ValueError
print(gcf(13, 17))
print(gcf(0, 12))
print(gcf(48, 186))
