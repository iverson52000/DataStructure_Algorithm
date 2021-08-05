package main

import (
	"fmt"
)

func modify(arr *[]int) {
	*arr = append((*arr), 5)
}

func main() {
	input := []int{1, 2, 3}
	modify(&input)
	fmt.Println(input)

}
