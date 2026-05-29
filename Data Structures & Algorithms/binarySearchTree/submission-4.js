class Node {
    constructor(val, key, left=null, right=null){
        this.key = key
        this.val = val
        this.left = left
        this.right = right
    }
}
class TreeMap{
    constructor() {
        this.root = null
    }

    /**
     * @param {number} key
     * @param {number} val
     * @returns {void}
     */
    insert(key, val) {
        if(!this.root){
            this.root = new Node(val, key)
            return 
        }
        const insertInPosition = (node, key) =>{
            if (!node){
                return new Node(val, key)
            }
            if (node.key === key ){
                node.val = val
                return node
            }
            if (node.key > key){
                node.left = insertInPosition(node.left, key)
            }else{
                node.right = insertInPosition(node.right, key)
            }
            return node
        }
        this.root = insertInPosition(this.root, key)
        
    }

    /**
     * @param {number} key
     * 
     * @returns {number}
     */
    get(key) {
        const findNode = (node, key)=>{
            
            if(!node){
                return -1
            }
            
            if(node.key === key){
                return node.val
            }
            if(key < node.key){
                return findNode(node.left, key)
            }else{
                return findNode(node.right, key)
            }
        }
        return findNode(this.root, key)
    }

    /**
     * @returns {number}
     */
    getMin() {
        if(!this.root){
            return -1
        }
        let node = this.root
        while(node.left){
            node = node.left
        }
        return node.val
    }

    /**
     * @returns {number}
     */
    getMax() {
        if(!this.root){
            return -1
        }
        let node = this.root
        while(node.right){
            node = node.right
        }
        return node.val
    }

    /**
     * @param {number} key
     * @returns {void}
     */
    remove(key) {
        const getMinFrom = (node)=> {
            while(node.left){
                node = node.left
            }
            return node
        }
        const removeRecurse = (node, key)=> {
            if(!node){
                return null
            }

            if(node.key === key){
                if(!node.left && !node.right){
                    return null
                }

                if(node.left && node.right){
                    const successor = getMinFrom(node.right)
                    
                    node.key = successor.key
                    node.val = successor.val
                    node.right = removeRecurse(node.right, successor.key)
                    return node
                }

                if(node.left){
                    return node.left
                }
                if(node.right){
                    return node.right
                }
            }

            if (key < node.key){
                node.left = removeRecurse(node.left, key)
            }else{
                node.right = removeRecurse(node.right, key)
            }
            
        }
        this.root = removeRecurse(this.root, key)
    }

    /**
     * @returns {number[]}
     */
    getInorderKeys() {
        const traverseInOrder = (node, path) => {
            if(!node){
                return 
            }
            
            traverseInOrder(node.left, path)
            path.push(node.key)
            traverseInOrder(node.right, path)
        }
        const path = []
        traverseInOrder(this.root, path)
        return path
    }
}
