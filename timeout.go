package main

import (
	"fmt"
	"net"
	"net/http"
	"time"
)

func NewClient(timeout time.Duration) *http.Client {
	transport := &http.Transport{
		Dial: func(network, address string) (net.Conn, error) {
			connection, err := net.DialTimeout(network, address, timeout*time.Millisecond)
			if err != nil {
				return nil, err
			}
			deadline := time.Now().Add(timeout * time.Millisecond)
			connection.SetDeadline(deadline)
			return connection, nil
		},
	}
	client := &http.Client{Transport: transport}
	return client
}

func main() {
	client := NewClient(0)
	start := time.Now()
	response, err := client.Get("http://google.com")
	if err != nil {
		fmt.Println("ERROR")
		fmt.Println("error:", err.Error())
		if response != nil {
			fmt.Println("response", response)
		}
	} else {
		fmt.Println("OK")
	}
	fmt.Println(fmt.Sprintf("duration: %v", time.Since(start)))
}
