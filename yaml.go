// Depends on goyaml:
// 
//   go get gopkg.in/yaml.v1
//
// Sample configuration file:
// 
//   directory:  /home/casa/tmp
//   email:
//     smtp_host: smtp.orange.fr
//     recipient: casa@sweetohm.net
//     sender:    casa@sweetohm.net
//     success:   true
//   
//   modules:
//     continuum:
//       url:     https://github.com/c4s4/continuum.git
//       command: |
//         set -e
//         export PATH=/opt/python/current/bin:$PATH
//         virtualenv env --no-site-packages
//         . env/bin/activate
//         pip install -r etc/requirements.txt
//         bee test

package main

import (
    "fmt"
    "io/ioutil"
    "gopkg.in/yaml.v1"
)

type Config struct {
    Directory string
    Email struct {
        SmtpHost string "smtp_host"
        Recipient string
        Sender string
        Success bool
    }
    Modules map[string] struct {
        Url string
        Command string
    }
}

func loadConfig(file string) Config {
    config := Config{}
    text, err := ioutil.ReadFile(file)
    if err != nil {
        panic(err.Error())
    }
    err = yaml.Unmarshal(text, &config)
    if err != nil {
        panic(err.Error())
    }
    return config
}

func main() {
    config := loadConfig("config.yml")
    fmt.Println(config.Email.SmtpHost)
}

