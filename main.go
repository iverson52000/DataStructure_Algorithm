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

func numSquares(n int) int {
	res := make([]int, n+1)

	for i := 1; i <= n; i++ {
		res[i] = n

		for j := 1; j*j <= i; j++ {
			if res[i-(j*j)]+1 < res[i] {
				res[i] = res[i-(j*j)] + 1
			}
		}
	}

	return res[n]
}
