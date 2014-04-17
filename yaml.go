package main

import "fmt"
import "io/ioutil"

func main() {
    content, error := ioutil.ReadFile("config.yml")
    if error != nil {
        fmt.Println("Error reading config file")
        panic(error)
    }
    fmt.Println(string(content))
}

