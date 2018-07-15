package main

import (
	"fmt"
)

type Node struct {
	count int,
	value int,
	children []*Node
}

func find(node *Node, min int, max int) []*Node {
	if min == -1 {
		return node.children
	}

	if max == -1 {
		max = min
	}

	results = make([]*Node)
	for _, c := range node.children {
		if c.value >= min && c.value <= max {
			results.append(c)
		}
	}

	return results
}

func insert(root *Node, date int, pid int, cid int, sid int, rid int) {

}

func query(root *Node, ds int, de int, pid int, cid int, sid int, rid int) {
	
}

func main() {

}