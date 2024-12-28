import abc
from typing import Iterator, List


class LLMInterface(metaclass=abc.ABCMeta):

    def initialize(self, name, persona_prompt, model):
        raise NotImplementedError()

    def chat_iter(self, prompt: str) -> Iterator[str]:
        """
        Sends a chat prompt to an agent and return an iterator to the response.
        This function will have to store the user message and ai response back to the memory.

        Parameters:
        - prompt (str): The message or question to send to the agent.

        Returns:
        - Iterator[str]: An iterator to the response from the agent.
        """
        raise NotImplementedError

    def handle_interrupt(self, heard_response: str) -> None:
        """
        This function will be called when the LLM is interrupted by the user.
        The function needs to let the LLM know that it was interrupted and let it know that the user only heard the content in the heard_response.
        The function should either (consider that some LLM provider may not support editing past memory):
        - Update the LLM's memory (to only keep the heard_response instead of the full response generated) and let it know that it was interrupted at that point.
        - Signal the LLM about the interruption.

        Parameters:
        - heard_response (str): The last response from the LLM before it was interrupted. The only content that the user can hear before the interruption.
        """
        raise NotImplementedError

    def pause_execution(self, heard_response: str) -> None:
        """
        This function will be called when the LLM is generation is paused by the user for performing actions..
        The function needs to let the LLM know that it was paused and there is content yet to be generated..
        The function should either (consider that some LLM provider may not support editing past memory):
        Parameters:
        - heard_response (str): The last response from the LLM before it was paused. The only content that the user can hear before the interruption.
        """
        raise NotImplementedError

    def load_memory(self, list_of_block_labels: List[str]) -> None:

        """
        This function will load memory blocks for inference.
        Parameters:
        - list_of_block_labels (List[str]): The list of blocks to load into the LLM CORE Memory
        """

        raise NotImplementedError

    def create_persona(self,persona_prompt,persona_name) -> None:
        """

        Args:
            prompt_path:
            prompt_name:

        Returns:

        """

