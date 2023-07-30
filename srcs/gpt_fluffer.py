""" Module to fluff text using GPT-3. """
import openai


class GPTFluffer:
    """Class to fluff text using GPT-3."""

    def __init__(self, key):
        openai.api_key = key

    def fluff(self, text):
        """Returns the fluffed text."""
        preprompt = (
            "You speak as the spirit protector of our house. Say in a poetic way : "
        )

        prompt = f"{preprompt} {text} \n\n"
        reponse = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        return reponse.choices[0].text
