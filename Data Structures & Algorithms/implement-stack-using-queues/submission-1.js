class Node {
    constructor(val){
        this.value = val
        this.next = null
        this.prev = null
    }
}

class MyStack {
    constructor() {
        this.dummyHead = new Node(-1)
        this.dummyTail = new Node(-1)
        this.dummyHead.next = this.dummyTail
        this.dummyTail.prev = this.dummyHead
    }

    /**
     * @param {number} x
     * @return {void}
     */
    push(x) {
        const newNode = new Node(x)
        newNode.next = this.dummyTail
        newNode.prev = this.dummyTail.prev
        this.dummyTail.prev.next = newNode
        this.dummyTail.prev = newNode
    }

    /**
     * @return {number}
     */
    pop() {
        const target = this.dummyTail.prev
        target.prev.next = this.dummyTail
        this.dummyTail.prev = target.prev
        return target.value
    }

    /**
     * @return {number}
     */
    top() {
        return this.dummyTail.prev.value
    }

    /**
     * @return {boolean}
     */
    empty() {
        return this.dummyHead.next === this.dummyTail
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
