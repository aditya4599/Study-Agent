from dataclasses import dataclass

@dataclass

class StudyTask:

    topic: str

    completed: bool = False

class StudyAgent:

    def __init__(self, student_name: str):

        self.student_name = student_name

        self.tasks: list[StudyTask] = []

    def add_task(self, topic: str) -> None:

        self.tasks.append(StudyTask(topic=topic))

    def get_progress(self) -> dict:

        completed = sum(task.completed for task in self.tasks)

        total = len(self.tasks)

        return {

            "student": self.student_name,

            "completed": completed,

            "total": total,

            "percentage": round((completed / total) * 100, 2) if total else 0,

        }

if __name__ == "__main__":

    agent = StudyAgent("Student")

    agent.add_task("Learn Python")

    agent.add_task("Learn APIs")

    agent.add_task("Learn AI Agents")

    print(agent.get_progress())
    
def complete_task(self, index: int) -> None:
    if 0 <= index < len(self.tasks):
        self.tasks[index].completed = True

def get_tasks(self) -> list[dict]:
    return [
        {
            "topic": task.topic,
            "completed": task.completed,
        }
        for task in self.tasks
    ]
def get_progress(self) -> dict:
    completed = sum(task.completed for task in self.tasks)
    total = len(self.tasks)

    return {
        "student": self.student_name,
        "completed": completed,
        "total": total,
        "percentage": round(
            (completed / total) * 100, 2
        ) if total else 0,
    }
def create_study_plan(self, topics: list[str]) -> None:
    for topic in topics:
        self.add_task(topic)