package main

import "fmt"
import "yaml"

func main() {
    config := yaml.ConfigFile("config.yml")
    fmt.Println(config)
}