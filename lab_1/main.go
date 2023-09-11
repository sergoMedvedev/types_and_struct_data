package main

import (
	"fmt"
	"os"
)

func main() {

	var x1, x2, h float32
	var b byte

	fmt.Println("Лаботаторная работа №1")
	fmt.Println("В данной ЛР будет проанализирована функция f(x) = (1/(x-2))+10 \n")

	for b = 250; b <= 255; b++ {
		fmt.Printf("Введите значение X1 (левая граница): ")
		fmt.Fscan(os.Stdin, &x1)
		fmt.Printf("Введите значение X2 (правая граница): ")
		fmt.Fscan(os.Stdin, &x2)
		fmt.Printf("Введите значение h (шаг): ")
		fmt.Fscan(os.Stdin, &h)

		if corectData(x1, x2, h) {
			fmt.Println()
			fmt.Println("Введите более коректные данные:")
			fmt.Println("1) Левая граница должна быть меньше, чем правая")
			fmt.Println("2) Шаг не должен быть отрицательным")
			fmt.Println("3) Разность координат не должна быть меньше шага")
			fmt.Println()
			continue
		}
	}
}

// функция проверки коректного ввода данных.
func corectData(x1 float32, x2 float32, h float32) bool {
	if (x1 > x2) && (h < 0) && (x2-x1 < h) {
		return false
	}

	return true
}

// функция для вычисления значения в точке
func functionValue(valueX float32) float32 {
	res := (1 / (valueX - 2)) + 10
	return res
}

func printTablePoint(x1 float32, x2 float32, h float32) {

	for i := x1; i <= x2; i += h {
		if (i > h) || (i != h) {
			fmt.Println("x = ", i, "\t\t\tf(", i, ")=", functionValue(i))
			continue
		}
	}
}
