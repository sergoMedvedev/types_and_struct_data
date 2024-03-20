from function import is_number

'''СИМВОЛЫ НА ПРОВЕРКУ ВАЛИДАЦИИ'''
CONST_CHAR = ['/', '*', '^', '+', '-', '(', ')']
CHAR_FUNC = ['s','i','n','c','o','s','t','g']
TRIGONO_FUNC = ['sin','cos','tg']


class Interface:
    '''
    поля:
        name progect -название ЛР
        input_string - входная строка
    '''

    def __init__(self, name, string):
        self.name_project = name
        self.input_string = string

    # функция для валидации
    def check_validate(self):
        buff = ''
        array_string_input = []
        for str in self.input_string:
            if str == '-':
                if array_string_input == []:
                    array_string_input.append('0')
            if str == '-':
                if array_string_input[-1] == '(':
                    array_string_input.append('0')

            if (is_number(str)) or str == "x":
                buff += str
                continue

            elif str == ' ':
                continue

            elif (str == "."):
                buff += str
                continue

            elif (str in CONST_CHAR):
                if buff != '':
                    array_string_input.append(buff)
                array_string_input.append(str)
                buff = ''
                continue

            elif (str == 'x'):
                array_string_input.append(str)
                continue

            elif (str in CHAR_FUNC):
                buff+=str
                if buff in TRIGONO_FUNC:
                    array_string_input.append(buff)
                    buff = ''
                    continue
                continue

            else:
                return False
        if buff != '':
            array_string_input.append(buff)
            buff = ''
        #print("Валидация строки", self.input_string, "успешная!")
        print('OOOKKK', array_string_input)
        self.input_string = array_string_input
        return True

    def have_x(self):
        if "x" in self.input_string:
            return 1
        else:
            return 0


#-1+20-7*(9-7*6^2*4^(-1))+4*x+sin(x)