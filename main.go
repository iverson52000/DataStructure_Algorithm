package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())

	go worker(ctx, "worker1")
	go worker(ctx, "worker2")
	go worker(ctx, "worker3")

	time.Sleep(5 * time.Second)
	fmt.Println("stop the gorutine")
	cancel()
	time.Sleep(5 * time.Second)
}

func findDuplicate(nums []int) int {
	m := make([]int, len(nums))

	for _, num := range nums {
		m[num]++
		if m[num] > 1 {
			return num
		}
	}

	return -1
}
