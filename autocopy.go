package main

import (
	"golang.org/x/exp/inotify"
	"log"
	"os"
	"fmt"
	"strings"
)

const (
	HELP = `autocopy src_dir dst_dir exts
Copy all files that appear with given extension in src_dir to a given directory:
src_dir   Watched directory for new files
dst_dir   Destination directory for copy
exts      File extensions to copy`
)

func watch(srcDir, dstDir string, exts []string) {
	extensions := strings.Join(exts, ", ")
	fmt.Printf("Copying files %s from '%s' to '%s'\n",
	           extensions, srcDir, dstDir)
	watcher, err := inotify.NewWatcher()
	if err != nil {
		log.Fatal(err)
	}
	err = watcher.Watch(srcDir)
	if err != nil {
		log.Fatal(err)
	}
	for {
		select {
		case ev := <-watcher.Event:
			log.Println("event:", ev)
		case err := <-watcher.Error:
			log.Println("error:", err)
		}
	}
}

func main() {
	if len(os.Args) < 4 {
		fmt.Println(HELP)
		os.Exit(1)
	}
	srcDir := os.Args[1]
	dstDir := os.Args[2]
	exts := os.Args[3:]
	watch(srcDir, dstDir, exts)
}
