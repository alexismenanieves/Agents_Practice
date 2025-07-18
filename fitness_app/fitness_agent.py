"""
Fitness program - Get your custom plan
======================================
This example demonstrate how to create an AI agent specialized in 
creating fitness programs. Pass your height, weight and age to get your 
custom plan of exercises.
"""

from pathlib import Path
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

exercise_planner = Agent(
    model=Ollama(id='mistral-small3.2:latest', options={"temperature": 0}),
    description="Creates customized workout plan based on user input",
    instructions=[
        "Create a workout plan including warm-ups, main exercises and cool-downs",
        "Adjust workout based on level: beginner, intermediate and expert",
        "Consider weight loss, muscle gain, endurance or flexibility goals",
        "If not mentioned, consider 3 days per week commitment, ", 
        "and home workouts using body weight and minimal equipment", 
        "Provide safety tips and injury prevention advice",
        "Suggest progress tracking methods for motivation",
        "If necessary, search the web using DuckDuckGo for additional information"
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

def get_fitness_plan(
        age: int, weight: float, height: float, 
        activity_level: str, fitness_level: str, 
        fitness_goal: str):
    prompt = (
        f"Generate a workout plan for a {age}-year-old person" 
        f"weighing {weight} kilograms, {height} centimeters tall, " 
        f"with an activity level of '{activity_level}', " 
        f"and a fitness level of '{fitness_level}' " 
        f"aiming to achieve '{fitness_goal}'. " 
        f"Include warm-up, exercises and cool-downs"
    )
    return exercise_planner.run(prompt)
