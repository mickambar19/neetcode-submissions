class MyDeque {
    constructor() {
        this.head = this.tail = null
        // <- x <- x <- x
        this.length = 0
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        return !this.length
    }

    /**
     * @param {number} value
     */
    append(value) {
        if(!this.length){
            this.head = this.tail = {
                value,
                prev: null
            }
            this.length++
            return 
        }
        const node = {
            value,
            prev: this.tail
        }
        this.tail = node
        this.length++
    }

    /**
     * @param {number} value
     * @return {void}
     */
    appendleft(value) {
        if(!this.length){
            this.head = this.tail = {
                value,
                prev: null
            }
            this.length++
            return 
        }
        const node = {
            value,
            prev: null
        }
        this.head.prev = node
        this.head = node
        this.length++
    }

    /**
     * @return {void}
     */
    pop() {
        if(!this.length){
            return -1
        }

        const el = this.tail
        this.tail = this.tail.prev
        this.length--
        return el.value
    }

    /**
     * @return {number}
     */
    popleft() {
        if(!this.length){
            return -1
        }
        let curr = this.tail
        let prev = null

        while(curr.prev){
            prev = curr
            curr = curr.prev
        }
        const value = curr.value
        curr = null
        this.head = prev
        if(this.head){
            this.head.prev = null
        }
        this.length--
        return value
    }
}
