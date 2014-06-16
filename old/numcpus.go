package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Printf("Number of CPUs: %d\n", runtime.NumCPU())
}
