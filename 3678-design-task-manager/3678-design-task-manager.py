class TaskManager:
    from sortedcontainers import SortedSet
    def __init__(self, tasks: List[List[int]]):
        # self.task_to_priority = defaultdict(tuple)
        self.task_to_priority = SortedSet()
        self.task_to_pu = defaultdict(tuple)

        # self.user_to_tp = defaultdict(SortedSet)

        for user_id, task_id, priority in tasks:
            # self.task_to_priority[task_id] = (priority, user_id)
            self.task_to_priority.add((-priority, -task_id))
            self.task_to_pu[task_id] = (priority, user_id)
            # self.user_to_tp[user_id].add((-priority, -task_id))
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # self.task_to_priority[taskId] = (priority, userId)
        # self.user_to_tp[userId].add((-priority, -taskId))

        self.task_to_pu[taskId] = (priority, userId)
        self.task_to_priority.add((-priority, -taskId))

        

    def edit(self, taskId: int, newPriority: int) -> None:
        # prev_task = self.task_to_priority[taskId]
        # prev = (-prev_task[0], -taskId)

        # self.task_to_priority[taskId] = newPriority, prev_task[1]
        # self.user_to_tp[prev_task[1]].remove(prev)

        # self.user_to_tp[prev_task[1]].add((-newPriority, -taskId))

        task = self.task_to_pu[taskId]

        prev = (-task[0], -taskId)

        self.task_to_priority.remove(prev)

        self.task_to_priority.add((-newPriority, -taskId))

        self.task_to_pu[taskId] = (newPriority, task[1])


    def rmv(self, taskId: int) -> None:
        task = self.task_to_pu[taskId]

        to_rmv = (-task[0], -taskId)

        self.task_to_priority.remove(to_rmv)

        self.task_to_pu.pop(taskId)
        # task = self.task_to_priority[taskId]

        # self.task_to_priority.pop(taskId)

        # task_to_remove = (-task[0], -taskId)

        # self.user_to_tp[task[1]].remove(task_to_remove)

        # if len(self.user_to_tp[task[1]]) == 0:
        #     self.user_to_tp.pop(task[1])
        

    def execTop(self) -> int:
        if not self.task_to_priority:
            return -1

        priority, taskId = -self.task_to_priority[0][0], -self.task_to_priority[0][1]
        self.task_to_priority.remove((-priority, -taskId))
        user_id = self.task_to_pu[taskId][1]
        self.task_to_pu.pop(taskId)

        return user_id
        # task_to_execute = (-1, None, None)
        # for user_id in self.user_to_tp:
        #     cur_task = self.user_to_tp[user_id][0]
        #     if -cur_task[0] > task_to_execute[0]:
        #         task_to_execute = (-cur_task[0], -cur_task[1], user_id)
        #     elif -cur_task[0] == task_to_execute[0] and task_to_execute[1] and task_to_execute[1] < -cur_task[1]:
        #         task_to_execute = (-cur_task[0], -cur_task[1], user_id)

        
        # if task_to_execute[2] is None:
        #     return -1

        # self.task_to_priority.pop(task_to_execute[1])
        # self.user_to_tp[task_to_execute[2]].remove((-task_to_execute[0], -task_to_execute[1]))

        # if len(self.user_to_tp[task_to_execute[2]]) == 0:
        #     self.user_to_tp.pop(task_to_execute[2])
        
        # return task_to_execute[2]


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()