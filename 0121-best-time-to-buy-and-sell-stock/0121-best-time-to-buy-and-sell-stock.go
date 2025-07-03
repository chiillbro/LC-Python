func maxProfit(prices []int) int {
    // n := len(prices)
    buy := prices[0]

    profit := 0
    for _, val := range prices {
        if val > buy {
            profit = max(profit, val - buy)
        } else {
            buy = val
        }
    }

    return profit
}