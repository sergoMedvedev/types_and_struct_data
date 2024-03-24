#Импортируем матрицу смежноссти
def dowloud_matrix(name_file):
    new =[]
    b = []
    try:
        file = open(name_file)
        array = [row.strip() for row in file]
        for i in range(len(array)):
            buff = array[i].strip("")
            for i in buff:
                b.append(int(i))
            new.append(b)
            b=[]
        return True, new
    except FileNotFoundError:
        return False, None


