# SQLModel Foreign Key Relationship

created: 2025-03-31T15:48:19.061844Z  uuid: 21ab027a-6623-4fd3-9ccc-d22ca9d2277b  export: old
messages: 2  total_chars: 3494  human_chars: 2422


---
**HUMAN** (2025-03-31T15:48):

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine
class HeroTeamLink(SQLModel, table=True):
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name="Spider-Boy", secret_name="Pedro Parqueador", teams=[team_preventers]
        )
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)
        print("Deadpond:", hero_deadpond)
        print("Deadpond teams:", hero_deadpond.teams)
        print("Rusty-Man:", hero_rusty_man)
        print("Rusty-Man Teams:", hero_rusty_man.teams)
        print("Spider-Boy:", hero_spider_boy)
        print("Spider-Boy Teams:", hero_spider_boy.teams)
def main():
    create_db_and_tables()
    create_heroes()
if **name** == "__main__":
    main()


for foreign_key="team.id", i don't see team anywhere but only Team, why does this work

---
**ASSISTANT** (2025-03-31T15:48):

 The foreign key reference in `foreign_key="team.id"` works because SQLModel (and SQLAlchemy underneath it) automatically converts your Python class names to lowercase for table names by default.

When you define a class with `table=True` like:

```python
class Team(SQLModel, table=True):
    ...
```

SQLModel creates a database table with the name "team" (lowercase version of your class name). This automatic conversion follows SQLAlchemy's naming convention.

Similarly, your `Hero` class creates a table named "hero", and the `HeroTeamLink` class creates a table named "heroteamlink".

So when you use `foreign_key="team.id"`, you're correctly referencing the database table name "team" (not the Python class name "Team").

If you wanted to explicitly specify a different table name, you could do so with the `__tablename__` attribute:

```python
class Team(SQLModel, table=True):
    __tablename__ = "teams"  # This would override the default "team"
    ...
```

In that case, you would need to update your foreign key references to match: `foreign_key="teams.id"`.
