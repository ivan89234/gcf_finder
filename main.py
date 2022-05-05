def gcf(first : int, second : int):
    g = [a for a in [j for j in [i for i in range(second + 1) if i != 0] if second % j ==0]]
    c = [j for j in [i for i in range(first + 1) if i != 0] if first % j ==0]
    result = [p for p in g if p in c]
    if result:
        return f'{max(result)} is the greatest common factor between {first} and {second}'
    return False
#Be careful with high numbers other wise it may crash
print(gcf(13, 17))
print(gcf(48, 12))