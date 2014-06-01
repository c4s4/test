package main

import "github.com/russross/blackfriday"

const (
    input = `# This is a test

A blank line.

## Second level title

Some *random* text, **nothing** important!`
)

func main() {
    output := blackfriday.MarkdownBasic(input)
    println(output)
}
