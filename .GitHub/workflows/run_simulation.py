name: Boundary-Horizon CI/CD

# Define when the workflow should trigger
on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      # 1. Checkout your repository code onto the runner
      - name: Checkout Repository
        uses: actions/checkout@v4

      # 2. Set up Python environment
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      # 3. Install dependencies (like numpy used in your simulations)
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install numpy matplotlib plotly

      # 4. Run your simulation scripts
      - name: Run Dynamic Horizon Simulation
        run: python dynamic_horizon_simulation.py

      - name: Run Refraction Simulation
        run: python refraction_simulation.py
