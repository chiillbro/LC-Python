type Node struct {
    key, val int
    prev *Node
    next *Node
}

type LRUCache struct {
    capacity int
    cache map[int]*Node
    oldest *Node
    latest *Node
}


func Constructor(capacity int) LRUCache {
    latest, oldest := &Node{0, 0, nil, nil}, &Node{0, 0, nil, nil}
    latest.prev = oldest
    oldest.next = latest
    return LRUCache{
        capacity: capacity,
        cache: make(map[int]*Node),
        latest: latest,
        oldest: oldest,
    }
}


func (this *LRUCache) Get(key int) int {
    if node, ok := this.cache[key]; ok {
        this.Remove(node)
        this.Insert(node)

        return node.val
    }

    return -1
}

func (this *LRUCache) Insert(node *Node) {
    prev, next := this.latest.prev, this.latest
    prev.next, next.prev = node, node
    node.next, node.prev = next, prev
}

func (this *LRUCache) Remove(node *Node) {
    prev, next := node.prev, node.next
    prev.next = next
    next.prev = prev
}

func (this *LRUCache) Put(key int, value int)  {
    if node, exists := this.cache[key]; exists {
        this.Remove(node)
    }

    newNode := &Node{key, value, nil, nil}
    this.Insert(newNode)
    this.cache[key] = newNode

    if len(this.cache) > this.capacity {
        lru := this.oldest.next
        this.Remove(lru)
        delete(this.cache, lru.key)
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */