package main

import "github.com/russross/blackfriday"

const (
	input = `# This is a test

A blank line.

## Second level title

Some *random* text, **nothing** important!`
)

func processXslt(xslFile string, xmlFile string) (jsonData []byte, err error) {
	cmd := exec.Cmd{
		Args: []string{"xsltproc", xslFile, xmlFile},
		Env:  os.Environ(),
		Path: "xsltproc",
	}

	jsonString, err := cmd.Output()
	if err != nil {
		return jsonData, err
	}

	fmt.Printf("%s\n", jsonString)

	jsonData = []byte(jsonString)

	return jsonData, err
}

func main() {
	output := blackfriday.MarkdownCommon([]byte(input))
	println(string(output))
}
