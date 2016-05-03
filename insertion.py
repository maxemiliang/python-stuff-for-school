values = [5,3,2,6,1,4,0]
end = len(values)-1
now = 1

while now <= end:
    insert = now
    while insert != 0 or values[insert] > values[insert-1]:
        if (values > 0):
            values[insert], values[insert-1] = values[insert-1], values[insert]
            insert -= 1
    now += 1
print values


