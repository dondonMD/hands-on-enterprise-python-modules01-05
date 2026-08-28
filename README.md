# Hands-On Enterprise Application Development with Python

## Course section: Modules 01-05

This student repository intentionally contains only Modules 01-05 of the Northwind Orders course. It begins after the orientation module and stops before the concurrency modules. Work through the modules in order: each is a self-contained activity, but together they show how a small order-management system becomes easier to change and able to handle more data.

## Prerequisites

- Windows with PowerShell.
- Git.
- Python 3.12 or newer. The course targets Python 3.14, but the supplied activities run on Python 3.12+.
- Visual Studio Code, recommended for editing the activity files.

No Docker, database server, Redis server, SQLAlchemy, or FastAPI is required for these five supplied activities. Module 5 uses in-memory fakes so the data-access lessons can run locally.

## Clone the repository

Open **PowerShell** in the folder where you keep projects, then run:

```powershell
git clone https://github.com/dondonMD/hands-on-enterprise-python-modules01-05.git
cd hands-on-enterprise-python-modules01-05
```

All remaining commands in this README are run from this repository's root folder unless a command says otherwise.

## Windows and VS Code setup

From the repository root in PowerShell, check that you are in the expected folder and that Python is available:

```powershell
Get-Location
python --version
```

The location should end in `hands-on-enterprise-python-modules01-05`, and Python must report 3.12 or newer.

To open the repository in VS Code, use **File > Open Folder** and select this folder. If the `code` command is installed, you can instead run:

```powershell
code .
```

## Create and activate your virtual environment

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

After activation, the PowerShell prompt begins with `(.venv)`. Keep that PowerShell window open while you work.

If PowerShell blocks the activation script, run this command in the same PowerShell window, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

This bypass applies only to the current PowerShell window.

## Install dependencies

With `(.venv)` visible in the prompt, run:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Verify the environment

Run these commands from the repository root, with the virtual environment activated:

```powershell
python --version
python -c "import sys; print(sys.executable)"
python -m pytest --version
Get-Location
```

The Python executable path must include `hands-on-enterprise-python-modules01-05\.venv\Scripts\python.exe`. If it does not, activate the environment again before running tests.

## Running tests

Run tests from the repository root. Use one module command at a time; do not run all module test folders in one pytest invocation because several modules use the same test filename.

```powershell
python -m pytest module01-architecture-foundations\tests -v
python -m pytest module02-design-patterns-creational-structural\tests -v
python -m pytest module03-design-patterns-behavioral-architectural\tests -v
python -m pytest module04-data-intensive-structures-memory\tests -v
python -m pytest module05-data-intensive-databases-caching\tests -v
```

If you prefer not to activate the environment, stay in the repository root and replace `python` in the commands above with `.\.venv\Scripts\python.exe`.

## Study order

1. **Module 01 - Foundations of Enterprise Application Architecture:** Refactor a tangled shop script into domain, infrastructure, and API layers, keeping dependencies directed inward.
2. **Module 02 - Design Patterns I: Creational & Structural Patterns:** Use Factory and Adapter so modern and legacy payment providers share one payment interface.
3. **Module 03 - Design Patterns II: Behavioral & Architectural Patterns:** Use Strategy, Observer, dependency injection, and repository ideas to make pricing and reactions to orders replaceable.
4. **Module 04 - Data-Intensive Applications I: Efficient Data Structures & Memory:** Replace eager CSV loading with streaming and batching so large inputs do not require all data in memory.
5. **Module 05 - Data-Intensive Applications II: Databases, Batching & Caching at Scale:** Detect and remove an N+1 access pattern, use keyset pagination, and add read-through caching.

Together, these modules move Northwind Orders from a hard-to-change script toward a system with clear boundaries, adaptable behavior, and scalable data access.

## Student workflow

For every module:

1. Read that module's `README.md`.
2. Inspect the starter code in its `activity` folder.
3. Run the module's test command and read the failure or collection error.
4. Implement only the requested activity.
5. Run the same test command again.
6. When all tests pass, reread the module README and explain to yourself why the implementation solves the stated engineering problem.
7. Come to class prepared to discuss the trade-off, not merely the syntax.

## Important testing rule

Initial failures are intentional. The activities are starter scaffolds and include TODOs and `NotImplementedError` calls. In Module 01, tests initially stop at collection because the requested domain/repository/API objects have not been defined yet. That is expected.

Success means:

1. The environment starts and pytest is found.
2. You see the expected unfinished starting state.
3. You complete the activity.
4. The module's complete test suite passes.

Expected initial state:

| Module | Starting state | Completed state |
|---|---|---|
| 01 | Test collection cannot import the not-yet-implemented domain/repository/API objects. | All 4 tests pass. |
| 02 | 5 tests fail because the adapter and factory raise `NotImplementedError`. | All 5 tests pass. |
| 03 | 4 tests fail because pricing, events, and checkout are unfinished. | All 4 tests pass. |
| 04 | 5 tests fail because streaming and batching are unfinished. | All 5 tests pass. |
| 05 | 7 tests fail because eager loading, pagination, and caching are unfinished. | All 7 tests pass. |

## Troubleshooting

### `Activate.ps1` is blocked

Use the process-only execution-policy command in the virtual-environment section, then activate again.

### `No module named pytest`

Your virtual environment is probably not active, or dependencies were not installed. Confirm `(.venv)` is in the prompt, then run:

```powershell
python -m pip install -r requirements.txt
```

### The wrong Python interpreter is running

Run:

```powershell
python -c "import sys; print(sys.executable)"
```

It must show the `.venv` inside this repository. In VS Code, select that same `.venv` interpreter from **Python: Select Interpreter**.

### Pytest cannot find the tests or imports fail unexpectedly

Run `Get-Location`. You must be in the repository root and use the exact module-specific command shown above. The initial Module 01 import/collection failure is intentional; other unexpected import errors usually mean the command was run from the wrong directory or wrong Python interpreter.

## Repository rule

Do not commit `.venv`, `__pycache__`, `.pytest_cache`, `.pyc` files, or personal VS Code settings. The included `.gitignore` excludes them.
