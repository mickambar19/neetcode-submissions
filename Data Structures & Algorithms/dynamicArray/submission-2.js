class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.size = 0
        this.elements = new Array(capacity)
        
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.elements[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.elements[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        let newIdx = this.size
        if(this.capacity === this.size){
            this.resize()
        }
        this.elements[newIdx] = n
        this.size += 1
        // [0, 0, 0] size= 0, cap: 3
        // [1, 0, 0] size= 1, cap: 3
        // [1, 2, 0] size= 2, cap: 3
        // [1, 2, 3] size= 3, cap: 3
        // [1, 2, 3, 8, 0, 0] size= 4, cap: 6
    }

    /**
     * @returns {number}
     */
    popback() {
        const item = this.elements[this.size - 1]
        this.size -= 1
        return item
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity *= 2
        let newArray = new Array(this.capacity)
        for(let i = 0; i < this.size; i++){
            newArray[i] = this.elements[i]
        }
        this.elements = newArray
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.size
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
