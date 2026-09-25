# Defining Circular SQLModel Relationships

created: 2025-03-31T15:15:30.818853Z  uuid: 9a1299ac-7c74-4f61-b561-6b82c77b1ac0  export: old
messages: 4  total_chars: 7094  human_chars: 4167


---
**HUMAN** (2025-03-31T15:15):

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine
class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="team")
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")
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
            name="Deadpond", secret_name="Dive Wilson", team=team_z_force
        )
        hero_rusty_man = Hero(
            name="Rusty-Man", secret_name="Tommy Sharp", age=48, team=team_preventers
        )
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)
        print("Created hero:", hero_deadpond)
        print("Created hero:", hero_rusty_man)
        print("Created hero:", hero_spider_boy)
        hero_spider_boy.team = team_preventers
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_spider_boy)
        print("Updated hero:", hero_spider_boy)
        hero_black_lion = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
        hero_sure_e = Hero(name="Princess Sure-E", secret_name="Sure-E")
        team_wakaland = Team(
            name="Wakaland",
            headquarters="Wakaland Capital City",
            heroes=[hero_black_lion, hero_sure_e],
        )
        session.add(team_wakaland)
        session.commit()
        session.refresh(team_wakaland)
        print("Team Wakaland:", team_wakaland)
        hero_tarantula = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
        hero_dr_weird = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
        hero_cap = Hero(
            name="Captain North America", secret_name="Esteban Rogelios", age=93
        )
        team_preventers.heroes.append(hero_tarantula)
        team_preventers.heroes.append(hero_dr_weird)
        team_preventers.heroes.append(hero_cap)
        session.add(team_preventers)
        session.commit()
        session.refresh(hero_tarantula)
        session.refresh(hero_dr_weird)
        session.refresh(hero_cap)
        print("Preventers new hero:", hero_tarantula)
        print("Preventers new hero:", hero_dr_weird)
        print("Preventers new hero:", hero_cap)
def main():
    create_db_and_tables()
    create_heroes()
if **name** == "__main__":
    main()



for     heroes: list["Hero"] = Relationship(back_populates="team"), there is no team  or heroes defined, why does it work?

---
**ASSISTANT** (2025-03-31T15:15):

 The code works despite the apparent circular reference in the relationship definition because of how Python and SQLModel handle type hints and relationships.

Let's break down what's happening with this line:
```python
heroes: list["Hero"] = Relationship(back_populates="team")
```

1. **Forward references with string literals**: The `"Hero"` in quotation marks is a string literal used as a forward reference. Python's type hinting system allows using string literals to reference types that haven't been fully defined yet. This is specifically designed to handle circular references like this one.

2. **Lazily evaluated relationships**: SQLModel (which is built on SQLAlchemy) doesn't immediately try to resolve these relationships when the class is defined. Instead, it stores the relationship information and resolves it later when the metadata is processed.

3. **Order of resolution**: When `SQLModel.metadata.create_all(engine)` is called, SQLModel goes through all the models it knows about, resolves these string references, and creates the appropriate database schema.

This pattern is common in ORM frameworks because database relationships are often bidirectional (a team has many heroes, and a hero belongs to a team), which naturally creates circular references in the code.

The same technique is used in the `Hero` class with:
```python
team: Team | None = Relationship(back_populates="heroes")
```

Together, these definitions create a bidirectional relationship between `Team` and `Hero` that SQLModel can properly translate into database foreign keys and relationships.

---
**HUMAN** (2025-03-31T15:41):

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select, text
class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="team", passive_deletes="all")
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(
        default=None, foreign_key="team.id", ondelete="SET NULL"
    )
    team: Team | None = Relationship(back_populates="heroes")
# Code below omitted 👇


what is this passive_deletes="all"?

---
**ASSISTANT** (2025-03-31T15:41):

 `passive_deletes="all"` is a parameter in SQLAlchemy (which SQLModel is built on) that affects how cascading deletes are handled in the relationship.

When set to `"all"`, it tells SQLAlchemy to rely entirely on the database's foreign key ON DELETE behavior instead of issuing additional DELETE statements from Python code.

In your specific example:

```python
heroes: list["Hero"] = Relationship(back_populates="team", passive_deletes="all")
```

Combined with the `ondelete="SET NULL"` setting in the Hero model:

```python
team_id: int | None = Field(
    default=None, foreign_key="team.id", ondelete="SET NULL"
)
```

This configuration means:

1. When a Team is deleted, SQLAlchemy won't issue additional DELETE statements for related Hero objects
2. Instead, it will rely on the database's ON DELETE SET NULL constraint to set the `team_id` to NULL in related Hero records
3. The heroes won't be deleted, just disassociated from the deleted team

Without `passive_deletes="all"`, SQLAlchemy would fetch all related heroes when a team is deleted and issue additional SQL statements to handle the relationship, which can be less efficient.

This approach is particularly useful for optimizing performance with large datasets and when you want to ensure your database's foreign key constraints handle the relationship maintenance.
