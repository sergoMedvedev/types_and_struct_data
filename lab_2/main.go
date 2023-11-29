package main

import "fmt"

type Stack struct {
	capacity int   // ёъмкость
	current  int   // текущее количество
	data     []int // данные
}

func work() {

	fmt.Println("Введите число для действия:")
	//TODO НАПИСАТЬ ЭТО ГОВНО

}

func (s Stack) completeness() bool {
	if s.current-1 == s.capacity {
		return true //если стек полна
	}
	fmt.Println("стек полон")
	return false
}

func (s Stack) emptiness() bool {
	if s.current == -1 {
		return true // если стек пуст
	}
	fmt.Println("стек пуст")
	return false
}

func (s Stack) check_first_elm() bool {
	if s.emptiness() {
		fmt.Println("stack don`t have first element")
		return false
	}
	fmt.Println("first element: ", s.data[s.current])
	return true
}

func (s Stack) delete_element() bool {
	if s.emptiness() {
		fmt.Println("stack don`t have first element")
		return false
	}
	fmt.Println("first element : ", s.data[s.current], "was delete")
	s.data = s.data[:len(s.data)-1]
	s.current -= 1
	return true
}

func (s Stack) add_element(element int) {
	//TODO НАПИСТАЬ РЕАЛИЗАЦИЮ ДАННОЙ ФУНКЦИИ
	if s.completeness() == false {
		s.data = append(s.data, element)
		s.current += 1
		fmt.Println("element add")
	}
}

func main() {
	work()
}
