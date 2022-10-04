# MIT License
#
# Copyright (c) 2022 Quandela
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, Dict, List

from perceval.utils import BasicState, SVDistribution, Parameter


class ProcessorType(Enum):
    SIMULATOR = 1
    PHYSICAL = 2


class AProcessor(ABC):
    def __init__(self):
        self._parameters = {}

    @property
    @abstractmethod
    def type(self) -> ProcessorType:
        pass

    @property
    @abstractmethod
    def is_remote(self) -> bool:
        pass

    def set_parameters(self, params: Dict):
        self._parameters = params

    def clear_parameters(self):
        self._parameters = {}

    @abstractmethod
    def with_input(self, input_state: BasicState) -> None:
        pass

    @property
    @abstractmethod
    def available_sampling_method(self) -> str:
        pass

    def samples(self, count: int, progress_callback: Callable = None) -> List[BasicState]:
        raise RuntimeError(f"Cannot call samples(). Available method is {self.available_sampling_method}")

    def sample_count(self, count: int, progress_callback: Callable = None) -> Dict[BasicState, int]:
        raise RuntimeError(f"Cannot call sample_count(). Available method is {self.available_sampling_method}")

    def probs(self, progress_callback: Callable = None) -> SVDistribution:
        raise RuntimeError(f"Cannot call probs(). Available method is {self.available_sampling_method}")

    @abstractmethod
    def get_circuit_parameters(self) -> Dict[str, Parameter]:
        pass

    @abstractmethod
    def set_circuit_parameters(self, params: Dict[str, Parameter]) -> None:
        pass
