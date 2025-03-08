# Simplified shell tool to execute only one command at a time

import logging
import platform
from shellix.memory import memory
from typing import Any, Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

MAX_OUTPUT_LENGTH = 100000


class ShellInput(BaseModel):
    command: str = Field(..., description="Single shell command to run.")


def _get_default_bash_process() -> Any:
    try:
        from langchain_experimental.llm_bash.bash import BashProcess
    except ImportError:
        raise ImportError(
            "BashProcess has been moved to langchain experimental."
            "To use this tool, install langchain-experimental "
            "with `pip install langchain-experimental`."
        )
    return BashProcess(return_err_output=True)


def _get_platform() -> str:
    system = platform.system()
    return "MacOS" if system == "Darwin" else system


class ShellTool(BaseTool):
    process: Any = Field(default_factory=_get_default_bash_process)

    name: str = "terminal"

    description: str = f"Run a single shell command on this {_get_platform()} machine at the current working directory."

    args_schema: Type[BaseModel] = ShellInput

    ask_human_input: bool = False

    def _run(
            self,
            command: str,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        print(f"Executing command: {command}")

        try:
            if self.ask_human_input:
                user_input = input("Proceed with command execution? (y/n): ").lower()
                if user_input != "y":
                    logger.info("User aborted command execution.")
                    return "User aborted command execution."

            result = self.process.run(command)
            if len(result) > MAX_OUTPUT_LENGTH:
                result = result[:MAX_OUTPUT_LENGTH] + "\n (output truncated)"

            if len(result) > 2000:
                memory.append(
                    {"role": "assistant", "content": f"Tool call, shell: {command} Result: {result[0:2000]}.."})
                print(result[0:2000] + '...')
            else:
                memory.append(
                    {"role": "assistant", "content": f"Tool call, shell: {command} Result: {result[0:2000]}"})
                print(result)

            return result

        except Exception as e:
            logger.error(f"Error during command execution: {e}")
            return str(e)
