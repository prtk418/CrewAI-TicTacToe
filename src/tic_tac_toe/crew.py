from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class TicTacToeCrew:
    """Tic Tac Toe Development Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["product_manager"]
        )

    @agent
    def game_designer(self) -> Agent:
        return Agent(
            config=self.agents_config["game_designer"]
        )

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config["developer"],
            allow_code_execution=True,
            allow_delegation=True
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["qa_engineer"],
            allow_code_execution=True,
            allow_delegation=True
        )

    @task
    def define_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["define_requirements"]
        )

    @task
    def design_mechanics(self) -> Task:
        return Task(
            config=self.tasks_config["design_mechanics"]
        )

    @task
    def implement_game(self) -> Task:
        return Task(
            config=self.tasks_config["implement_game"],
            output_file="src/tic_tac_toe/game.py"
        )

    @task
    def test_game(self) -> Task:
        return Task(
            config=self.tasks_config["test_game"]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Tic Tac Toe Development Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
        )