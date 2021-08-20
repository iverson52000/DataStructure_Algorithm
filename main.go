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

func coinChange(coins []int, amount int) int {
	INF := 65535
	size := amount + 1

	dp := make([]int, size)

	for idx, _ := range dp {
		dp[idx] = INF
	}

	dp[0] = 0

	for i := 1; i <= amount; i += 1 {
		for _, coin := range coins {
			if coin <= i {
				dp[i] = min(dp[i-coin]+1, dp[i])
			}
		}
	}

	if dp[amount] == INF {
		return -1
	} else {
		return dp[amount]
	}

}
