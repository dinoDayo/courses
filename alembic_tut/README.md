## Following tutorial for alembic found online src linked below
- [tutorial source linked here](https://makimo.com/blog/connect-to-postgresql-with-sqlalchemy-and-asyncio/)

### An overview of each file's purpose:
    - `database.py`: This file provides a schema for alembic to apply to the postgres database
    - `env.py`: This file provides tells alembic how to access the postgres database
    - `alembic revision --autogenerate -m "Add Tutorial model"`: This command initiates the autogenerated code which is used to upgrade the existing database schema
    - `alembic upgrade head`: This command applies the revision logic generated in the command above to the database, creating the defined schemas in postgres and updating the `alembic_version.head` column to reflect the current migration version.
    - `ad6b803fe05d_add_tutorial_model.py`: This is the autogenerated migration code which is used to upgrade the existing database schema from its current state to the state passed to the `env.py > target_metadata` field.
    - `tutorial_dto.py`: This class allows us to create data entries that can passed between the python context and the database context with predefined default values and type annotations for each field.
    - `services.py`: This class demonstrates how we can create, read, update and delete objects within the postgres database. Everything up until this point is preparing the schemas. The `alembic_tutorial.py` file allows us to actually edit the data with the database.
    - `app.py`: This file allows us to interact with the async crud application we have created via a starlette application.
    - NOTE: Consecutive schema edits and additions are relatively simple and follow a 3-command order of operations. Documentation on this workflow can be found [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-second-migration).