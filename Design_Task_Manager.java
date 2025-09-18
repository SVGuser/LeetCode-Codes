import java.util.*;

class Task implements Comparable<Task> {
    public int userId;
    public int taskId;
    public int priority;

    public Task(int userId, int taskId, int priority) {
        this.userId = userId;
        this.taskId = taskId;
        this.priority = priority;
    }

    @Override
    public int compareTo(Task other) {
        // Higher priority first, then higher taskId
        if (this.priority != other.priority) {
            return Integer.compare(other.priority, this.priority);
        }
        return Integer.compare(other.taskId, this.taskId);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Task)) return false;
        Task other = (Task) obj;
        return this.taskId == other.taskId;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(taskId);
    }
}

class TaskManager {
    private Map<Integer, Task> taskMap;
    private TreeSet<Task> taskSet;

    public TaskManager(List<List<Integer>> tasks) {
        taskMap = new HashMap<>();
        taskSet = new TreeSet<>();
        for (List<Integer> t : tasks) {
            int userId = t.get(0), taskId = t.get(1), priority = t.get(2);
            Task task = new Task(userId, taskId, priority);
            taskMap.put(taskId, task);
            taskSet.add(task);
        }
    }

    public void add(int userId, int taskId, int priority) {
        Task task = new Task(userId, taskId, priority);
        taskMap.put(taskId, task);
        taskSet.add(task);
    }

    public void edit(int taskId, int newPriority) {
        Task oldTask = taskMap.get(taskId);
        if (oldTask != null) {
            taskSet.remove(oldTask);
            Task newTask = new Task(oldTask.userId, taskId, newPriority);
            taskMap.put(taskId, newTask);
            taskSet.add(newTask);
        }
    }

    public void rmv(int taskId) {
        Task task = taskMap.remove(taskId);
        if (task != null) {
            taskSet.remove(task);
        }
    }

    public int execTop() {
        if (taskSet.isEmpty()) return -1;
        Task top = taskSet.pollFirst(); // removes and returns highest priority task
        taskMap.remove(top.taskId);
        return top.userId;
    }
}
