class Node {
    constructor(value){
        this.value = value
        this.next = null
    }
}
class LinkedList {
    constructor() {
        this.head = this.tail = null
        this.length = 0
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        if(index >= this.length || index < 0){
            return -1
        }
        let i = 0
        let curr = this.head
        while(i < index && curr){
            curr = curr.next
            i++
        }
        return curr?.value
    }


    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        const newNode = new Node(val)
        newNode.next = this.head
        this.head = newNode
        if(!this.length){
            this.tail = this.head
        }
        this.length++
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        const newNode = new Node(val)
        if(!this.length){
            this.head = this.tail = newNode
            this.length++
            return 
        }
        if(this.tail){
            this.tail.next = newNode
        }
        this.tail = newNode
        this.length++
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        // A
        // A -> B
        // A -> B -> C
        if(index >= this.length || index < 0){
            return false
        }

        let curr = this.head
        let prev = null
        let i = 0
        while(i < index && curr){
            prev = curr
            curr = curr.next
            i++
        }
        
        if(prev){
            prev.next = curr.next
        }
        if(this.head === curr){
            this.head = curr.next
        }
        if(this.tail === curr){
            this.tail = prev
        }
        this.length--
        return true
    }

// 5, 2, 1, 3, 4
// 5, 2, 3, 4 
// 2, 3, 4
// 6, 2, 3, 4
// 6, 2, 3, 4, 7
    /**
     * @return {number[]}
     */
    getValues() {
        let items = []
        let curr = this.head
        while(curr){
            items.push(curr.value)
            curr = curr.next
        }
        return items
    }
}
