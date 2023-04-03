def bagiArray(array,pembagi):
    arrayOutput = [] 
    temp = ''
    for char in array:
        if char == pembagi:
            arrayOutput = tambahArray(arrayOutput,temp)
            temp = ''
        else:
            temp = tambahArray(temp,char)
    arrayOutput = tambahArray(arrayOutput,temp)
    return arrayOutput
             
def tambahArray(array1,array2):
    sumArray = [0 for i in range (panjang(array1) + panjang(array2))]
    for i in range (panjang(array1)):
        sumArray[i] = array1[i]
    for i in range(panjang(array1)+1,panjang(array1)+panjang(array2)):
        sumArray[i] = array2[i]
    return sumArray
        

def panjang(x):
    sum = 0
    for i in (x):
        sum += 1
    return sum