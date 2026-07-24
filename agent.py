from deploygent import Agent
from deploygent.input import (
    TextInput,
    NumberInput,
    BooleanInput,
    SelectInput,
)
from deploygent.output import TextOutput

agent = Agent(
    name="Testing Agent",
    version="1.0.0",
    description="A sample agent to test the DeployGent SDK."
)


@agent.task
def greet(
    name: TextInput(label="Your Name"),
    age: NumberInput(label="Age"),
    excited: BooleanInput(label="Excited?", required=False),
    language: SelectInput(
        label="Language",
        options=["English", "Spanish", "French"]
    ),
) -> TextOutput:

    greeting = {
        "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour",
    }

    message = f"{greeting.get(language, 'Hello')} {name}! You are {age} years old."

    if excited:
        message += " 🎉 Welcome to DeployGent!"

    return message


if __name__ == "__main__":
    agent.serve()
