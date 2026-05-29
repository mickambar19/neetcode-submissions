class MinStack {
    constructor() {
        this.elements = []
        this.minIdx = null
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.elements.push(val)
        if(this.minIdx === null || val < this.elements[this.minIdx]){
            this.minIdx = this.elements.length - 1
        }
    }

    /**
     * @return {void}
     */
    pop() {
        const el = this.elements.pop()
        if (this.minIdx === this.elements.length){
            this.minIdx = 0
            for(let i = 1; i < this.elements.length; i++){
                if(this.elements[i] < this.elements[this.minIdx]){
                    this.minIdx = i
                }
            }
        }
        return el
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
        if(!this.elements.length){
            return null
        }
        return this.elements[this.minIdx]
    }
}
