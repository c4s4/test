package main

import (
    "fmt"
    "time"
)

func main() {
    println("Hello World!")
    fmt.Println("Hello World!")
    fmt.Println(<-time.After(10*time.Second))
}

