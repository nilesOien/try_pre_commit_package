from fastapi import FastAPI
from pydantic import BaseModel

# Set up tags that appear in the documentation pages that FastAPI generates.
tags_metadata = [
    {
        "name": "theApp",
        "description": "An app that shows fast API serving out a dictionary.",
        "externalDocs": {
            "description": "How this documentation was added",
            "url": "https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags",
        },
    },
    {
        "name": "static-dict-service",
        "description": "An end point that serves out a static dictionary.",
    },
]


# Get an application object
theApp = FastAPI(
    title="Fast API Example",
    summary="Very simple instance of FastAPI that just serves out a static dictionary",
    description="Used here just to have something for pre-commit to test",
    contact={
        "name": "Niles Oien",
        "url": "https://nso.edu",
        "email": "noien@nso.edu",
    },
    version="1.0.0",
    openapi_tags=tags_metadata,
)

# Define a static dictionary
static_data = {
    "firstName": "Niles",
    "lastName": "Oien",
    "numPets": 5,
    "usesPiApproximation": 3.141,
    "likesAurorasTooMuch": True,
}


# Pydantic class (inherits from BaseModel) that defines our response schema.
# Lets the documentation be more detailed.
class theResponseClass(BaseModel):
    """
    This defines the schema for the JSON response.
    """

    firstName: str
    lastName: str
    numPets: int
    usesPiApproximation: float
    likesAurorasTooMuch: bool


# The actual service that serves out the static dict.
# Usually the dict would come from a database or something like that.
# As such it could be quite extensive (and often is in production systems).
# Here, it's just the static dictionary static_data that conforms to the schema
# defined by theResponseClass.
@theApp.get(
    "/static-dict", response_model=theResponseClass, tags=["static-dict-service"]
)
async def get_static_dict():
    """
    Returns the static_data dictionary as a JSON response.
    """
    return static_data
