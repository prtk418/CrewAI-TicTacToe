# Tic Tac Toe Crew

## Prerequisites
- Python >=3.10 <=3.13
- [Miniconda](https://docs.anaconda.com/miniconda/#quick-command-line-install)
- OpenAI API key ([Get it here](https://platform.openai.com/api-keys))
- Make sure docker is installed on your system and running (for the developer and qa agents to run the generated code)

## Installation Steps

1. **Create and activate conda environment**
   ```bash
   conda create --name tic-tac-toe python=3.12.7
   conda activate tic-tac-toe
   ```

2. **Clone and enter repository**
   ```bash
   git clone git@github.com:prtk418/CrewAI-TicTacToe.git
   cd CrewAI-TicTacToe
   ```

3. **Install dependencies**
   ```bash
   pip install crewai
   crewai install
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   vi .env    # Add your OpenAI API key here
   ```

## Run the project

1. Start the crew:
   ```bash
   crewai run
   ```

2. Execute generated python code
   ```bash
   python src/tic_tac_toe/game.py
   ```

