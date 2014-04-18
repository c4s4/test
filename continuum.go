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
    "os"
    "fmt"
    "os/exec"
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

type Build struct {
    Success bool
    Output string
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

func buildModule(name string, config Config) Build {
    fmt.Printf("Building '%s'... ", name)
    // go in build directory
    err := os.Chdir(config.Directory)
    if err != nil {
        return Build{ Success: false, Output: err.Error() }
    }
    // delete module directory if it already exists
    if _, err := os.Stat(name); err == nil {
        os.RemoveAll(name)
    }
    // git clone the module repository
    cmd := exec.Command("git", "clone", config.Modules[name].Url)
    output, err := cmd.CombinedOutput()
    if err != nil {
        fmt.Println("ERROR")
        return Build{
            Success: false,
            Output: string(output),
        }
    } else {
        os.Chdir(name)
        // run the build command
        cmd := exec.Command("bash", "-c", config.Modules[name].Command)
        output, err := cmd.CombinedOutput()
        if err != nil {
            fmt.Println("ERROR")
            return Build {
                Success: false,
                Output: string(output),
            }
        } else {
            fmt.Println("OK")
            return Build{
                Success: true,
                Output: string(output),
            }
        }
    }
}

func main() {
    config := loadConfig("config.yml")
    builds := make(map[string] Build)
    success := true
    for module := range(config.Modules) {
        build := buildModule(module, config)
        builds[module] = build
        success = success && build.Success
    }
    if success {
        fmt.Println("OK")
    } else {
        fmt.Println("ERROR:")
        for module := range(builds) {
            fmt.Println("===================================")
            fmt.Println(module)
            fmt.Println("-----------------------------------")
            fmt.Println(builds[module].Output)
            fmt.Println("-----------------------------------")
          }
    }
}

