#Импортируем матрицу смежноссти
def dowloud_matrix(name_file):
    try:
        file = open(name_file)
        array = [row.strip() for row in file]
        return True, array
    except FileNotFoundError:
        return False


