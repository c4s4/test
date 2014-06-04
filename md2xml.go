package main

import (
    "os"
    "github.com/russross/blackfriday"
    "os/exec"
    "io/ioutil"
    "fmt"
)

const (
    xslFile = "md2xml.xsl"
)

func processXsl(xslFile, xmlFile string) ([]byte) {
    command := exec.Command("xsltproc", xslFile, xmlFile)
    result, err := command.CombinedOutput()
    if err != nil {
        panic(err)
    }
    return result
}

func markdown2xhtml(filename string) ([]byte) {
    markdown, err := ioutil.ReadFile(filename)
    if err != nil {
        panic(err)
    }
    xhtml := "<xhtml>\n" + string(blackfriday.MarkdownCommon([]byte(markdown))) + "\n</xhtml>"
    return []byte(xhtml)
}

func processFile(filename string) string {
    xhtml := markdown2xhtml(filename)
    xmlFile, err := ioutil.TempFile("/tmp", "md2xml-")
    if err != nil {
        panic(err)
    }
    defer os.Remove(xmlFile.Name())
    ioutil.WriteFile(xmlFile.Name(), xhtml, 0755)
    result := processXsl(xslFile, xmlFile.Name())
    return string(result)
}

func main() {
    for _, filename := range os.Args[1:len(os.Args)] {
        fmt.Println(processFile(filename))
    }
}

