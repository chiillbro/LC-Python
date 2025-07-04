type MinStack struct {
    stack []int
    mins []int
}


func Constructor() MinStack {
   return MinStack{
    stack: []int{},
    mins: []int{},
   }
}


func (this *MinStack) Push(val int)  {
    this.stack = append(this.stack, val)

    if len(this.mins) == 0 || val <= this.mins[len(this.mins)-1] {
        this.mins = append(this.mins, val)
    }
}


func (this *MinStack) Pop()  {
    top := this.stack[len(this.stack) - 1]

    this.stack = this.stack[:len(this.stack) - 1]

    if this.mins[len(this.mins) - 1] == top {
        this.mins = this.mins[:len(this.mins) - 1]
    }
}


func (this *MinStack) Top() int {
    return this.stack[len(this.stack) - 1]
}


func (this *MinStack) GetMin() int {
    return this.mins[len(this.mins) - 1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */