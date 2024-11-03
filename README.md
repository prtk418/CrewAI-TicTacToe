# Tic Tac Toe Crew

## Prerequisites
- Python >=3.10 <=3.13
- [Miniconda](https://docs.anaconda.com/miniconda/#quick-command-line-install)
- OpenAI API key ([Get it here](https://platform.openai.com/api-keys))

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

5. **Run the project**
   ```bash
   crewai run
   ```
