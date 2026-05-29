class MinStack {
    constructor() {
        this.elements = []
        this.minStack = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.elements.push(val)
        const minVal = Math.min(val, this.minStack.length ? this.minStack[this.minStack.length - 1] : val)
        this.minStack.push(minVal)
    }

    /**
     * @return {void}
     */
    pop() {
        this.minStack.pop()
        return this.elements.pop()
    }

    /**
     * @return {number}
     */
    top() {
        return this.elements[this.elements.length - 1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack[this.minStack.length - 1]
    }
}
