package main

import (
	"fmt"
	"log"
	"net/rpc"
)

type Args struct {
	VM_id int
	Key   string
}

func confirm() bool {
	fmt.Print("All modified files will be lost! \nAre you sure you want to reset the operating system?(y/n) ")

	var input string
	fmt.Scanln(&input)

	if input == "y" {
		return true
	} else {
		return false
	}
}

func main() {
	if !confirm() {
		return
	}

	client, err := rpc.Dial("tcp", "vm-server-ip:4444")
	if err != nil {
		log.Fatal("Reset failed.")
	}

	args := &Args{44, "MyID"}
	var reply string
	err = client.Call("VMRPCService.Reset", args, &reply)
	if err != nil {
		log.Fatal("Reset failed.")
		return
	}

	log.Println("Result:", reply)
}
