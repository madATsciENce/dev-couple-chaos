// feelings/argue_detector.go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

var triggers = []string{
    "You never listen!",
    "You always do this!",
    "Forget it.",
    "It's fine. (It’s not fine)",
}

func detectArgument() bool {
    rand.Seed(time.Now().UnixNano())
    chance := rand.Float64()
    if chance < 0.3 {
        trigger := triggers[rand.Intn(len(triggers))]
        fmt.Println("🚨 Argument detected:", trigger)
        return true
    }
    return false
}

func main() {
    if detectArgument() {
        fmt.Println("🔥 Fight detected. Logging...")
    } else {
        fmt.Println("🌸 Peaceful day!")
    }
}
