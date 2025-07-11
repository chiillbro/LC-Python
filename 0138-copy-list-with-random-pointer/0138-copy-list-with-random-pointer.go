/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    oldToNew := make(map[*Node]*Node)

    cur := head

    for cur != nil {
        newNode := &Node{cur.Val, nil , nil}
        oldToNew[cur] = newNode
        cur = cur.Next
    }

    cur = head

    for cur != nil {
        newNode := oldToNew[cur]
        if cur.Next != nil {
            newNode.Next = oldToNew[cur.Next]
        }
        
        if cur.Random != nil {
            newNode.Random = oldToNew[cur.Random]
        }
        cur = cur.Next
    }


    return oldToNew[head]
}