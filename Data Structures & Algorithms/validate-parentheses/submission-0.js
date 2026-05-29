class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = new Stack()
        const pair = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        for(let i = 0; i < s.length; i++){
            if(stack.length() && pair[stack.peek()] === s[i]){
               stack.pop()
            } else {
                stack.push(s[i])
            } 
        }
        return stack.length() === 0
    }
}

class Stack {
    constructor(){
        this.elements = []
    }

    length(){
        return this.elements.length
    }
    
    peek(){
        return this.elements[this.elements.length - 1]
    }

    push(item){
        this.elements.push(item)
    }

    pop(){
        return this.elements.pop()
    }
}