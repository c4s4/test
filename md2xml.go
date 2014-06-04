package main

import (
    "os"
    "github.com/russross/blackfriday"
    "os/exec"
    "io/ioutil"
    "bytes"
    "io"
    "fmt"
)

func processXslt(xslFile string, input []byte) {
    command := exec.Command("xsltproc", xslFile, "-")
    stdin, err := command.StdinPipe()
    if err != nil {
        panic(err)
    }
    stdout, err := command.StdoutPipe()
    if err != nil {
        panic(err)
    }
    err = command.Start()
    if err != nil {
        panic(err)
    }
    io.Copy(stdin, bytes.NewBuffer(input))
    io.Copy(os.Stdout, stdout)
    err = command.Wait()
    if err != nil {
        panic(err)
    }
}

func main() {
    for _, filename := range os.Args[1:len(os.Args)] {
        file, err := os.Open(filename)
        if err != nil {
            panic(err)
        }
        input, err := ioutil.ReadAll(file)
        if err != nil {
            panic(err)
        }
        output := blackfriday.MarkdownCommon([]byte(input))
        fmt.Println(string(output))
        processXslt("md2xml.xsl", output)
    }
}
