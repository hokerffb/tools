package main

import (
	"fmt"
	"log"
	"net"
	"net/rpc"
	"os/exec"
	"strconv"
)

type VMRPCService struct{}

type Args struct {
	VM_id int
	Key   string
}

func run_cmd(cmd string, args ...string) string {
	proc := exec.Command(cmd, args...)

	output, err := proc.Output()
	if err != nil {
		log.Fatal(err)
	}

	return string(output)
}

// RPC function
func (s *VMRPCService) Reset(args *Args, reply *string) error {
	output := ""
	fmt.Println(args.Key)
	if args.Key == "MyID" {
		fmt.Println("Verify key success.")
		*reply = ""
		output = run_cmd("qm", "list")
		fmt.Println(output)
		output = run_cmd("qm", "listsnapshot", strconv.Itoa(VM_id))
		fmt.Println(output)
		output = run_cmd("qm", "rollback", strconv.Itoa(VM_id), "ResetPos")
		fmt.Println(output)
		output = run_cmd("qm", "start", strconv.Itoa(VM_id))
		fmt.Println(output)
		output = run_cmd("qm", "status", strconv.Itoa(VM_id))
		fmt.Println(output)
	} else {
		fmt.Println("Verify key failed.")
	}
	*reply = output
	return nil
}

func main() {
	rpcService := new(VMRPCService)
	rpc.Register(rpcService)

	listener, err := net.Listen("tcp", ":4444")
	if err != nil {
		log.Fatal("Listen error:", err)
	}

	log.Println("RPC server is listening on port 4444...")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal("Accept error:", err)
		}
		go rpc.ServeConn(conn)
	}
}
