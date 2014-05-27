package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("Hello World!")
    fmt.Println(<-time.After(10*time.Second))
}

