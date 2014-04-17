package main

import "fmt"
Import "yaml"

func main() {
    config := yaml.ConfigFile("config.yml")
    fmt.Println(config)
}