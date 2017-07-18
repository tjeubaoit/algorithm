package main
import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
)

func climb(n int, minStep int, maxStep int, sub []int) int {
    count := 0    
    for i := minStep; i <= maxStep; i++ {
        if i == n { 
            count++
        } else if i > n { 
            break 
        } else {
            if sub[n-i] != -1 {
                count += sub[n-i]
            } else {
                count += climb(n-i, minStep, maxStep, sub)    
            }                                        
        }
    }
    sub[n] = count
    return count
}

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT    
    reader := bufio.NewReader(os.Stdin)
    text, _ := reader.ReadString('\n')
    s, _ := strconv.Atoi(text[:len(strings.TrimSpace(text))])
    
    for i := 0; i < s; i++ {
        text, _ := reader.ReadString('\n')
        n, _ := strconv.Atoi(text[:len(strings.TrimSpace(text))])
        
        sub := make([]int, n+1, n+1)
        for j := 0; j < n; j++ {
            sub[j] = -1
        }
        fmt.Println(climb(n, 1, 3, sub))
    }
}
