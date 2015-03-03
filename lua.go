package main

import "github.com/yuin/gopher-lua"

func main() {
	L := lua.NewState()
	defer L.Close()
	L.DoString(`
print("Hello World!")
l = "foo"
`)
	println(L.GetGlobal("l").String())
}
