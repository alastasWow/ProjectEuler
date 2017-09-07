import time

perfectCubes = {}
num = 406
cubeNum = 5
delta = time.time()
while True:
    cube = tuple(sorted((map(int, str(num**3)))))
    if cube in perfectCubes:
        perfectCubes[cube][0] += 1
        if perfectCubes[cube][0] == cubeNum:
            print(cube, perfectCubes[cube][1], perfectCubes[cube][1]**3)
            
            break
    else:
        perfectCubes[cube] = [1, num]
    num += 1
delta = time.time() - delta
print(delta)
