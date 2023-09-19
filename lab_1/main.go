package main

import (
	"fmt"
	"math"
	"os"
)

const ITERATION_MAX = 500

func main() {
	run()
}

// главная функция
func run() {
	var x1, x2, h float32
	var b byte
	var v byte

	fmt.Println("Лаботаторная работа №1")
	fmt.Println("В данной ЛР будет проанализирована функция f(x) = (1/(x-2))+10 \n")

	for b = 250; b <= 255; b++ {
		fmt.Printf("Введите значение X1 (левая граница): ")
		fmt.Fscan(os.Stdin, &x1)
		fmt.Printf("Введите значение X2 (правая граница): ")
		fmt.Fscan(os.Stdin, &x2)
		fmt.Printf("Введите значение h (шаг): ")
		fmt.Fscan(os.Stdin, &h)
		fmt.Println()

		if corectData(x1, x2, h) {
			fmt.Println()
			fmt.Println("Введите более коректные данные:")
			fmt.Println("1) Левая граница должна быть меньше, чем правая")
			fmt.Println("2) Шаг не должен быть отрицательным")
			fmt.Println("3) Разность координат не должна быть меньше шага")
			fmt.Println()
			continue
		}

		var arrayPoint []float32 = makeArrayWhisPoint(x1, x2, h)

		printTablePoint(arrayPoint)

		var integrationMethod int
		var eps float32
		var dh float32
		var resultIntMethod float32

		for v = 250; v <= 255; v++ {
			fmt.Println()
			fmt.Println("Введите ЭПСЕЛЕН для интегрирования:")
			fmt.Fscan(os.Stdin, &eps)
			if eps > 1 && eps < 0 {
				continue
			}
			fmt.Println()
			fmt.Println("Выберите способ интегрирования. Наберите цифру способа")
			fmt.Println("1 - по ЛЕВОЙ стороне ")
			fmt.Println("2 - по ПРАВОЙ стороне ")
			fmt.Println("3 - по ТРАПЕЦИИ (-)")
			fmt.Println()

			fmt.Println("Введите число: ")
			fmt.Fscan(os.Stdin, &integrationMethod)
			fmt.Println("Введите величену уменьшения шага")
			fmt.Fscan(os.Stdin, &dh)
			fmt.Println()

			switch integrationMethod {
			case 1:
				resultIntMethod = integratingWithEps(arrayPoint, eps, dh, integratingLeft)
				break
			case 2:
				resultIntMethod = integratingWithEps(arrayPoint, eps, dh, integratingRight)
				break
			case 3:
				// в разработке)
			default:
				fmt.Println("Что-то пошло не так. Попробуйте еще раз, но используй числа только из диапозона от 1 - 3")
				continue

			}
			break

		}

		fmt.Println("Ответ = ", resultIntMethod, "при епселен =", eps)

	}
}

func integratingWithEps(arrayPoint []float32, eps float32, dh float32, f func(arrayPoint []float32) float32) float32 {
	buff := 0
	var result float32 = f(arrayPoint)
	if result == 0 {
		return 0
	}
	var buffResult float32
	var hstep float32 = arrayPoint[1] - arrayPoint[0]

	for ; buff < ITERATION_MAX; buff++ {
		var buffArrayPoint []float32 = makeArrayWhisPoint(arrayPoint[0], arrayPoint[len(arrayPoint)-1], hstep-dh)
		buffResult = f(buffArrayPoint)
		fmt.Println("result = ", result, " buffResult = ", buffResult)
		if math.Abs(float64(result)-float64(buffResult)) < float64(eps) {
			return result
		} else {
			result = buffResult
			continue
		}
	}
	fmt.Println("Не выполнилось условие количества циклов (500). ")
	return 0
}

// функция проверки коректного ввода данных.
func corectData(x1 float32, x2 float32, h float32) bool {
	if (x1 > x2) && (h < 0) && (x2-x1 < h) {
		return true
	}
	return false
}

// функция для вычисления значения в точке
func functionValue(valueX float32) float32 {
	res := (1 / (valueX - 2)) + 10
	return res
}

// функция для вывода таблицы
func printTablePoint(arrayPoint []float32) {

	for _, valui := range arrayPoint {
		fmt.Printf("x = %f\tf(%f) = %f \n", valui, valui, functionValue(valui))
	}
}

// функция разбивает интервал на массив точек
func makeArrayWhisPoint(x1 float32, x2 float32, h float32) []float32 {

	var array []float32
	i := x1

	for ; i < x2; i += h {
		array = append(array, i)
	}
	if i == x2 {
		array = append(array, x2)
	} else {
		array = append(array, x2)
	}
	return array
}

// функция проверки интеграла на расходимость
func checkCorectPoint(arrayPoint []float32, i int) bool {
	if (functionValue(float32(arrayPoint[i])) == float32(math.Inf(-1))) || (functionValue(float32(arrayPoint[i])) == float32(math.Inf(1))) {
		fmt.Println("Невозможно взять интеграл на данном промежутке, так как интеграл расходится")
		fmt.Println()
		return false
	}
	return true
}

// функция вычисления интеграла по ЛЕВОЙ границе
func integratingLeft(arrayPoint []float32) float32 {
	var si float32 = 0

	for i := 0; i < len(arrayPoint)-2; i++ {

		if checkCorectPoint(arrayPoint, i) {
			if functionValue(float32(arrayPoint[i])) < functionValue(arrayPoint[i+1]) {
				si += functionValue(float32(arrayPoint[i])) * (arrayPoint[i+1] - arrayPoint[i])
			} else {
				si += functionValue(float32(arrayPoint[i+1])) * (arrayPoint[i+1] - arrayPoint[i])
			}
		} else {
			return 0
		}
	}
	return si
}

// функция вычисления интеграла по ПРАВОЙ границе
func integratingRight(arrayPoint []float32) float32 {
	var si float32 = 0

	for i := 0; i < len(arrayPoint)-2; i++ {

		if checkCorectPoint(arrayPoint, i) {
			if functionValue(float32(arrayPoint[i])) < functionValue(arrayPoint[i+1]) {
				si += functionValue(float32(arrayPoint[i+1])) * (arrayPoint[i+1] - arrayPoint[i])
			} else {
				si += functionValue(float32(arrayPoint[i])) * (arrayPoint[i+1] - arrayPoint[i])
			}
		} else {
			return 0
		}
	}

	return si
}

// Интегрирование методом трапеции
//func intrgrTrape(arrayPoint float32) float32 {
//интегрирование по трапеции
//	return
//}
