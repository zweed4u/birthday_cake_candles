package main

import (
	"fmt"
	"math"
)

// O(2n)
func birthdayCakeCandles(ar []int) int {
	maxHeight := 0
	for _, candle := range ar {
		maxHeight = int(math.Max(float64(candle), float64(maxHeight)))
	}
	numberOfTallestCandle := 0
	for _, candle := range ar {
		if candle == maxHeight {
			numberOfTallestCandle += 1
		}
	}
	fmt.Println(numberOfTallestCandle)
	return numberOfTallestCandle

}

func main() {
	birthdayCakeCandles([]int{3, 2, 1, 3})
}
