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

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func maxSlidingWindow(nums []int, k int) []int {
	res := []int{}
	q := []int{}

	for i := 0; i < len(nums); i++ {
		if len(q) > 0 && q[0] <= i-k {
			q = q[1:]
		}
		for len(q) > 0 && nums[q[len(q)-1]] < nums[i] {
			q = q[:len(q)-1]
		}

		q = append(q, i)
		if i >= k-1 {
			res = append(res, nums[q[0]])
		}
	}

	return res
}
