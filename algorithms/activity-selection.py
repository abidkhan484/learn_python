start = [0,3,1,5,5,8]
end = [6,4,2,9,7,9]

print('before the algorithm')
print(*start)
print(*end)

# here inside zip func- end is the first parameter
# bcoz sorted func sort using first parameter
# this can be done using dictionary

# one liner
li = sorted(zip(end, start))
# print('after sorting according with the end:\n', *li)

minim = li[0][0]; start=[]; end=[]; start.append(li[0][1]); end.append(li[0][0])
# print(li[0], end=', ')
for i in range(1, len(li)):
    m, n = li[i]
    if n >= minim:
        minim = m
        start.append(li[i][1])
        end.append(li[i][0])
        # print(li[i], end=', ')

print('so the activity selection')
print(*start)
print(*end)
