# C868_API
API for the C868_Front



to run the API:
enter your virtual environment.
`pip install -r requirements.txt`
cd into src, or wherever the root level is
`uvicorn main:app --reload`


VSCode python linter might be wacked by default.
make sure to source your env first, make sure VSCode identifies that env as the python exe.
install mypy with `pip install mypy`
then use ctrl+shift+p to change linter to mypy.
now type hints and pydantic models should not be erroneously identified as missing.


Note: we're using NEST-like file structure
each module has it's own folder, with the model and service separate from each other.