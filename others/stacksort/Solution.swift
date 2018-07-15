
var stackOdd: [Int] = [3, -6, 1, 5, 9, 16, 11, 4, 7, 15, 8]
var stackEven = [Int]()
let size = stackOdd.count

for i in 0...(size / 2) {
    var min = stackOdd.popLast()!
    while stackOdd.count > i {
        let top = stackOdd.popLast()!
        if top < min {
            stackEven.append(min)
            min = top
        } else {
            stackEven.append(top)
        }
    }
    stackOdd.append(min)
    
    var max = stackEven.popLast()!
    while stackEven.count > i {
        let top = stackEven.popLast()!
        if top > max {
            stackOdd.append(max)
            max = top
        } else {
            stackOdd.append(top)
        }
    }
    stackEven.append(max)
}

while !stackEven.isEmpty {
    let count = stackEven.count
    stackOdd.append(stackEven.popLast()!)
}

for x in stackOdd {
    print(x, terminator: ", ")
}